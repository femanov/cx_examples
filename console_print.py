#!/usr/bin/env python

import pycx4.pycda as cda


import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def printval(chan):
    print(chan.val)

chan = cda.Chan("linac1:11.rst1.GUN_V.Imes")
chan.valueMeasured.connect(printval)

cda.main_loop()
