import os
import ast

import snc_funcs as sf
import tsv_funcs as tf
import snc_variable as sv
import snc_dimension as sdm


reload(sf)  # kill for production
reload(tf)
reload(sv)


class Dataset(object):
    """
    Dataset object imitating netCDF Dataset

    *Class Attributes*

    :attributes: Dictionary of dataset attributes
    :dimensions: Dictionary of dataset variable dimensions
    :filepath: The file path used to instantiate the current dataset
    :globals: Attributes that apply to the entire dataset (e.g. conventions)
    :snc_DateTime: Not used
    :variables: Dictionary of dataset variable objects

    """

    """class attributes go here"""

    def __init__(self, file_string=None):
        # eventually want to update with argv
        self.snc_DateTime = None
        self.globals = {}  # globals go here
        self.attributes = {}  # multiple variables by column
        self.variables = {}  # collection of variable objects
        self.filepath = os.path.abspath(file_string)
        self.dimensions = {}

    def __str__(self):
        """Prints Dataset attributes
           access self.variables attributes and loop through keys to print"""
        tempkeys = [self.filepath]
        for k in self.variables:  # default is to loop through keys
            tempkeys.append(k)
        return '\n'.join(tempkeys)

    def createGlobal(self, gvarname, *args, **kwargs):
        """Sets global variable attributes

           :gvarname: variable that applies to the whole Dataset
           :args: values that follow gvars in the TSV
        """
        attrs = [i for i in args[0] if i != '']
        self.globals[gvarname] = attrs

    def createVariable(self, varname, *args, **kwargs):
        """Creates dataset variable

           :varname: variable name

           *kwargs*

           :datatype: type of data for each variable
           :dimensions: dimension of variable
        """
        var = sv.Variable(varname, *args, **kwargs)
        self.variables[varname] = var


    def setVarAttribute(self, var, *args, **kwargs):
        """Sets variable attributes
        """
        v = self.variables.get(var)
        v.attributes[kwargs['attribute']] = kwargs['description']

    def setVarData(self, varname, *args, **kwargs):
        """Sets variable data array

           setVarData(varname, data_array, **kwargs)
        """
        v = self.variables.get(varname)
        v.data_array.extend(args[0])

    def addVarDimension(self, varname):
        """Sets variable dimension in dataset

           Requires variable already exists and variable name is
           correctly passed to function.
        """
        v = self.variables.get(varname)
        if v:
            d = len(v.data_array)
            vd = sdm.Dimension(varname, d)
            self.dimensions[varname] = vd
        else:
            print 'Error: Bad key passed'

    @classmethod
    def readFromTSV(cls, file_string, globaltag="this_file"):
        """Creates Dataset class from TSV file

        :filestring: File string of the TSV file used to create the new
         class instance
        :globaltag: Tag used to identify attributers that apply to the
         entire TSV file. Default is *this_file*"""

        dataset = cls(file_string)

        tsv_lines = tf.tsv_read(file_string)
        tsv_scrub = [sf.list_item_scrub(r) for r in tsv_lines]
        # print tsv_scrub

        """
        use this_file tag to extract global variables
        variable data will follow the 'Start Data' tag
        """

        """find start and end of data"""
        sd = None
        ed = None
        for i, row in enumerate(tsv_scrub):
            if 'start data' in row:
                sd = i
            elif 'end data' in row:
                ed = i
        tsv_variables = tsv_scrub[sd+1]
        # print tsv_variables
        [dataset.createVariable(v) for v in tsv_variables]

        """set global and variable attributes from file"""
        for i, row in enumerate(tsv_scrub):
            if globaltag in row:
                print 'Found global attribute "{}"'.format(row[1])
                dataset.createGlobal(row[1], sf.list_split(row, row[1]))

            # set variable attributes and descriptions
            elif row[0] in tsv_variables and i < sd:
                print 'Found variable "{}" attribute: {}'.format(row[0], row[1])
                dataset.setVarAttribute(row[0], attribute=row[1],
                                        description=row[2])

        """create variable data arrays and update dataset"""
        tsv_dataarrays = [[] for n in tsv_variables]
        for l in tsv_scrub[sd+2:ed]:
            [tda.append(sf.list_detect_type(i)) for
             tda, i in zip(tsv_dataarrays, l)]

        variable_datasets = zip(tsv_variables, tsv_dataarrays)
        [dataset.setVarData(k, v) for k, v in variable_datasets]

        return dataset
