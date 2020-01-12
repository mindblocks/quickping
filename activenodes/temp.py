
"""
activenodes/activeNodesExec.py
executable python file of activeNodes.py
"""

import sys
import subprocess
import ipaddress
from threading import Thread
from queue import Queue

def next(oldip):

    def gen_next_ip(ip):
        octets = ip.split(".")
        last_octet = octets[-1]
        if last_octet == '254':
            octets[2] = str(int(octets[2]) + 1)
            nextip = '{0}.{1}.{2}.{3}'.format(octets[0],octets[1],octets[2],"0")

        else:
            octets[3] = str(int(octets[3]) + 1)
            nextip = '{0}.{1}.{2}.{3}'.format(octets[0],octets[1],octets[2],octets[3])
        return str(nextip)

    try :
        oldip == str(ipaddress.IPv4Address(oldip))

        out = gen_next_ip(oldip)
        return out
    except:
        print("Your address is not vaild")


if len(sys.argv) == 3:
	start_range = sys.argv[1]
	end_range = sys.argv[2]
	
	print("Please Wait ...")
else:
	print("""Use it like that
~$ python3 livenodes.py 192.168.0.1 192.168.3.254""")
	exit()

address = start_range
iprange = []

while address != end_range:
    address = next(address)
    iprange.append(address)
#iprange = iprange[--:--]
#print(iprange)


LiveNodes = []
#the number of threads set to 512 if you have powerfull computer you can increases
num_threads = 512
queue = Queue()

#wraps system ping command
def pinger(i, q):
	"""Pings subnet"""
	while True:
		ip = q.get()
		#print("Thread {0}: Pinging {1}".format(i, ip))
		ret = subprocess.call("ping -c 1 {0}".format(ip),
		shell=True,
		stdout=open('/dev/null', 'w'),
		stderr=subprocess.STDOUT)
		if ret == 0:
			#print( "There is a Live Node at : {0}".format(ip))
			LiveNodes.append(ip)
		else:
			pass
			#print( "There is no Node Available at {0}".format(ip))
		q.task_done()
#Spawn thread pool
for i in range(num_threads):

    worker = Thread(target=pinger, args=(i, queue))
    worker.setDaemon(True)
    worker.start()
#Place work in queue
for ip in iprange:
    queue.put(ip)
#Wait until worker threads are done to exit
queue.join()
print("\nAll live nodes in Range ({0} -- {1})".format(start_range, end_range))
for node in LiveNodes:
	print(node)
