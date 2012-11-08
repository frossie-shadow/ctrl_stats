import re
from record import Record

class Executing(Record):
    # event number: 001
    def __init__(self, year, lines):
        Record.__init__(self, year, lines)

        pat = r"\<(?P<hostAddr>\d+.\d+.\d+.\d+:\d+)\>"

        values = re.search(pat,lines[0]).groupdict()
        self.executingHostAddr = values["hostAddr"]

    def printAll(self):
        Record.printAll(self)
        print "executingHostAddr = ",self.executingHostAddr

    def describe(self):
        s = "%s host=%s" % (self.timestamp, self.executingHostAddr)
        return s