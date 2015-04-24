import snc_funcs as sf


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

        tsv_gen_object = sf.tsv_gen(tsv_file)
        self.conventions, self.FeatureType, self.snc_DateTime \
            = sf.create_cfs(tsv_gen_object)

        self.VariableValues = sf.create_variable_data(tsv_gen_object)
        tsv_gen_object.close()

        self.VariableHeaders = self.VariableValues.keys()
        """dict will hold, header: std_name, long_name,
           units, missing value, ioos_cat"""

        tsv_list = sf.tsv_read(self.tsv_file)
        self.snc_Extra_variables = sf.create_extra_variables(tsv_list)
