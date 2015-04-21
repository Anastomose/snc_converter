from snc_funcs import (csv_read, 
                       create_variable_data,
                       create_cfs)


class snc_create(object):
    """
    creates object from tsv file set up for conversion to netCDF
    """

    def __init__(self, tsv_file):
        self.tsv_file = tsv_file # eventually want to update with argv
        
        # snc attributes that will be used
        # current values scraped from test file
        reader_object = csv_read(self.tsv_file)
        self.conventions, self.FeatureType, self.snc_DateTime \
            = create_cfs(reader_object)


        self.snc_Extra_variables = dict()

        # snc variables 
        self.VariableHeaders = dict()  # dict will hold, header: std_name, long_name, units, missing value, ioos_cat
        
        # self.VariableValues = dict() # create dict keys from line following "Start data", assign values from columns that follow
        reader_object = csv_read(self.tsv_file)
        self.VariableValues = create_variable_data(reader_object)
