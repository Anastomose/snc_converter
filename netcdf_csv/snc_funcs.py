
def create_cfs(list_object):
    """
    Returns conventions, FeatureType, DateTime  attributes from
    list_object parsed by tsv_funcs.tsv_read()

    See example for formatting:, keywords are:

         + conventions
         + FeatureType
         + snc_DateTime
    """
    conv = []
    ft = []
    dt = []

    for r in list_object:
        n_line = list_item_scrub(r)  # quoted line needs to be scrubbed
        if 'conventions' in n_line:
            conv += list_splitter(n_line, 'conventions')
        elif 'featuretype' in n_line:
            ft += list_splitter(n_line, 'featuretype')
        elif 'snc_datetime' in n_line:  # re.search('date', n_line)
            dt += list_splitter(n_line, 'snc_datetime')

        # note here we may need to create a checker for the snc obj
        # to deal with cases where more than 1 line has the same kwarg
    return (conv, ft, dt)


def create_variable_data(gen):
    """Creates variable data dict from csv generator between 'Start data'
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


def list_splitter(l, kwarg):
    """Returns items in list that follow location of  kwarg
    """
    if kwarg in l:
        arg_address = l.index(kwarg) + 1
        return l[arg_address:]


def list_item_scrub(l):
    """Returns list of values from csv-split line scrubbed of spaces and smashed to lower()

       Note this function is specific to lines that are not tsv in test file header
    """
    # line = l[0].split(',')
    n_line = [i.lower().strip() for i in l]
    return n_line





