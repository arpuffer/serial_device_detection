from serial.tools import list_ports
from serial.tools.list_ports_common import ListPortInfo
from typing import NamedTuple, List


def find_devices(vid: int, pid: int) -> List[ListPortInfo]:
    """Return a list of serial devices that match given hardware id parameters
    
    Args:
        vid (int): Vendor ID
        pid (int): Product ID
    
    Returns:
        List[ListPortInfo]
    """
    devices = list_ports.comports()
    return [x for x in devices if all((x.vid==vid, x.pid==pid))]

def main():
    no_devices = find_devices(0, 0)
    trendnet = find_devices(1659, 8963)
    print("No device result: %s" % str(no_devices))
    print("TRENDNet result:  %s" % str(trendnet))

if __name__ == '__main__':
    main()
