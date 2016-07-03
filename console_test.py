#!/usr/bin/env python

import time
import signal
import pycx4.pycda as cda

signal.signal(signal.SIGINT, signal.SIG_DFL)


nchans = 10000
i = 0

def printval(chan):
    global i
    i += 1
    if i == 10000000:
        print(chan.val)
        t2 = time.time()
        print('time1 = %f ' % (t1-t0))
        print("time2 = %f " % (t2-t1))
        cda.break_()

t0 = time.time()

context = cda.Context("localhost:1.NAME")

chans = []

for x in range(nchans):
    chans.append(cda.DChan("%d" % x, context))

for x in chans:
    x.valueChanged.connect(printval)

t1 = time.time()

cda.main_loop()
