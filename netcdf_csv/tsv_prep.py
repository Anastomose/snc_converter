import csv


class tsv_prep(object):
    """Returns an iterator with tsv file content"""

    def __init__(self, filename):
        self.thisfile = filename
        self.filecontents = self.fid_read(filename)
        self.start = -1
        self.stop = len(self.filecontents)

    def __iter__(self):
        self.current = self.start
        return self

    def next(self):
        self.current += 1
        if self.current < self.stop:
            return self.filecontents[self.current]
        else:
            raise StopIteration

    def fid_read(self, filename):
        with open(filename, 'rb') as fid:
            reader = csv.reader(fid, dialect='excel-tab')
            file_content = [row for row in reader]
        return file_content
