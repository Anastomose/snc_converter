
from snc_funcs import (csv_read, 
                       var_headers,
                       )


class snc_read(object):
    """
    creates object from tsv file set up for conversion to netCDF
    """

    def __init__(self, tsv_file):
        self.tsv_file = tsv_file
        
        # snc attributes that will be used
        # current values scraped from test file
        self.conventions = []
        self.FeatureType = []
        self.snc_DateTime = []
        self.snc_Extra_variables = dict()

        # snc variables 
        self.VariableHeaders = dict()  # dict will hold, header: std_name, long_name, units, missing value, ioos_cat
        
        # self.VariableValues = dict() # create dict keys from line following "Start data", assign values from columns that follow
        reader_object = csv_read(self.tsv_file)

        for row in reader_object:
            if 'Start data' in row:
                # headerline = 
                varHeaderValues = reader_object.next()  # var_headers(headerline)
                varValues =[[] for l in range(0, len(varHeaderValues))]
                break

        # here we take existing generator's state and append data values
        for row in reader_object:
            if 'End data' not in row:
                # temp_r = row[0].split(',')
                [vV.append(r) for vV, r in zip(varValues, row)]

        self.VariableValues = {vH: vV for vH, vV in zip(varHeaderValues, varValues)}
