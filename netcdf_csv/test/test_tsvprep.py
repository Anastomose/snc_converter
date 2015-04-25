import pytest

from netcdf_csv import tsv_prep as ts

tfile = r'tdata/test_delim_tab.tsv'

def test_tsvprep():
    tsv_obj = ts.tsv_prep(tfile)

    assert tsv_obj.thisfile == 'tdata/test_delim_tab.tsv'

    for row in tsv_obj:
        assert type(row) is list
        assert row[0] is not None

        # if tsv_obj.current < 25:
        #     print row

        # if tsv_obj.start == 24:
        #    assert False

