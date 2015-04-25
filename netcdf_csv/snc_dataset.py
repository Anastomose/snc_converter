import os

import snc_funcs as sf
reload(sf) # kill for production

import tsv_funcs as tf
reload(tf)


class Dataset(object):
    """
    creates dataset object from tsv file set up for conversion to netCDF

    initialization creates the following attributes from the tsv file
    based on current example formatting:

    (note, this is brittle right now and not very flexible)

    + tsv_file
    + conventions: list of conventions used
    + FeatureType: list of features in file
    + snc_DateTime: datetime convention used
    + ExtraVars: extra variables
    + VarHeaders: variable header dict
    + VarValues: variable name and values dict
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
        return '\n'.join(pstr)

    def read_header(self):
        # read from header information
        pass
