import snc_funcs as sf
import tsv_funcs as tf


class Variable(object):
    """variable object holds snc variables pulled from tsv
    """

    def __init__(self, name, datatype, dimensions=()):

        self.extra_variables = None
        self.variable = None
        self.name = name
        self.datatype = datatype
        self.dimensions = dimensions

    """seems like this class should just be a custom dict with additional methods"""

    def __keys__(self):
        return self.name

    def __items__(self):
        return self.name

    # def CreateVariable(self, tsv_file):
    #     """Returns variable dict from tsv file"""
    #     tsv_gen_object = tf.tsv_gen(tsv_file)
    #     self.variable = sf.create_variable_data(tsv_gen_object)
    #     return self.variable
