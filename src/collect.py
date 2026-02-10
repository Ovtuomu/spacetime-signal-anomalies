"""
Collect raw GNSS data from a serial port and store it as CSV.

This script intentionally performs minimal processing.
All interpretation is deferred to later analysis steps.
"""

import serial
import time
import csv
from datetime import datetime

PORT = "COM3"   # change this to your GNSS port
BAUD = 9600
OUTPUT_FILE = "data/raw_gnss_log.csv"


def collect():
    with serial.Serial(PORT, BAUD, timeout=1) as ser:
        with open(OUTPUT_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            # write header if file is empty
            if f.tell() == 0:
                writer.writerow(["unix_time", "utc_time", "raw_message"])

            print("GNSS data collection started. Press Ctrl+C to stop.")

            try:
                while True:
                    line = ser.readline().decode("utf-8", errors="ignore").strip()
                    if line:
                        writer.writerow([
                            time.time(),
                            datetime.utcnow().isoformat(),
                            line
                        ])
                        print(line)

            except KeyboardInterrupt:
                print("\nCollection stopped by user.")


if __name__ == "__main__":
    collect()
