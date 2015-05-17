import os
import ast

import snc_funcs as sf
import tsv_funcs as tf
import snc_variable as sv


reload(sf)  # kill for production
reload(tf)
reload(sv)


class Dataset(object):
    """
    Dataset object imitating netCDF Dataset
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
           createGlobal(global variable, attribute, **kwargs)
        """
        attrs = [i for i in args[0] if i != '']
        self.globals[gvarname] = attrs

    def createVariable(self, varname, *args, **kwargs):
        """Creates dataset variable
           createVariable(variable name, datatype, dimensions, **kwargs)
           """
        var = sv.Variable(varname, *args, **kwargs)
        self.variables[varname] = var

    def setVarAttribute(self, var, *args, **kwargs):
        """Sets variable attributes
           setVarAttribute(var, attribute=attribute, description=description)
           """
        v = self.variables.get(var)
        v.attributes[kwargs['attribute']] = kwargs['description']

    def setVarData(self, varname, *args, **kwargs):
        """Set variable data array
        setVarData(varname, data array, **kwargs)
        """
        v = self.variables.get(varname)
        v.data_array.extend(args[0])

    @classmethod
    def readFromTSV(cls, file_string):
        """Creates Dataset class from TSV file"""
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
            if 'this_file' in row:
                print 'Found global {}'.format(row[1])
                dataset.createGlobal(row[1], sf.list_split(row, row[1]))

            # set variable attributes and descriptions
            elif row[0] in tsv_variables and i < sd:
                print 'Found variable {} attribute {}'.format(row[0], row[1])
                dataset.setVarAttribute(row[0], attribute = row[1], 
                                        description = row[2])

        """create variable data arrays and update dataset"""
        tsv_dataarrays = [[] for n in tsv_variables]
        for l in tsv_scrub[sd+2:ed]:
            [vV.append(i) for vV, i in zip(tsv_dataarrays, l)]

        variable_datasets = zip(tsv_variables, tsv_dataarrays)
        [dataset.setVarData(k, v) for k, v in variable_datasets]

        return dataset
