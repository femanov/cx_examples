#!/usr/bin/env python
import signal
import pycx4.pycda as cda

signal.signal(signal.SIGINT, signal.SIG_DFL)


def printval(chan):
    print chan.val


text_c = cda.strchan("localhost:0.msg.1")
text_c.valueMeasured.connect(printval)

cda.main_loop()
