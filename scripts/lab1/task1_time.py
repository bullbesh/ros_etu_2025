#!/usr/bin/env python3

import time
from datetime import datetime

while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\rCurrent time: {current_time}")
        time.sleep(5)
