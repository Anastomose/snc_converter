
import csv

class snc_read(object):
    """
    creates object from tsv file set up for conversion to netCDF
    """

    def __init__(self, tsv_file):
        self.tsv_file = tsv_file

    def csv_read(self):
        """generator that returns lines from excel-tab separated file
        """
        with open(self.tsv_file, 'rb') as fid:
            reader = csv.reader(fid, dialect='excel-tab')

            for row in reader:
                yield row
