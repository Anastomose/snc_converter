import pytest
import os
import sys
import re

from netcdf_csv import snc_dataset as sd

t_file = os.path.join(os.path.split(__file__)[0], 'tdata', 'snc_trajectory.tsv')


def test_snc_dataset():
    tempclass = sd.Dataset(t_file)
    assert tempclass is not None


def test_snc_str():
    tempclass = sd.Dataset.readFromTSV(t_file)

    strvar = str(tempclass)
    assert strvar is not None
    assert re.search('snc_trajectory.tsv', strvar)
    assert re.search('cruisename', strvar)
    # assert False

def test_snc_create():
    tc = sd.Dataset()
    tc.createGlobal('new_global', ['text'])
    tc.createVariable('new_var')
    tc.setVarAttribute('new_var', attribute='attribute1',
                       description='description text')
    v = tc.variables.get('new_var')

    assert tc.globals != {}
    assert 'text' in tc.globals.get('new_global')
    assert tc.variables != {}
    assert v.attributes.get('attribute1') is 'description text'

def test_snc_setData():
    tc = sd.Dataset.readFromTSV(t_file)
    v_temp = tc.variables.get('temp')
    vd = v_temp.data_array
    # print vd

    assert type(vd) is list

    try: float(vd[0])
    except ValueError: assert False 
    assert False
