## Detect HW by VID and PID
Given a MID and PID, find a match in connected serial device.

Purpose: my previous implementation of this idea was based on the pywin32 lib, and is therefore windows-only.  This is my attempt to create a cross-platform equivalent.



### 11/28/2019 - Testing with TRENDNet TU-S9 plugged in via USB

#### Win10:
```
PS D:\Source\Repos\serial_device_detection> python -m unittest tests.test_find_by_hwid -v
test_TRENDNet_hex (tests.test_find_by_hwid.TestFindByHWID) ... ok
test_TRENDNet_int (tests.test_find_by_hwid.TestFindByHWID) ... ok
test_invalid_args (tests.test_find_by_hwid.TestFindByHWID) ... ok
test_no_results (tests.test_find_by_hwid.TestFindByHWID) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.011s

OK
```
#### Ubuntu 18.04LTS:
```
alex@alex-Spin-SP111-31:~/Source/Repos/serial_device_detection$ python3 -m unittest tests.test_find_by_hwid -v
test_TRENDNet_hex (tests.test_find_by_hwid.TestFindByHWID) ... ok
test_TRENDNet_int (tests.test_find_by_hwid.TestFindByHWID) ... ok
test_invalid_args (tests.test_find_by_hwid.TestFindByHWID) ... ok
test_zero (tests.test_find_by_hwid.TestFindByHWID) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.048s

OK
```
