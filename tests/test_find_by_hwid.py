import unittest
from serial_find import serial_find as ser

class TestFindByHWID(unittest.TestCase):
    """Tests for the find_by_hwid function.  Note: the TRENDNet hardware is required to be plugged in to run this test
       TODO: create mock objects to run test without hardware dependency
    """

    def test_zero(self):
        found_devices = ser.find_by_hwid(vid=0, pid=0)
        self.assertListEqual(found_devices, [])

    def test_TRENDNet_int(self):
        TRENDNet_vid = 1659
        TRENDNet_pid = 8963
        found_devices = ser.find_by_hwid(vid=TRENDNet_vid, pid=TRENDNet_vid)
        for device in found_devices:
            self.assertEqual(device.vid, TRENDNet_vid)
            self.assertEqual(device.pid, TRENDNet_pid)
    
    def test_TRENDNet_hex(self):
        TRENDNet_vid = 1659
        TRENDNet_pid = 8963
        TRENDNet_vid_hex = hex(1659)[2:]
        TRENDNet_pid_hex = hex(8963)[2:]
        found_devices = ser.find_by_hwid(vid=TRENDNet_vid_hex, pid=TRENDNet_pid_hex)
        for device in found_devices:
            self.assertEqual(device.vid, TRENDNet_vid)
            self.assertEqual(device.pid, TRENDNet_pid)

    def test_invalid_args(self):
        with self.assertRaises(ValueError):
            ser.find_by_hwid(vid='Foo', pid='Bar')

if __name__ == '__main__':
    unittest.main()
