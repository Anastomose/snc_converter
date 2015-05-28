import ast

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


def list_detect_type(v):
    """Returns literal eval of list object"""
    try:
        beta = ast.literal_eval(v)
    except ValueError:  # this catches malformed string error
        beta = v  # just hand back the input string
    return beta

