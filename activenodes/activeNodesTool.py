
"""
activenodes/activeNodesTool.py
executable python file of activeNodes.py as Terminal Tool
"""

import sys
import re

from activeNodes import ActiveNodes

start = sys.argv[1]
end = sys.argv[2]

if 'log' in sys.argv:
    log = True

for arg in sys.argv:
    if re.search(r'threads:([0-9])\d+', arg):
        threads = arg.split(':')[1]

ant = ActiveNodes(start, end, threads=512, log=log).active()
