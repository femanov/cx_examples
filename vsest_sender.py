#!/usr/bin/env python

import signal
import pycx4.pycda as cda

signal.signal(signal.SIGINT, signal.SIG_DFL)

nchans = 50

def printval(chan):
    v = chan.val+1
    chan.setValue(v)
    print 'updating value'

context = cda.cda_context("localhost:2.name")

chans = []

for x in range(nchans):
    chans.append(cda.vchan("%d" % x, context, cda.PY_CXDTYPE_DOUBLE, 1000))
    chans[-1].valueMeasured.connect(printval)


cda.py_sl_main_loop()
