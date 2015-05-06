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



class tsv_blocks(object):
    """Breaks tsv file into usable blocks for snc_dataset
    """

    def __init__(self, filename):
        self.filename = filename
        self.reader_index = self.tsv_blanks(self.filename)

        with open(self.filename, 'rb') as fid:
            self.GlobalBlock = fid.read(self.reader_index[0])
            self.VarsAttrBlock = fid.read(self.reader_index[1])
            self.FeatIdBlock = fid.read(self.reader_index[2])
            self.VarsbyColBlock = fid.read(self.reader_index[3])        

    
    def tsv_tabs(self, tsv_line):
        """Returns True on blank lines in tsv file"""
        alpha = re.search('^(\\t)*\r\n', tsv_line)
        if alpha:
            return True


    def tsv_blanks(self, filename):
        """Returns number of bytes to read between blank rows"""
        line_index = []
        with open(filename, 'rb') as fid:
            fid.read()
            eof = fid.tell()
            fid.seek(0)

            while fid.tell() != eof:
                row = fid.readline()
                if self.tsv_tabs(row):
                    # print fid.tell()
                    line_index.append(fid.tell())

        i = line_index[0]
        reader_index = []
        reader_index.append(i)

        for v in line_index[1:]:
            reader_index.append(v-i)
            i = v

        return reader_index


