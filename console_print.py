#!/usr/bin/env python3
import pycx4.pycda as cda
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def printval(chan):
    print(chan.val)

chan = cda.Chan("ring_current")
chan.valueMeasured.connect(printval)

cda.main_loop()
