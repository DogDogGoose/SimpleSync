
import string
import os
import re
import pprint

###########################
class ptabgrab(object):
    """
    Main
    """
    def __new__(cls, verbose=False):
        newobj = object.__new__(cls)
        newobj.verbose = verbose
        return newobj 

    def __init__(self, bidirectional=True, verbose=False):
        self.verbose = verbose
        self.bidirectional = bidirectional

    def __str__(self):
        return ""

    # TODO: change this to changing the config dir
    def setOutputDir(self, odir):
        newodir = os.path.join(odir, '')
        if not os.path.isdir(newodir):
            os.makedirs(newodir)

        self.outdir = newodir
        return
    
