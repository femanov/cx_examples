#!/usr/bin/env python

import pycx4.pycda as cda
import pycx4.scheduler as sl

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def printval(chan):
    print(chan.val)

chan = cda.schan("localhost:1.name.0")
chan.valueMeasured.connect(printval)

sl.main_loop()
