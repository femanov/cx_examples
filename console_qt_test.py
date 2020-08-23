#!/usr/bin/env python3
import sys
import signal
from PyQt5 import QtCore
import pycx4.qcda as cda

signal.signal(signal.SIGINT, signal.SIG_DFL)

def printval(chan):
    print(chan.val)

app = QtCore.QCoreApplication(sys.argv)

c = cda.DChan('canhw:13.S13_out.Imes')
c.valueMeasured.connect(printval)

app.exec_()
