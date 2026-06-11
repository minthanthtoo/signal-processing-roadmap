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
  "Week 01: Basics: Signals & Systems"
  "Week 02: Sampling & Aliasing"
  "Week 03: Fourier Series & DFT"
  "Week 04: FIR & IIR Filters"
  "Week 05: FFT & STFT"
  "Week 06: Spectrograms & Windowing"
  "Week 07: Audio & Speech Basics"
  "Week 08: Audio Denoising & Music Features"
  "Week 09: ECG & EEG Preprocessing"
  "Week 10: ML + Biomedical & Anomaly Detection"
  "Week 11: Radar Signal Processing"
  "Week 12: Modulation & Demodulation"
  "Week 13: IoT Sensor Streams & Multirate"
  "Week 14: Embedded DSP & Hardware Constraints"
  "Week 15: Financial Time Series & Kalman Filtering"
  "Week 16: Wavelets, ICA & Machine Learning"
)

declare -a bodies=(
  "Understand signals, systems, LTI, convolution, impulse/step. Notebook: Week_01_Signals_And_Systems.ipynb"
  "Sampling theorem, Nyquist rate, aliasing, reconstruction filters. Notebook: Week_02_Sampling_And_Aliasing.ipynb"
  "Fourier series harmonics, Discrete Fourier Transform (DFT), Fast Fourier Transform (FFT). Notebook: Week_03_Fourier_Series_and_DFT.ipynb"
  "Filter design, FIR/IIR low-pass and high-pass filters, scipy.signal. Notebook: Week_04_Filters.ipynb"
  "Comparing FFT efficiency, Short-Time Fourier Transform (STFT) for non-stationary signals. Notebook: Week_05_FFT_STFT.ipynb"
  "Spectrograms, windowing techniques (Hann/Hamming), real-time audio analysis. Notebook: Week_06_Spectrograms.ipynb"
  "Digital audio, zero-crossing rate (ZCR), Short-Time RMS Energy, VAD project. Notebook: Week_07_Audio_Speech.ipynb"
  "Mel-Frequency Cepstral Coefficients (MFCCs), Chroma features, audio transformations. Notebook: Week_08_Audio_Denoising.ipynb"
  "Biomedical signals, simulated heartbeat ECG, filtering baseline wander, isolation of EEG brainwaves. Notebook: Week_09_Biomedical.ipynb"
  "Heart Rate Variability (HRV) feature extraction, Random Forest classification, Isolation Forest anomalies. Notebook: Week_10_ML_Biomedical.ipynb"
  "FMCW radar, linear chirps, range-Doppler map, 2D FFT. Notebook: Week_11_Radar_Communication.ipynb"
  "AM, FM, BPSK, 16-QAM modulation/demodulation, constellation diagrams. Notebook: Week_12_Modulation.ipynb"
  "IoT data cleaning, downsampling (decimation), upsampling (interpolation), sensor rate alignment. Notebook: Week_13_IoT_Multirate.ipynb"
  "Fixed-point representation, coefficient quantization, circular buffer for streaming DSP. Notebook: Week_14_Embedded_DSP.ipynb"
  "SMA/EMA tracking lag, state-space models, 1D Kalman filter from scratch, backtesting crossovers. Notebook: Week_15_Financial_Kalman.ipynb"
  "Continuous Wavelet Transform (CWT), Independent Component Analysis (ICA) Cocktail Party Problem, ML classification pipeline. Notebook: Week_16_Wavelets_ICA_ML.ipynb"
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