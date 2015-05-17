import pytest
import os
import sys
import re

from netcdf_csv import snc_dataset as sd

t_file = os.path.join(os.path.split(__file__)[0], 'tdata', 'snc_trajectory.tsv')


def test_snc_dataset():
    tempclass = sd.Dataset(t_file)
    assert tempclass is not None


def test_sncd_str():
    tempclass = sd.Dataset.readFromTSV(t_file)

    strvar = str(tempclass)
    assert strvar is not None
    assert re.search('snc_trajectory.tsv', strvar)
    assert re.search('cruisename', strvar)
    # assert False
