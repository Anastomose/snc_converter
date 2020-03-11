class Variable(object):
    """Class holds a variable pulled from a snc dataset

       *Class Attributes*

       :attributes: A dictionary of the variable attributes. For example
        the variable 'temperature' may include an attribute 'long name' with
        a value of 'Temperature in degrees celsius'.
       :datatype: Type of data stored.
       :data_array: A list that holds the variable data.
       :dimensions: The dimensions of the data array. For one-dimensional
        data arrays this will be the length of the list.
       :extra_variables: Currently not used.
       :name: Name of the variable.
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

