import pytest
import os
import sys

from netcdf_csv import snc_dataset as sd


t_file = os.path.join(os.path.split(__file__)[0], 'snc_trajectory.tsv')

def test_snc_dataset():
    tempclass = sd.Dataset(t_file)
    assert tempclass is not None


def test_sncd_str():
    tempclass = sd.Dataset(t_file)
    strvar = str(tempclass)
    assert 'snc_trajectory.tsv' in strvar
    # assert False
