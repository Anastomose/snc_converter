import csv
import re


def tsv_read(filename):
    """creates list object with all tsv file contents"""
    with open(filename, 'rb') as fid:
        reader = csv.reader(fid, dialect='excel-tab')
        file_content = [row for row in reader]
        return file_content


def tsv_gen(filename):
    """generator that returns each line from excel-tab separated file

       quoted lines are returned as single item list
       tab-separated values are returned as a list of values per line
    """
    with open(filename, 'rb') as fid:
        reader = csv.reader(fid, dialect='excel-tab')
        for row in reader:
            yield row


def create_cfs(list_object):
    """
    .. py:function:: create_cfs(generator)

       Returns conventions, FeaturType, DateTime attributes from
       the tsv file identified in csv_read function.

       create conventions, FeatureType, snc_DateTime attributes from
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

    for r in list_object:
        n_line = list_item_scrub(r)
        if 'conventions' in n_line:
            conv += list_splitter(n_line, 'conventions')
        elif 'featuretype' in n_line:
            ft += list_splitter(n_line, 'featuretype')
        elif 'snc_datetime' in n_line:  # re.search('date', n_line)
            dt += list_splitter(n_line, 'snc_datetime')

        # note here we may need to create a checker for the snc obj
        # to deal with cases where more than 1 line has the same kwarg
    return (conv, ft, dt)


def list_splitter(l, kwarg):
    """returns items in header line following kwarg
    """
    if kwarg in l:
        arg_address = l.index(kwarg) + 1
        return l[arg_address:]


def list_item_scrub(l):
    """Returns csv split line from attributes at top of snc_tsv file

       note this function is specific to lines that are not tsv
    """
    line = l[0].split(',')
    n_line = [i.lower().strip() for i in line]
    return n_line


def create_variable_data(gen):
    """creates variable data dict from csv generator between 'Start data'
        and 'End data' tags
    """
    for row in gen:
        if 'Start data' in row[0]:
            varHeaderValues = gen.next()  # var_headers(headerline)
            varValues = [[] for l in range(0, len(varHeaderValues))]
            break

    # here we take existing generator's state and append data values
    for row in gen:
        if 'End data' not in row:
            [vV.append(r) for vV, r in zip(varValues, row)]

    variable_data = {vH: vV for vH, vV in zip(varHeaderValues, varValues)}
    return variable_data


def create_extra_variables(gen):
    ex_vars = None
    n=0
    for row in gen:
        n+=1
        n_row = list_item_scrub(row)
        if 'snc_extra_variables' in n_row:
            addr = n_row.index('snc_extra_variables')
            ex_vars = n_row[addr:]
            exvar_dict = dict()
            (exvar_dict.setdefault(ex, []) for ex in ex_vars)

        if ex_vars:
            for ex in ex_vars:
                if ex in n_row:
                    print ex
                    print n_row
                    temp_item = exvar_dict.get(ex)
                    ext_item = temp_item.append((row[1], row[2]))
                    exvar_dict[ex] = ext_item
                    print exvar_dict[ex]

        # if n < 25:
        #     print n_row

    return exvar_dict






