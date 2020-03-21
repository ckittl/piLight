from pi_light.io.Switch import Switch
from pi_light.exceptions.SwitchException import SwitchException
import pytest

__author__ = "Chris Kittl"
__version__ = "0.1"
__license__ = "GPL v 3"
__status__ = "Final"


def test_correct_instantiation():
    switch = Switch("test switch", 1, 1000)
    assert switch.id == "test switch"
    assert switch.pin_channel == 1
    assert switch.bounce_time == 1000


def test_instantiation_with_incorrect_pin_channel():
    with pytest.raises(SwitchException) as ex:
        Switch("test switch", 42, 1000)
    assert ex.value.args[0] == "You may limit to GPIO channel number to 40. You provided 42."


def test_instantiation_with_incorrect_bounce_time():
    with pytest.raises(SwitchException) as ex:
        Switch("test switch", 1, -10)
        print(ex.value)
    assert ex.value.args[0] == "The bounce time have to be positive. You provided -10."
