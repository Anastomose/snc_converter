
def create_variable_data(gen):
    """Returns variable dictionary from tsvgen

       Creates variable data dict from tsv generator between
       'Start data' and 'End data' tags.
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


def list_split(l, kwarg):
    """Returns items in list that follow location of  kwarg
    """
    if kwarg in l:
        arg_address = l.index(kwarg) + 1
        return l[arg_address:]


def list_item_scrub(l):
    """Returns list of values from tsv-split line scrubbed of spaces
       and smashed to lower()

       Note this function is specific to lines that are not parsed by
       csv module in selected dialect
    """
    n_line = [i.lower().strip(' ') for i in l]
    return n_line





