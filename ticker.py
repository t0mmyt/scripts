#!/usr/bin/python
# -*- coding: latin-1 -*-
import json
import httplib
from threading import Thread

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

# container for threads
thr = {}

# empty objects for threads
btsmp_all = {}
mtgox_all = {}
bitty_all = {}
yahoo_exc = {}

thr['yahoo'] = Thread(target = get_json, args = ('query.yahooapis.com', 443, '/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20(%22GBPUSD%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=', yahoo_exc))
thr['btsmp'] = Thread(target = get_json, args = ('www.bitstamp.net', 443, '/api/ticker/', btsmp_all))
thr['mtgox'] = Thread(target = get_json, args = ('data.mtgox.com', 443, '/api/2/BTCUSD/money/ticker_fast', mtgox_all))
thr['bitty'] = Thread(target = get_json, args = ('bittylicious.com', 443, '/api/v1/quote/BTC/GB/GBP/BANK/1', bitty_all))

# Start all threads
for i in thr.keys():
    thr[i].start()

# Collect all threads
for i in thr.keys():
    thr[i].join()

# Extract the GBPUSD exchange rate
gbpusd = float(yahoo_exc['query']['results']['rate']['Ask'])

# Extract btsmp, bitty and mtgox prices
btsmp = float(btsmp_all['last'])
mtgox = float(mtgox_all['data']['last']['value'])
bitty = float(bitty_all['totalPrice'])

# Pretty print
print "btsmp: $% 7.2f (£% 7.2f) bitty: £% 7.2f mtgox: $% 7.2f" % (btsmp, btsmp/gbpusd, bitty, mtgox)
