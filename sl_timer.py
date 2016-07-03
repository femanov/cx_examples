#!/usr/bin/env python

import pycx4.pycda as cda

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def print_t(timer):
    print("time out")


t = cda.Timer(1000000, 1)
t.shot.connect(print_t)

cda.main_loop()
