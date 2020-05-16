
"""
cli/cLI.py
executable python file of quickping as command-line tools
"""

import click
from quickping import Quickping

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-s', '--start', default="", required=True, type=str, help='start range of IPv4 address')
@click.option('-e', '--end', default="", required=True, type=str, help='end range of IPv4 address')
@click.option('-t', '--threads', default=512, type=int, help='number of threads')
@click.option('-l', '--log', default=False, type=bool, help='display logging')
def cLI(start, end, threads, log):
    
    try:
        testRange = Quickping(start=start, end=end, ignore=[], threads=threads, log=log)
        testRange.active()
    except expression as identifier:
        raise identifier from None

    print('\nActive Addresses\n')
    for aa in testRange.activeAddresses:
        print(aa)

    informations = """\nStart at : {}\nEnd at : {}\nTotal Addresses : {}\nActive Addresses : {}\nNumber of Threads : {}""".format(
        testRange.start,
        testRange.end,
        len(testRange.addresses),
        len(testRange.activeAddresses),
        testRange.threads)
    click.echo(informations)

if __name__ == "__main__":
    cLI()

