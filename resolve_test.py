#!/usr/bin/env python

import pycx4.pycda as cda

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# try to register not existing channel in existing server to
# get "channel unresolved" event.
# if channel unresolved - message will be printed and event will be send
# to user
chan = cda.Chan("ichw1-2:0.pwa1.pa1ccc")


cda.main_loop()
