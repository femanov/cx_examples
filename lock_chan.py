#!/usr/bin/env python3

# in order to see locking work run 2 copies of this program

import pycx4.pycda as cda
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


def printval(chan):
    if chan.lock_state:
        print("cur_val=", chan.val)
        print("s val")
        chan.setValue(chan.val - 0.1)


def locked(chan):
    if chan.lock_state:
        print("chan locked, now I can work")
        # initiate some work
        chan.setValue(chan.val - 0.1)


chan1 = cda.Chan("canhw:11.rings.Iset")
chan1.valueMeasured.connect(printval)
chan1.lockStateUpdate.connect(locked)

chan1.lock()  # <- not working

cda.main_loop()
