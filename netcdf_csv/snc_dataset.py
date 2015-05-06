import os
import csv

import snc_funcs as sf
reload(sf) # kill for production

import tsv_funcs as tf
reload(tf)

import snc_variable as sv
reload(sv)


class Dataset(object):
    """
    Creates dataset object from tsv file set up for conversion to netCDF
    """

    def __init__(self, file_string=None):
        # eventually want to update with argv
        self.tsv_file = file_string
        self.snc_DateTime = None
        self.attributes = {}
        self.variables = {}  # sf.create_variable_data(file_string)

        self.filepath = os.path.abspath(file_string)
        self.dimensions = {}

        # use createVariable to update variables
        # try:
        tsv_gen_object = tf.tsv_gen(file_string)
        variableDict = sf.create_variable_data(tsv_gen_object)
        variabletypes = [type(variableDict.get(t)[0]) for t
                         in variableDict.keys()]

        for k, t in zip(variableDict.keys(), variabletypes):
            self.createVariable(k, t)
            # print '{} variable of type {} created'.format(k, t)
        # except Exception:
        #     print 'An exception occurred trying to autoload variables'

    def __str__(self):
        """Prints Dataset attributes"""
        rtsv = tf.tsv_blocks(self.tsv_file)
        global_raw = rtsv.GlobalBlock
        ivars_attr_raw = rtsv.VarsAttrBlock
        feature_id_raw = rtsv.FeatIdBlock
        vars_column_raw = rtsv.VarsbyColBlock

        pstr = []
        pstr.append(self.filepath)
        pstr.append('Globals:')
        pstr.append(global_raw.strip('\r\n'))
        pstr.append('Individual Variable Attributes:')
        pstr.append(ivars_attr_raw.strip('\r\n'))
        pstr.append('Feature IDs:')
        pstr.append(feature_id_raw.strip('\r\n'))
        pstr.append('Variables by Column Attributes:')
        pstr.append(vars_column_raw.strip('\r\n'))
        return '\n'.join(pstr)

    # def read_header(self):
    #     """Returns parsed header above 'start data' tag in file"""
    #     read_hdr = tf.tsv_gen(self.tsv_file)
    #     rh_output = []
    #     for row in read_hdr:
    #         rl = sf.list_item_scrub(row)
    #         if 'start data' not in rl:
    #             rh_output.append(rl)
    #     pretty_rho = [' '.join(r) for r in rh_output]
    #     return pretty_rho

    def read_variables(self):
        """Returns list of variables"""
        read_var = tf.tsv_gen(self.tsv_file)
        for row in read_var:
            if 'start data' in sf.list_item_scrub(row):
                vars_list = read_var.next()
        return vars_list

    def createVariable(self, varname, datatype, dimensions=()):
        var = sv.Variable(varname, datatype)
        self.variables[varname] = var
