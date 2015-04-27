import pytest
import os
import sys

# add current directory to path so mods can be imported
sys.path.append(os.path.abspath(os.curdir))

from netcdf_csv import snc_funcs as sf
from netcdf_csv import tsv_funcs as tf

tdir = os.path.join(os.path.split(__file__)[0], 'tdata')


def test_fail():
    print 'test file func'
    print tdir
    print __file__


t_file = os.path.join(tdir, 'snc_trajectory.tsv')
temp = tf.tsv_read(t_file)


def gen_setup():
    """returns generator for testing
    """
    gen = tf.tsv_gen(t_file)
    return gen


def test_reader():
    """test csv_read function"""
    # temp = gen_setup()

    for r in temp:
        assert r is not None
        assert r[0] is not None
        assert type(r) is list
    # assert False


def test_create_var_data():
    """test create_variable_data function
    """
    temp_gen = gen_setup()
    t_dict = sf.create_variable_data(temp_gen)

    assert type(t_dict) is dict
    assert type(t_dict.keys()) is list
    print t_dict.keys()[0]
    assert t_dict.keys()[0] == 'cruiseName'
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
    assert type(temp) is list
    conv, ft, dt = sf.create_cfs(temp)
    print conv
    print ft
    print dt
    assert type(conv) is list
    for i in [conv, ft]:
        assert i != []
    # assert False

# def test_create_exvars():
#     exv_dict = sf.create_extra_variables(temp)
#     assert type(exv_dict) is dict
#     assert exv_dict.get('vessel_name') is not None
#     assert exv_dict.keys() == ['vessel_name', 'dataset_name']
#     assert False