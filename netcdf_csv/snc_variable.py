import snc_funcs as sf
import tsv_funcs as tf


class Variable(object):
    """variable object holds snc variables pulled from tsv
    """

    def __init__(self, tsv_file):

        self.extra_variables = None
        self.variable = None

    def CreateVariable(self, tsv_file):
        tsv_gen_object = tf.tsv_gen(tsv_file)
        self.variable = sf.create_variable_data(tsv_gen_object)
        tsv_gen_object.close()
