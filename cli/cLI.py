
"""
cli/cLI.py
executable python file of quickping as command-line tools
"""

import time
import click
from quickping import Quickping

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-s', '--start', default="", required=True, type=str, help='start range of IPv4 address')
@click.option('-e', '--end', default="", required=True, type=str, help='end range of IPv4 address')
@click.option('-t', '--threads', default=512, type=int, help='number of threads')
@click.option('-l', '--log', default=False, type=bool, help='display logging')
def cLI(start, end, threads, log):

    """
    run python cLI.py --help
    """

    stimer = time.time()
    try:
        testRange = Quickping(start=start, end=end, ignore=[], threads=threads, log=log)
        testRange.active()
    except expression as identifier:
        raise identifier from None
    etimer = time.time()

    click.echo("\nActive Addresses\n")
    for aa in testRange.activeAddresses:
        click.echo(aa)

    # time take to process
    timeToDone = time.strftime("%H:%M:%S", time.gmtime(etimer - stimer))
    click.echo("")
    click.echo("Start @           : {}".format(testRange.start))
    click.echo("End @             : {}".format(testRange.end))
    click.echo("Total Addresses   : {}".format(len(testRange.addresses)))
    click.echo("Active Addresses  : {}".format(len(testRange.activeAddresses)))
    click.echo("Number of Threads : {}".format(testRange.threads))
    click.echo("Time take to Done : {}".format(timeToDone))
    click.echo("")

if __name__ == "__main__":
    cLI()

