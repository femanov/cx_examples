#!/usr/bin/env python3
import sys
import os

# since protocol requires
#flags = sys.getdlopenflags()
#sys.setdlopenflags(flags | os.RTLD_GLOBAL)
import pycx4.pycda as cda
#sys.setdlopenflags(flags)

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def printval(chan):
    print(chan.val)

chan1 = cda.Chan("canhw:13.S13_out.Imes")
chan1.valueMeasured.connect(printval)

#cont = cda.Context("")

chan = cda.DChan("EPICS::V5:PA:Current1M") # , context=cont)
chan.valueMeasured.connect(printval)

cda.main_loop()
