#!/usr/bin/env python

# In case of any issue please contact chandersingh2060@gmail.com
import psutil

# Iterate over all running process

for proc in psutil.process_iter():
    try:
        # Get process name & pid from process object.
        processName = proc.name
        processID = proc.pid
        processMem = float(proc.memory_info().vms) / (1000 * 1000 * 1000 * 1000)
        if float(processMem) > 10 and float(processMem) < 15:
            print(processName)
            exit(1)
        if float(processMem) > 15:
            print(processName)
            exit(2)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
exit(0)
