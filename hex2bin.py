#!/usr/bin/env python
import sys
import binascii

while True:
    a = sys.stdin.read()
    if a == "":
        break
    sys.stdout.write(binascii.unhexlify(a.replace(':','').replace('\n','')))
