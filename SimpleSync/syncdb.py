
import pprint

###########################
class syncdb(object):
    """
    Main
    """
    def __new__(cls, verbose=False):
        newobj = object.__new__(cls)
        newobj.verbose = verbose
        return newobj 

    def __init__(self, verbose=False):
        self.verbose = verbose

    def __str__(self):
        return ""

    def initdb(self, dbfile):
        try:
            return sqlite3.connect(dbfile)
        except:
            print "ERROR loading database (%s)" % (dbfile)
    
