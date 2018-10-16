
import sqlite3

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

    def initConnectionForDir(self, dirpath):
        mydbfile = self.getdbpath(dirpath)
        try:
            self.db = sqlite3.connect(mydbfile)
            return
        except:
            print ("ERROR loading database")

