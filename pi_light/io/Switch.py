#!/usr/bin/env python

from pi_light.exceptions.SwitchException import SwitchException

__author__ = "Chris Kittl"
__version__ = "0.1"
__license__ = "GPL v 3"
__status__ = "Final"


class Switch:
    """This class represents an electrical switch with attached attributes for use as GPIO input.

    Attributes
        id          Identifier of the switch
        pin_channel Pin at which the switch is connected
        bounce_time Delay for de bouncing the input. Given in ms.
    """
    id = ""
    pin_channel = 0
    bounce_time = 0

    def __init__(self, id_in, pin_channel_in, bounce_time_in):
        """Initialises an instance of the switch.

        Attributes
            id          Identifier of the switch
            pin_channel Pin at which the switch is connected
            bounce_time Delay for de bouncing the input. Given in ms.
        """
        self.id = id_in
        if pin_channel_in > 40:
            raise SwitchException("You may limit to GPIO channel number to 40. You provided " + str(pin_channel_in) +
                                  ".")
        else:
            self.pin_channel = pin_channel_in
        if bounce_time_in < 0:
            raise SwitchException("The bounce time have to be positive. You provided " + str(bounce_time_in) + ".")
        else:
            self.bounce_time = bounce_time_in
