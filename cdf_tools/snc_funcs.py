import csv

def csv_read(filename):
    """generator that returns each line from excel-tab separated file
    """
    with open(filename, 'rb') as fid:
        reader = csv.reader(fid, dialect='excel-tab')

        for row in reader:
            yield row

def create_variable_data(gen):
    """creates variable data dict from csv generator
    """
    for row in gen:
        if 'Start data' in row:
            # headerline = 
            varHeaderValues = gen.next()  # var_headers(headerline)
            varValues =[[] for l in range(0, len(varHeaderValues))]
            break

    # here we take existing generator's state and append data values
    for row in gen:
        if 'End data' not in row:
            # temp_r = row[0].split(',')
            [vV.append(r) for vV, r in zip(varValues, row)]
    variable_data = {vH: vV for vH, vV in zip(varHeaderValues, varValues)}
    return variable_data