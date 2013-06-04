#!/usr/bin/env python
from netaddr import *
import sys

iplist = []

for line in sys.stdin.readlines():
    iplist.append(IPAddress(line))

iplist.sort

for ip in sorted(iplist):
    print "%s" % ip
