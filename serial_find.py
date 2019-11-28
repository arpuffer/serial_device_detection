from serial.tools import list_ports
from typing import NamedTuple

class TargetDevice():
    vid
    pid

def find_device(vid, pid):
    ser_devices = list_ports()
    # I don't have any USB to serial converters, so I can't tell what info PySerial can actually give on my machines
    # TODO: Get a usb-to-serial converter

