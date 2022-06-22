#!/usr/bin/env python3

import pycx4.pycda as cda

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def printval(chan):
    print(chan.val)
    #print(chan.aval)

chan = cda.VChan('canhw:23.ipp_gw1.box9.data', max_nelems=9, dtype=cda.DTYPE_INT32)
chan.valueMeasured.connect(printval)

cda.main_loop()