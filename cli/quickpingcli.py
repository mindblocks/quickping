
"""
activenodes/activeNodesTool.py
executable python file of activeNodes.py as Terminal Tool
"""

import sys
import re

from quickping import Quickping

log = True if 'log' in sys.argv else False

ipre = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
for arg in sys.argv:
    if re.search(r'threads:([0-9])\d+', arg):
        threads = int(arg.split(':')[1])

    if re.search(ipre + r':' + ipre, arg):
        start, end = arg.split(':')

try:
    ant = Quickping(start, end, threads=threads, log=log)
    print('\nActive Node : {0}\n'.format(ant.active()))
except expression as identifier:
    raise identifier from None
