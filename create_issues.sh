#!/bin/bash

### Step 0: 🚀 Prerequisites
# Make sure you have:
#   1.	GitHub CLI installed: https://cli.github.com/
#   2.	Authenticated: Run gh auth login
#	3.	Created your GitHub repo: If not:

# gh repo create signal-processing-roadmap --public --clone
# cd signal-processing-roadmap


### 📜 Step 1: Create Milestones via CLI
gh milestone create "Milestone 1 – Foundations" --description "Weeks 1–3: Signals, Transforms, Sampling"
gh milestone create "Milestone 2 – Filtering" --description "Weeks 4–6: Digital Filters, FFT, Spectrograms"
gh milestone create "Milestone 3 – Real-World Applications" --description "Weeks 7–10: Audio, Speech, Biomedical"
gh milestone create "Milestone 4 – Radar/IoT" --description "Weeks 11–14: Radar, Communication, IoT, Kalman"
gh milestone create "Milestone 5 – Advanced DSP" --description "Weeks 15–16: Financial, Wavelets, ICA, ML"


### ⚙️ Step 2: Create Issues Automatically (Script)

declare -a titles=(
  "Week 01: Signals & Systems"
  "Week 02: Fourier, Z, Laplace (Part 1)"
  "Week 03: Sampling & Aliasing"
  "Week 04: FIR & IIR Filters"
  "Week 05: FFT & STFT"
  "Week 06: Spectrograms & Real-Time Analysis"
  "Week 07: Audio & Speech Basics"
  "Week 08: Audio Transformations & Features"
  "Week 09: ECG/EEG Preprocessing"
  "Week 10: Biomedical Features & Events"
  "Week 11: Radar Signal Basics"
  "Week 12: Communication Signals"
  "Week 13: IoT Sensor Streams & Multirate"
  "Week 14: Kalman Filters in IoT"
  "Week 15: Financial Signals + Kalman"
  "Week 16: Wavelets, ICA & ML + Signals"
)

declare -a bodies=(
"Understand signals, systems, LTI, convolution, impulse/step. Notebook: Week_01_Basics.ipynb"
"Fourier series/transform, Z and Laplace basics. Notebook: Week_02_Transforms.ipynb"
"Sampling theorem, aliasing demos, reconstruction filters. Notebook: Week_03_Sampling.ipynb"
"Filter design, FIR/IIR, scipy.signal. Notebook: Week_04_Filters.ipynb"
"FFT, STFT, signal analyzer. Notebook: Week_05_FFT_STFT.ipynb"
"Spectrograms, real-time audio. Notebook: Week_06_Spectrograms.ipynb"
"Speech waveform, pitch, energy, zero-crossing. Notebook: Week_07_AudioBasics.ipynb"
"MFCC, chroma, pitch shift. Notebook: Week_08_AudioFeatures.ipynb"
"ECG/EEG filters, noise removal. Notebook: Week_09_ECG_EEG.ipynb"
"Extract HRV, EEG bands, features. Notebook: Week_10_BioFeatures.ipynb"
"Radar chirp, range-Doppler, pulse. Notebook: Week_11_Radar.ipynb"
"AM/FM/BPSK modulations. Notebook: Week_12_CommSignals.ipynb"
"IoT data, multirate filters. Notebook: Week_13_IoT_Multirate.ipynb"
"Kalman for smoothing sensor signals. Notebook: Week_14_Kalman_IoT.ipynb"
"Stock data, MA + Kalman smoothing. Notebook: Week_15_Financial.ipynb"
"Wavelet, ICA, ML + signal classification. Notebook: Week_16_Advanced.ipynb"
)

declare -a milestones=(
"Milestone 1 – Foundations"
"Milestone 1 – Foundations"
"Milestone 1 – Foundations"
"Milestone 2 – Filtering"
"Milestone 2 – Filtering"
"Milestone 2 – Filtering"
"Milestone 3 – Real-World Applications"
"Milestone 3 – Real-World Applications"
"Milestone 3 – Real-World Applications"
"Milestone 3 – Real-World Applications"
"Milestone 4 – Radar/IoT"
"Milestone 4 – Radar/IoT"
"Milestone 4 – Radar/IoT"
"Milestone 4 – Radar/IoT"
"Milestone 5 – Advanced DSP"
"Milestone 5 – Advanced DSP"
)

for i in "${!titles[@]}"; do
  gh issue create --title "${titles[$i]}" \
                  --body "${bodies[$i]}" \
                  --milestone "${milestones[$i]}"
done

### ▶️ Step 3: Run the Script
#chmod +x create_issues.sh
#./create_issues.sh

### Optional 📌: Add Labels
gh label create "week-01" --color FAEBD7
gh label create "audio" --color 1E90FF
gh label create "iot" --color 00CED1
gh label create "biomedical" --color 9ACD32