import pytest
import os
import sys

# add current directory to path so mods can be imported
sys.path.append(os.path.abspath(os.curdir))

from cdf_tools import snc_funcs as sf

t_file = 'tdata/test_delim_tab.tsv'

def gen_setup():
    """returns generator for testing
    """
    temp = sf.csv_read(t_file)
    for row in temp:
        yield row

def test_reader():
    """test csv_read function"""
    temp = gen_setup()

    for r in temp:
        assert r is not None
        assert r[0] is not None

    assert False

def test_var_header():
    """test var_headers row function
    """
    temp = gen_setup()
    for line in temp:
        if 'Start data' in line:
            headers = sf.var_headers(temp.next())
            break

    assert type(headers) is list
    assert False


