import csv
import re


def csv_read(filename):
    """generator that returns each line from excel-tab separated file

       quoted lines are returned as single item list
       tab-separated values are returned as a list of values per line
    """
    with open(filename, 'rb') as fid:
        reader = csv.reader(fid, dialect='excel-tab')

        for row in reader:
            yield row


def gen_cleanup(gen):
    try:
        gen.close()
    except AttributeError:
        pass


def create_cfs(gen):
    """create conventions, FeatureType, snc_DateTime attributes from
       tsv header lines as a 3 x tuple

       See example for formatting:, keywords are:

            + conventions
            + FeatureType
            + snc_DateTime
       
        Lines must be quoted in order to be processed with current tooling
    """
    conv = []
    ft = []
    dt = []

    for r in gen:
        n_line = list_item_scrub(r)
        if 'conventions' in n_line:
            conv += list_splitter(n_line, 'conventions')
        elif 'featuretype' in n_line:
            ft += list_splitter(n_line, 'featuretype')
        elif 'snc_datetime' in n_line:  # re.search('date', n_line)
            dt += list_splitter(n_line, 'snc_datetime')

        # note here we may need to create a checker for the snc obj
        # to deal with cases where more than 1 line has the same kwarg

    gen_cleanup(gen)


def list_splitter(l, kwarg):
    """returns items in header line following kwarg
    """
    if kwarg in l:
        arg_address = l.index(kwarg) + 1
        return l[arg_address:]


def list_item_scrub(l):
    """returns csv split line from attributes at top of snc_tsv file
    """
    line = l[0].split(',')
    temp_line = [i.lower() for i in line]
    n_line = [j.strip(' ') for j in temp_line]
    return n_line


def create_variable_data(gen):
    """creates variable data dict from csv generator between 'Start data'
        and 'End data' tags
    """
    for row in gen:
        if 'Start data' in row:
            varHeaderValues = gen.next()  # var_headers(headerline)
            varValues = [[] for l in range(0, len(varHeaderValues))]
            break

    # here we take existing generator's state and append data values
    for row in gen:
        if 'End data' not in row:
            [vV.append(r) for vV, r in zip(varValues, row)]
    variable_data = {vH: vV for vH, vV in zip(varHeaderValues, varValues)}
    gen_cleanup(gen)
    return variable_data


def create_extra_variables(gen):
    for row in gen:
        n_row = list_item_scrub(row)
        if 'snc_extra_variables' in list_item_scrub(n_row):
            addr = n_row.index('snc_extra_variables')
            ex_vars = n_row[addr:]


