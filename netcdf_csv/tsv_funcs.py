import csv
import re


def tsv_read(filename):
    """Creates list of lists with all tsv file contents"""
    with open(filename, 'rb') as fid:
        reader = csv.reader(fid, dialect='excel-tab')
        file_content = [row for row in reader]
        return file_content


def tsv_gen(filename):
    """generator that returns each line from excel-tab separated file

       quoted lines are returned as single item list
       tab-separated values are returned as a list of values per line
    """
    with open(filename, 'rb') as fid:
        reader = csv.reader(fid, dialect='excel-tab')
        for row in reader:
            yield row