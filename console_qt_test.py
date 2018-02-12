#!/usr/bin/env python

import sys
import signal
from PyQt5 import QtCore

from pycx4.qcda import cda

signal.signal(signal.SIGINT, signal.SIG_DFL)


def printval(chan):
    print(chan.val)


app = QtCore.QCoreApplication(sys.argv)


c = cda.DChan('canhw:11.rings.imes')
c.valueMeasured.connect(printval)

app.exec_()