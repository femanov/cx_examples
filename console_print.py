#!/usr/bin/env python

import pycx4.pycda as cda


import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def printval(chan):
    print(chan.val)

chan = cda.schan("ichw1-2:0.pwa1.Etoday")
chan.valueMeasured.connect(printval)

cda.main_loop()
