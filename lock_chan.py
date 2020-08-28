#!/usr/bin/env python3

# in order to see locking work run 2 copies of this program


import pycx4.pycda as cda
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


def printval(chan):
    chan.lock()  # here works good
    print(chan.val)
    if chan.lock_state:
        print("setting val")
        chan.setValue(chan.val - 0.1)


def locked(chan):
    if chan.lock_state:
        print("chan locked, now I can work")
        # initiate some work
        chan.setValue(chan.val - 0.1)


chan = cda.Chan("canhw:11.rings.Iset")
chan.valueMeasured.connect(printval)
chan.lockStateUpdate.connect(locked)

#chan.lock() # <- not working here

cda.main_loop()
