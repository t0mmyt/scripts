#!/usr/bin/env python
import sys
import binascii

still_going = True

while still_going:
    a = sys.stdin.read()
    if a == "":
        still_going = False
    sys.stdout.write(binascii.unhexlify(a.replace(':','').replace('\n','')))
