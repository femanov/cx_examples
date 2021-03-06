#!/usr/bin/env python

import time
import sys
from PyQt4 import QtCore

from pycx4.qcda import cda
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)

nchans, i = 10000, 0

def printval(chan):
    global i
    i += 1
    if i == 1000000:
        print chan.val
        t2 = time.time()
        print 'time1 = %f ' % (t1-t0)
        print "time = %f " % (t2-t1)
        app.quit()

t0 = time.time()

app = QtCore.QCoreApplication(sys.argv)

context = cda.Context("localhost:1.NAME")
chans = []

for x in range(nchans):
    chans.append(cda.DChan("%d" % x, context))

for x in chans:
    x.valueChanged.connect(printval)

t1 = time.time()

sys.exit(app.exec_())