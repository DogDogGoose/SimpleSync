import argparse
import os

import SimpleSync.core

###########################
# Global
###########################
gDBDefaultDir = '.'

# 
# Import local packages
#
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    # print(path.dirname(path.dirname(path.abspath(__file__))))
    pkgPath = path.dirname(path.dirname(path.abspath(__file__)))
    sys.path.append(pkgPath)

    gDBDefaultDir = os.path.join(pkgPath, 'Database')


###########################
# Main
###########################

parser = argparse.ArgumentParser(description='Synchronize two directories.')
parser.add_argument('--verbose', '-v', type=bool, default=True, help='Wow much talk.', dest='verbose')
parser.add_argument('--cfgdir', '-c', required=False, help='Directory of YAML configuration files; these will be executed in series by this script.')
parser.add_argument('--cfgfile', '-f', required=False, help='YAML config path; if provided, this is the only file that will be executed (ignores cfgdir option)')

args = parser.parse_args()

mysync = SimpleSync.core.SyncManager(args.verbose)
mysync.setDBDir(gDBDefaultDir)

#
# get the cfg dirs
#


#
# Iteratively process each cfg dir
#

