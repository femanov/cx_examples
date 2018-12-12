#!/usr/bin/env python3

import pycx4.pycda as cda

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def print_rslv(chan):
    print(chan.name, chan.rslv_str)

def print_val(chan):
    print(chan.name, chan.val, chan.rslv_str)


chan = cda.DChan('canhw:11.QL1.Iset')
chan.resolve.connect(print_rslv)
chan.valueMeasured.connect(print_val)

cda.main_loop()
