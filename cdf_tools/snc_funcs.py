import csv


def csv_read(filename):
    """generator that returns each line from excel-tab separated file

       quoted lines are returned as single item list
       tab-separated values are returned as a list of values per line
    """
    with open(filename, 'rb') as fid:
        reader = csv.reader(fid, dialect='excel-tab')

        for row in reader:
            yield row


def create_cfs(gen):
    """create conventions, FeatureType, snc_DateTime attributes from
       tsv header lines as a 3 x tuple

       See example for formatting:, keywords are:
            + conventions
            + FeatureType
            + snc_DateTime
    """
    conv = []
    ft = []
    dt = []

    for r in gen:
        line = r[0].split(',')
        n_line = [l.lower() for l in line]
        if 'conventions' in n_line:
            conv += list_splitter(line, 'conventions')
        elif 'FeatureType' in n_line:
            ft += list_splitter(line, 'featuretype')
        elif 'snc_DateTime' in n_line:
            dt += list_splitter(line, 'snc_datetime')

    try: 
        gen.close()
    except AttributeError:
        pass
    return (conv, ft, dt)



def list_splitter(l, kwarg):
    """returns items in header line following kwarg
    """
    if kwarg in l:
        arg_address = l.index(kwarg) + 1
        return l[arg_address:]



def create_variable_data(gen):
    """creates variable data dict from csv generator between 'Start data'
        and 'End data' tags
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

    try:
        gen.close()
    except AttributeError:
        pass
    return variable_data