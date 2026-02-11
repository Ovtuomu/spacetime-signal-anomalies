import csv
import time
import matplotlib.pyplot as plt
from collections import defaultdict, deque

FILE = "data/parsed_nmea.csv"

WINDOW = 100

snr_history = defaultdict(lambda: deque(maxlen=WINDOW))
time_history = deque(maxlen=WINDOW)

plt.ion()
fig, ax = plt.subplots()

while True:
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        if not rows:
            time.sleep(1)
            continue

        last = rows[-1]
        t = float(last["unix_time"])
        msg = last["raw_sentence"]

        if msg.startswith("$GPGSV"):
            parts = msg.split(",")

            for i in [7, 11, 15, 19]:
                if i < len(parts) and parts[i].isdigit():
                    snr = int(parts[i])
                    sat_id = f"SAT_{i}"
                    snr_history[sat_id].append(snr)

            time_history.append(t)

            ax.clear()
            for sat, values in snr_history.items():
                ax.plot(list(values), label=sat)

            ax.set_title("Live GNSS SNR")
            ax.set_ylabel("SNR (dB-Hz)")
            ax.set_xlabel("Samples")
            ax.legend(loc="upper right")

            plt.pause(0.5)

    except FileNotFoundError:
        print("Waiting for parsed_nmea.csv ...")
        time.sleep(2)
