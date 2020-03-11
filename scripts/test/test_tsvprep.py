import pytest
import os

from netcdf_csv import tsv_prep as ts

tfile = os.path.join(os.path.split(__file__)[0], 'tdata', 'test_delim_tab.tsv')

def test_tsvprep():
    tsv_obj = ts.tsv_prep(tfile)

    assert os.path.split(tsv_obj.thisfile)[1] == 'test_delim_tab.tsv'

    for row in tsv_obj:
        assert type(row) is list
        assert row[0] is not None

        # if tsv_obj.current < 25:
        #     print row

        # if tsv_obj.start == 24:
        #    assert False

