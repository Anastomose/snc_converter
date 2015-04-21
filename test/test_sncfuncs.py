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
        assert type(r) is list
    # assert False


def test_create_var_data():
    """test create_variable_data function
    """
    temp = gen_setup()
    test_dict = sf.create_variable_data(temp)

    assert type(test_dict) is dict
    assert type(test_dict.keys()) is list
    assert test_dict.keys()[0] == 'fCO2_water_equi_uatm'  
    # assert False


def test_list_splitter():  
    """test list_splitter function for populating attributes
    """
    templist = [["conventions, a, b, c"], ["FeatureType, 1,2,3"]]
    alpha_list = sf.list_splitter(templist[0][0].split(','), 'conventions')
    beta_list = sf.list_splitter(templist[1][0].split(','), 'FeatureType')
    
    print templist[0], alpha_list
    print templist[1], beta_list

    assert type(alpha_list) is list
    assert len(alpha_list) is not None
    assert alpha_list[0] != []
    # assert False


def test_create_cfs():
    temp = gen_setup()

    conv, ft, dt = sf.create_cfs(temp)
    
    print conv
    print ft
    print dt

    assert type(conv) is list
    for i in [conv, ft, dt]:
        assert i != []
