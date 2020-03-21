#!/usr/bin/env python

"""Main entry point to my pi light project"""

import logging.config
import time
import datetime
import pi_light.io.GpioPreparator as Button
from pi_light.io.Switch import Switch

__author__ = "Chris Kittl"
__version__ = "0.1"
__license__ = "GPL v 3"
__status__ = "Under Development"

logging.config.fileConfig('pi_light/resources/logging.conf')
logger = logging.getLogger("piLight")

# Global variables
set_switch = Switch("set", 11, 10000)
reset_switch = Switch("reset", 13, 1000)


def run():
    logger.info("Starting pi light")
    Button.prepare({set_switch, reset_switch})
    while True:
        logger.debug("It's %s, waiting another second", datetime.datetime.now())
        time.sleep(1)


def button_pushed(channel):
    if channel == set_switch.pin_channel:
        logger.info("Set button has been pushed")
    if channel == reset_switch.pin_channel:
        logger.info("Reset button has been pushed")
