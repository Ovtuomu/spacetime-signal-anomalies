"""
Parse raw GNSS CSV logs and extract NMEA messages.

This script performs minimal parsing and does not interpret values.
Its purpose is to separate structured NMEA data from raw logs
for later analysis.
"""

import csv
from collections import defaultdict

INPUT_FILE = "data/raw_gnss_log.csv"
OUTPUT_FILE = "data/parsed_nmea.csv"


def parse_nmea():
    message_counts = defaultdict(int)

    with open(INPUT_FILE, "r", encoding="utf-8") as infile, \
         open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as outfile:

        reader = csv.DictReader(infile)
        writer = csv.writer(outfile)

        # Output header
        writer.writerow([
            "unix_time",
            "utc_time",
            "message_type",
            "raw_sentence"
        ])

        for row in reader:
            raw = row["raw_message"]

            if raw.startswith("$"):
                # NMEA sentence
                msg_type = raw.split(",")[0]
                message_counts[msg_type] += 1

                writer.writerow([
                    row["unix_time"],
                    row["utc_time"],
                    msg_type,
                    raw
                ])

    print("Parsing complete.")
    print("Extracted NMEA message counts:")
    for msg, count in message_counts.items():
        print(f"{msg}: {count}")


if __name__ == "__main__":
    parse_nmea()
