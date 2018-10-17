import os
import sqlite3

###########################
SYNCDB_DATABASE_NAME = 'SimpleSync.db'

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

    def getDBPath (self, dirpath):
        return os.path.join (self.dbpath, SYNCDB_DATABASE_NAME)

    def initConnectionForDir(self, dirpath):
        mydbfile = self.getDBPath(dirpath)
        if os.path.isfile(mydbfile):
            try:
                self.db = sqlite3.connect(mydbfile)
                return
            except:
                print ("ERROR loading database")


