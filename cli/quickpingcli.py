
"""
cli/quickpingcli.py
executable python file of quickping as Terminal Tool
"""

import re
import sys

from quickping import Quickping

log = True if 'log' in sys.argv else False

ipre = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
for arg in sys.argv:
    if re.search(r'threads:([0-9])\d+', arg):
        threads = int(arg.split(':')[1])

    if re.search(ipre + r':' + ipre, arg):
        start, end = arg.split(':')

try:
    testRange = Quickping(start, end, threads=threads, log=log)
    testRange.active()
except expression as identifier:
    raise identifier from None

print('\nActive Addresses\n')
for aa in testRange.activeAddresses:
    print(aa)

informations = """
Start at : {}
End at : {}
Total Addresses : {}
Active Addresses : {}
Number of Threads : {}
""".format(
        testRange.start,
        testRange.end,
        len(testRange.addresses),
        len(testRange.activeAddresses),
        testRange.threads
        )

if __name__ == "__main__":
    print(informations)

