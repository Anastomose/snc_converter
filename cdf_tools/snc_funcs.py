import csv

def csv_read(filename):
    """generator that returns each line from excel-tab separated file
    """
    with open(filename, 'rb') as fid:
        reader = csv.reader(fid, dialect='excel-tab')

        for row in reader:
            yield row

def var_headers(line):
    """returns list of variable header values
       function depricated
    """
    dict_keys = [k for k in line[0].split(',')]
    return dict_keys