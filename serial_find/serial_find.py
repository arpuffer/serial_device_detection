from serial.tools import list_ports
from serial.tools.list_ports_common import ListPortInfo
from typing import NamedTuple, List, Union


def find_by_hwid(vid: Union[int, str], pid: Union[int, str]) -> List[ListPortInfo]:
    """Return a list of serial devices that match given hardware id parameters
    
    Args:
        vid (int, str): Vendor ID - also accepts hex
        pid (int, str): Product ID - also accepts hex string
    
    Returns:
        List[ListPortInfo]
    """
    try:
        vid = int(vid)
    except ValueError:
        vid = int(vid, 16)
    try:
        pid = int(pid)
    except ValueError:
        pid = int(pid, 16)
    devices = list_ports.comports()
    return [x for x in devices if all((x.vid==vid, x.pid==pid))]
