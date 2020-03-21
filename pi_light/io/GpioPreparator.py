#!/usr/bin/env python

"""Handling the GPIO interface for different buttons."""

from pi_light import pi_light as main_module

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  Did you do sudo?")

__author__ = "Chris Kittl"
__version__ = "0.1"
__license__ = "GPL v 3"
__status__ = "Under Development"


def prepare(switch_set):
    """Prepares the Raspberry Pi's GPIO interface by setting up the general settings and switch specific settings

    Attributes
        switch_set  Set of switches that are connected to the GPIO pin
    """
    main_module.logger.debug("Preparing GPIO")
    GPIO.setmode(GPIO.BOARD)
    for switch in switch_set:
        GPIO.setup(switch.pin_channel, GPIO.IN)
        GPIO.add_event_detect(switch.pin_channel, GPIO.FALLING, callback=main_module.button_pushed,
                              bouncetime=switch.bounce_time)
        main_module.logger.info("Setting switch \"%s\" to pin %i with bounce time %i ms", switch.id, switch.pin_channel,
                                switch.bounce_time)
    main_module.logger.debug("Ready preparing GPIO")
