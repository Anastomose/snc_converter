from snc_funcs import (csv_read,
                       create_variable_data,
                       create_cfs)


class snc_create(object):
    """
    creates object from tsv file set up for conversion to netCDF

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

    def __init__(self, tsv_file):
        self.tsv_file = tsv_file  # eventually want to update with argv

        # snc attributes that will be used
        # current values scraped from test file
        reader_object = csv_read(self.tsv_file)
        self.conventions, self.FeatureType, self.snc_DateTime \
            = create_cfs(reader_object)

        self.snc_Extra_variables = dict()

        self.VariableHeaders = dict()
        """dict will hold, header: std_name, long_name,
           units, missing value, ioos_cat"""

        reader_object = csv_read(self.tsv_file)
        self.VariableValues = create_variable_data(reader_object)
