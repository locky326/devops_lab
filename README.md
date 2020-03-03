# **DevOps Lab 2019 (September-December)**
## Python
### *Task 3*

***

## "Snapshot" application description
This python application makes snapshot of the system information:

1. Output is written to the plain `text` or `json` file.

2. It creates snapshots of the state of the system each 300 seconds (5 minutes) by default with:

- Overall CPU load
- Overall disk memory usage
- Overall virtual memory usage
- Disk I/O information
- Network I/O information
***
# Usage:

  Type "snapshot" in the command prompt
  >(notice, that results file will be created in current directory).

You can change frequency of snapshot making, and export file type in the command prompt. Only `json` and `txt` can be chosen. Default settings is `txt` and `300 sec` (5min).

***
# Installing/uninstalling:

  Before using this application please install `psutil` with `pip` (pip install psutil). Python version `3.6` requaried.

Created a distributive package of the script (to make wheel from source files):
`python3 setup.py bdist_wheel --universal`

Package has to be located in the parent directory.

`pip install snapshot-1.0-py3-none-any.whl`
***
# Examples of use:
> `snapshot` - frequency is 300 sec, file-format `txt`

> `snapshot 10 json` - frequency is 10 sec, file-format `json`

> `snapshot 600 txt` - Runs system monitoring with 600 sec interval, snapshots file-format: `txt`
