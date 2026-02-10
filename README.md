# spacetime-signal-anomalies
Exploring subtle, repeatable anomalies in GNSS signals through long-term time and phase analysis.
# spacetime-signal-anomalies

### Listening carefully to what GNSS signals might be telling us

This project explores a simple but rarely asked question:

**Do high-precision GNSS (GPS) signals behave exactly as we expect them to — all the time?**

Rather than assuming new physics or extraordinary explanations, this repository documents a careful, open-ended attempt to look for **subtle, repeatable irregularities** in real GNSS signals using long-term time and phase analysis.

---

## Why this project exists

Modern GNSS systems rely on atomic clocks and extremely precise signal timing.
Because of this precision, GNSS signals are not only navigation tools — they are also sensitive probes of space, time, and signal propagation.

Most applications focus on *accuracy*.
This project focuses on **behavior**.

Specifically:
- Are there tiny deviations that persist over time?
- Do some effects correlate with direction in the sky?
- Are there weak periodic patterns that survive long-term averaging?

These questions are rarely explored outside large institutions — not because they are impossible, but because they require patience rather than scale.

---

## What this project is (and is not)

### What it *is*
- An exploratory, measurement-driven project
- Focused on raw GNSS time, phase, and frequency behavior
- Interested in **repeatable anomalies**, not one-off glitches
- Designed to be open, minimal, and reproducible

### What it *is not*
- ❌ It does not claim the discovery of wormholes
- ❌ It does not claim new physics
- ❌ It does not assume any exotic explanation in advance

Any irregularity observed here is treated strictly as an **anomaly** — a pattern that deserves explanation, not a conclusion.

Names come last.  
Data comes first.

---

## Core idea

If space-time and signal propagation behave exactly as modeled, then:

- Noise should be random
- Phase jitter should average out
- Directional effects should cancel over time

If they do not, we might observe:
- Weak but persistent periodic patterns
- Direction-dependent behavior
- Correlations tied to Earth’s rotation or orientation

This project exists to **look carefully**, not to prove anything prematurely.

---

## Approach

The methodology is intentionally simple:

1. Collect raw GNSS data from a fixed location
2. Observe signals over long time spans
3. Analyze time, phase, and frequency stability
4. Search for structured, non-random behavior
5. Document everything openly

Complexity is added only when necessary.

---

## Reproducibility and openness

This repository is meant to be:
- Transparent
- Reproducible
- Open to scrutiny

Anyone with compatible GNSS hardware should be able to:
- Collect similar data
- Run the same analysis
- Compare results independently

Independent verification is not just welcome — it is encouraged.

---

## Project status

🟡 Early stage / exploratory

- Hardware: single GNSS receiver
- Data collection: in progress
- Analysis: iterative and evolving

This repository will grow as measurements accumulate.

---

## Philosophy

> Extraordinary claims require extraordinary evidence.  
> Careful observation requires only patience and honesty.

This project chooses the second path.

---

## License

MIT License — use, test, question, and improve freely.

## A personal note

This project began as an individual attempt to slow down and look more carefully at the world.

Like many people, I often found myself asking questions that were difficult to articulate — questions about structure, order, and whether everything we observe truly exhausts what is happening around us. Rather than trying to answer those questions philosophically, this project chooses a practical path: measurement.

GNSS signals offer a rare opportunity to work with real, high-precision data that continuously interacts with space and time itself. Exploring these signals is not about chasing extraordinary conclusions, but about regaining a sense of clarity through careful observation.

This repository is, in that sense, both a technical experiment and a personal discipline:  
to measure before naming,  
to observe before concluding,  
and to stay honest about uncertainty.

## How to run

This project is designed to be simple to set up and run.

### 1. Requirements
Make sure you have Python 3.9+ installed.

### Install dependencies:
```bash
pip install -r requirements.txt
Connect GNSS device

### Connect your GNSS/GPS receiver via USB or serial

Note the serial port name:

Windows: COM3, COM4, ...

Linux: /dev/ttyUSB0

macOS: /dev/tty.usbserial-*

ollect raw GNSS data

Edit the serial port in src/collect.py if needed, then run:

python src/collect.py

This will:

read raw GNSS messages

store them in data/raw_gnss_log.csv

run continuously until stopped with Ctrl + C

### Parse NMEA messages

After collecting data, extract NMEA sentences:

python src/parse.py

This will generate:

data/parsed_nmea.csv

5. Analysis (next step)

Analysis scripts will be added incrementally.
The current focus is on clean data collection and parsing.
