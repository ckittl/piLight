#!/usr/bin/env python

"""Main entry point to my pi light project"""

import logging.config

__author__ = "Chris Kittl"
__version__ = "0.1"
__license__ = "GPL v 3"
__status__ = "Under Development"

logging.config.fileConfig('pi_light/resources/logging.conf')
logger = logging.getLogger("piLight")


def run():
    logger.info("Starting pi light")
