#!/usr/bin/env python

"""Main entry point to my pi light project"""

import logging.config
import time
import datetime
import pi_light.io.Button as Button

__author__ = "Chris Kittl"
__version__ = "0.1"
__license__ = "GPL v 3"
__status__ = "Under Development"

logging.config.fileConfig('pi_light/resources/logging.conf')
logger = logging.getLogger("piLight")

# Global variables
set_pin = 11
set_bounce_time = 10000  # bounce time for set pin (10s)
reset_pin = 13
reset_bounce_time = 1000  # bounce time for set pin (1s)


def run():
    logger.info("Starting pi light")
    Button.prepare(set_pin, set_bounce_time, reset_pin, reset_bounce_time)
    while True:
        logger.debug("It's %s, waiting another second", datetime.datetime.now())
        time.sleep(1)


def button_pushed(channel):
    if channel == set_pin:
        logger.info("Set button has been pushed")
    if channel == reset_pin:
        logger.info("Reset button has been pushed")
