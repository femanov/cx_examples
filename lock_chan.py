#!/usr/bin/env python3

import pycx4.pycda as cda
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def printval(chan):
    chan.lock()
    print(chan.val)
    #chan

def locked(chan):
    print('chan locked?', chan.lock_state)

chan = cda.Chan("canhw:11.rings.Iset")
chan.valueMeasured.connect(printval)
chan.lockStateUpdate.connect(locked)



cda.main_loop()
