
"""
quickping/quickping.py
Python3 package for find active addresses for IPv4 in range of IP address
"""

import sys
import time
import subprocess
import ipaddress
from threading import Thread
from queue import Queue

from .error import AddressRangeError
from .color import colorize

class Quickping:
    def __init__(self, start, end, threads=512, log=False):

        self.start = start
        self.end = end
        self.threads = threads
        self.log = log
        self.logs = []
        self.addresses = []
        self.activeAddresses = []
        self.deactiveAddresses = []

        try:
            ipaddress.IPv4Address(start)
            ipaddress.IPv4Address(end)
        except ValueError as e:
            raise e

        if ipaddress.ip_address(self.start) > ipaddress.ip_address(self.end):
            raise AddressRangeError("Start and end address are not same range")

    def __repr__(self):
        return "Quickping('{0}', '{1}', {2})".format(self.start, self.end, self.threads)

    def genAddresses(self):

        """
        collect IPv4 addresses
        """
        
        self.addresses.clear()

        #start from first address 
        address = self.start
        while address != self.end:
            #print(address)
            address = str(ipaddress.ip_address(address) + 1)
            self.addresses.append(address)

        return self.addresses
    
    def pinger(self, thread, queue):
        
        """
        Pings subnet
        """

        self.logs.clear()
        
        while True:
            address = queue.get()

            if self.log:
                log = "{0} Thread <{1}> Pinging : {2}".format(time.ctime(), 
                        colorize(thread, fg="cyan"),
                        colorize(address, fg="cyan"))
                self.logs.append(log)
                print(log)

            ret = subprocess.call("ping -c 1 {0}".format(address),
            shell=True,
            stdout=open('/dev/null', 'w'),
            stderr=subprocess.STDOUT)
            if ret == 0:
                if self.log:
                    log = "{0} Active Address at : {1}".format(time.ctime(), colorize(address, fg="green"))
                    self.logs.append(log)
                    print(log)
                self.activeAddresses.append(address)
            else:
                if self.log:
                    log = "{0} Deactive Address at : {1}".format(time.ctime(), colorize(address, fg="red"))
                    self.logs.append(log)
                    print(log)
                self.deactiveAddresses.append(address)
            queue.task_done()

    def active(self):

        """
        return self.activeAddresses, self.deactiveAddresses
        """

        self.genAddresses()
        queue = Queue()

        for thread in range(self.threads):
            worker = Thread(target=self.pinger, args=(thread, queue))
            worker.setDaemon(True)
            worker.start()

        for address in self.addresses:
            queue.put(address)
        queue.join()

        #remove duplicates addresses and sort them
        self.activeAddresses = list(dict.fromkeys(sorted(self.activeAddresses)))
        self.deactiveAddresses = list(dict.fromkeys(sorted(self.deactiveAddresses)))

        #ratio add after this function run
        self.ratio = {
            "addresses": len(self.addresses),
            "active": len(self.activeAddresses),
            "deactive": len(self.deactiveAddresses)
        }
        
        return self.activeAddresses

    def deactive(self):
        self.active()
        return self.deactiveAddresses

