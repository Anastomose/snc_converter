import pytest
import os
import sys

from netcdf_csv import snc_dataset as sd


def test_snc_dataset():
    tempclass = sd.Dataset('test_delim_tab.tsv')
    assert tempclass is not None


def test_sncd_str():
    tempclass = sd.Dataset('test_delim_tab.tsv')
    strvar = str(tempclass)
    assert 'test_delim_tab.tsv' in strvar
    # assert False