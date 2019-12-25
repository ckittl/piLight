#!/usr/bin/env python

"""Handling the GPIO interface for different buttons"""

import pi_light.pi_light as main_module

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  Did you do sudo?")

__author__ = "Chris Kittl"
__version__ = "0.1"
__license__ = "GPL v 3"
__status__ = "Under Development"


def prepare(set_pin, set_bounce_time, reset_pin, reset_bounce_time):
    main_module.logger.debug("Preparing GPIO")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(set_pin, GPIO.IN)
    GPIO.setup(reset_pin, GPIO.IN)
    main_module.logger.info("Setting set pin to %i with bounce time %i ms", set_pin, set_bounce_time)
    GPIO.add_event_detect(set_pin, GPIO.FALLING, callback=main_module.button_pushed, bouncetime=set_bounce_time)
    main_module.logger.info("Setting reset pin to %i with bounce time %i ms", reset_pin, reset_bounce_time)
    GPIO.add_event_detect(reset_pin, GPIO.FALLING, callback=main_module.button_pushed, bouncetime=reset_bounce_time)
    main_module.logger.debug("Ready preparing GPIO")
