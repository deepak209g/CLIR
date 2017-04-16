import codecs


class Corpus(object):
    def __init__(self, foreign_file, native_file):
        self.f_file = codecs.open(foreign_file, 'r', encoding="utf-8")
        self.e_file = codecs.open(native_file, 'r', encoding="utf-8")
        self.f_line = ''
        self.e_line = ''

    def __del__(self):
        self.f_file.close()
        self.e_file.close()

    def back_to_top(self):
        """reset file pointers to the beginning of the files"""
        self.f_file.seek(0, 0)
        self.e_file.seek(0, 0)

    def has_more(self):
        """returns true if
        their are more lines to be read else returns false"""
        self.f_line = self.f_file.readline()
        self.e_line = self.e_file.readline()
        if self.f_line == '':
            return False
        else:
            return True

    def next_f_line(self):
        """returns next french line"""
        return self.f_line

    def next_e_line(self):
        """returns next english line"""
        return self.e_line
