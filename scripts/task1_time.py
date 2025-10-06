#!/usr/bin/env python3

import time
from datetime import datetime

def display_current_time():
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\rCurrent time: {current_time}", end="", flush=True)
        time.sleep(5)

if name == "main":
    display_current_time()