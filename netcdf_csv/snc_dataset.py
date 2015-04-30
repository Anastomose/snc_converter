import os

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

    def __init__(self, file_string = None):
        # eventually want to update with argv
        self.tsv_file = file_string
        self.snc_DateTime = None
        self.attributes = {}
        self.variables = {}

        self.filepath = os.path.abspath(file_string)
        self.dimensions = {}

    # def CreateConventions(self, tsv_file):
    #     tsv_gen_object = tf.tsv_gen(tsv_file)

    #     self.conventions, self.FeatureType, self.snc_DateTime = sf.create_cfs(tsv_gen_object)

    def __str__(self):
        pstr = []
        pstr.append(self.filepath)
        pstr + self.read_header()
        pstr.append('Variables:')
        pstr.append('\n'.join(self.read_variables()))
        # loop through here to list variable keys in __str__ method
        return '\n'.join(pstr)

    def read_header(self):
        """Returns parsed header above 'start data' tag in file"""
        read_hdr = tf.tsv_gen(self.tsv_file)
        rh_output = []
        for row in read_hdr:
            rl = sf.list_item_scrub(row)
            if 'start data' not in rl:
                rh_output.append(rl)
        pretty_rho = [' '.join(r) for r in rh_output]
        return pretty_rho

    def read_variables(self):
        """Returns list of variables"""
        read_var = tf.tsv_gen(self.tsv_file)
        for row in read_var:
            if 'start data' in sf.list_item_scrub(row):
                vars_list = read_var.next()
        return vars_list

    def createVariable(self, varname, datatype, dimensions=()):
        var = sv.Variable(name, datatype)
        self.variables[varname] = var
