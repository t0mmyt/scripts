#!/usr/bin/env python
from netaddr import *
import sys

iplist = []

try:
    for line in sys.stdin.readlines():
	iplist.append(IPAddress(line))
except:
    print "Something wasn't just an IP address, bombing out"
    sys.exit()

iplist.sort

for ip in sorted(iplist):
    print "%s" % ip
