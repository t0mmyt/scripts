#!/usr/bin/python
import json
import httplib

def get_json(host, port, path, result):
    '''
    To to pull HTTP JSON data in to specified dict.
    Why not just return the dict? This way it can be used as a thread
    (i.e. async).
    '''
    conn = httplib.HTTPSConnection(host, port)
    conn.request('GET', path)
    resp = conn.getresponse()
    if resp.status != 200:
        raise RuntimeError("HTTP Error: " + str(resp.status))
    result.update(json.loads(resp.read()))

btsmp = {}
mtgox = {}

get_json('www.bitstamp.net', 443, '/api/ticker/', btsmp)
get_json('data.mtgox.com', 443, '/api/2/BTCUSD/money/ticker_fast', mtgox)
print "btsmp:% 7.2f  mtgox:% 7.2f" % (float(btsmp['last']), float(mtgox['data']['last']['value']))
