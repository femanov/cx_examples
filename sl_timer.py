#!/usr/bin/env python3

import pycx4.pycda as cda
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


def print_t():
    print("time out")


t = cda.Timer(1000)
t.start()
t.timeout.connect(print_t)


cda.main_loop()
