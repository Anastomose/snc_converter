class Variable(object):
    """variable object holds snc variables pulled from tsv
    """

    def __init__(self, name, datatype = None, dimensions=()):

        self.extra_variables = None
        self.name = name
        self.datatype = datatype
        self.dimensions = dimensions
        self.attributes = {}  # header info goes here
        self.data_array = []  # think about np array later

    """seems like this class should just be a custom dict with additional methods"""

    def __key__(self):
        return self.name

    # def CreateVariable(self, tsv_file):
    #     """Returns variable dict from tsv file"""
    #     tsv_gen_object = tf.tsv_gen(tsv_file)
    #     self.variable = sf.create_variable_data(tsv_gen_object)
    #     return self.variable

