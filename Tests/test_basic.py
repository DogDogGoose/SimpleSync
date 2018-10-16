import argparse

# 
# Import local packages
#
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    # print(path.dirname(path.dirname(path.abspath(__file__))))
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import SimpleSync.core

###########################
# Main
###########################
print ("Running basic test...")

parser = argparse.ArgumentParser(description='.')
parser.add_argument('--verbose', '-v', type=bool, default=True, help='Wow much talk.', dest='verbose')

args = parser.parse_args()

myptab = ptab.core.ptabgrab(True)

# insert the tests here.


