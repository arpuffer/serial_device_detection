Given a MID and PID, find a match in connected serial device.

Purpose: my previous implementation of this idea was based on the pywin32 lib, and is therefore windows-only.  This is my attempt to create a cross-platform equivalent.

11/28/2019 - working on Win10, and *should* also work on Ubuntu
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

