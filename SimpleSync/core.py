
import string
import SimpleSync.syncdb

###########################
class SyncManager(object):
    """
    Main
    """
    def __new__(cls, verbose=False):
        newobj = object.__new__(cls)
        newobj.verbose = verbose
        newobj.dbpath = '.'
        newobj.db = SimpleSync.syncdb.syncdb(verbose)

        return newobj 

    def __init__(self, bidirectional=True, verbose=False):
        self.verbose = verbose
        self.bidirectional = bidirectional

    def __str__(self):
        return ""

    # TODO: change this to changing the config dir
    def setOutputDir(self, odir):
        return
   
    def setDBDir(self, targetdir):
        self.dbpath = targetdir

    def processDir(self, targetdir):
        myconnection = self.db.initConnectionForDir(targetdir)
        return
       
