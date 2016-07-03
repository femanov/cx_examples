#!/usr/bin/env python

import signal
import pycx4.pycda as cda

signal.signal(signal.SIGINT, signal.SIG_DFL)


def sendval(chan):
    chan.setValue("hello world!".encode("ascii"))

text_c = cda.strchan("localhost:0.msg.1")
text_c.valueMeasured.connect(sendval)
text_c.setValue("hello world".encode("ascii"))

cda.main_loop()
