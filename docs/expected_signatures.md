# Expected Signal Signatures

This document outlines the types of patterns we expect to search for in GNSS signal data if there is any non-random behavior that stands out beyond noise.

---

## 1. Random Noise vs Structured Anomalies

**Random noise:**
- irregular
- unpredictable
- direction-independent
- no consistent period

**Structured anomalies:**
- periodic or quasi-periodic
- consistent across sessions
- direction-dependent
- survives long-term averaging

If a pattern repeats daily or with Earth’s rotation, that suggests a *directional effect*, not random noise.

---

## 2. Types of Signatures We Aim to Detect

### 2.1 Frequency Band Deviations
Look for:
- narrow peaks not explained by satellite frequency models
- repeatable over multiple days
- stronger in certain directions

Expected in data:


### 2.2 Phase Jitter Patterns
Normal:
- small random jitter
Anomaly:
- rhythmic jitter
- shows correlation with sidereal time

### 2.3 Directional Dependence
If the anomaly changes when the satellite is in a particular azimuth or elevation, that is:
- not explained by atmospheric models
- potentially interesting

To visualize:


---

## 3. Periodicity

A real structured signal will show:
- repeated patterns
- same behavior at similar sidereal times
- symmetry with daily Earth rotation

Random noise will not repeat with Earth’s rotation.

---

## 4. Practical Tips

- Always average over long spans
- Filter out known GNSS artifacts
- Compare with known atmospheric models
- Correlate with satellite orbit and Earth rotation

---

## 5. Terminology

- **Amplitude:** size of deviation
- **Phase:** how the wave shifts
- **Frequency:** how often something repeats
- **Direction:** azimuth / elevation

