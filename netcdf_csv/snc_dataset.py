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
        # loop through here to list variable keys in __str__ method
        return '\n'.join(pstr)

    def read_header(self):
        # read from header information
        pass

    def createVariable(self, varname, datatype, dimensions=()):
        var = sv.Variable
        self.variables[varname] = var
