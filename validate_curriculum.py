#!/usr/bin/env python3
"""
validate_curriculum.py
Verifies curriculum metadata consistency across the README, progress CSV,
issue creator script, and notebooks in the repository root.
"""
import os
import re
import csv
import json
import sys

REPO_ROOT = "/Users/min/projects/mth-signal-processing"

def main():
    print("🔬 Running Curriculum Metadata Validator...")
    errors = []

    # 1. Expected filenames mapping
    expected_notebooks = {
        1: "Week_01_Signals_And_Systems.ipynb",
        2: "Week_02_Sampling_And_Aliasing.ipynb",
        3: "Week_03_Fourier_Series_and_DFT.ipynb",
        4: "Week_04_Filters.ipynb",
        5: "Week_05_FFT_STFT.ipynb",
        6: "Week_06_Spectrograms.ipynb",
        7: "Week_07_Audio_Speech.ipynb",
        8: "Week_08_Audio_Denoising.ipynb",
        9: "Week_09_Biomedical.ipynb",
        10: "Week_10_ML_Biomedical.ipynb",
        11: "Week_11_Radar_Communication.ipynb",
        12: "Week_12_Modulation.ipynb",
        13: "Week_13_IoT_Multirate.ipynb",
        14: "Week_14_Embedded_DSP.ipynb",
        15: "Week_15_Financial_Kalman.ipynb",
        16: "Week_16_Wavelets_ICA_ML.ipynb",
    }

    # Verify files exist in filesystem
    print("-> Checking physical notebook existence...")
    for week, filename in expected_notebooks.items():
        path = os.path.join(REPO_ROOT, filename)
        if not os.path.exists(path):
            errors.append(f"Missing notebook file in repository: {filename}")
        else:
            print(f"   [OK] {filename} exists")

    # 2. Check CSV database
    csv_path = os.path.join(REPO_ROOT, "Learning_Tracker_progress.csv")
    print("\n-> Checking progress tracker CSV consistency...")
    if not os.path.exists(csv_path):
        errors.append("Missing Learning_Tracker_progress.csv file")
    else:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            if len(rows) != 16:
                errors.append(f"CSV tracker must contain exactly 16 rows, found {len(rows)}")
            for idx, row in enumerate(rows):
                week_num = idx + 1
                csv_week = int(row["Week"])
                if csv_week != week_num:
                    errors.append(f"CSV row index {idx} specifies Week {csv_week}, expected {week_num}")
                print(f"   [OK] CSV Week {csv_week} maps to topic: '{row['Topic']}'")

    # 3. Check README.md Colab/Binder links
    readme_path = os.path.join(REPO_ROOT, "README.md")
    print("\n-> Checking README.md hyperlinks...")
    if not os.path.exists(readme_path):
        errors.append("Missing README.md file")
    else:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
            
            # Check Colab link filenames
            colab_links = re.findall(r"colab\.research\.google\.com/github/[^/]+/[^/]+/blob/main/([A-Za-z0-9_]+\.ipynb)", content)
            binder_links = re.findall(r"mybinder\.org/v2/gh/[^/]+/[^/]+/HEAD\?filepath=([A-Za-z0-9_]+\.ipynb)", content)
            
            # Colab link verification
            if len(colab_links) != 16:
                errors.append(f"README.md contains {len(colab_links)} Colab links instead of 16")
            else:
                for idx, link_file in enumerate(colab_links):
                    expected = expected_notebooks[idx + 1]
                    if link_file != expected:
                        errors.append(f"README Colab link {idx + 1} points to {link_file}, expected {expected}")
            
            # Binder link verification
            if len(binder_links) != 16:
                errors.append(f"README.md contains {len(binder_links)} Binder links instead of 16")
            else:
                for idx, link_file in enumerate(binder_links):
                    expected = expected_notebooks[idx + 1]
                    if link_file != expected:
                        errors.append(f"README Binder link {idx + 1} points to {link_file}, expected {expected}")

    # 4. Check create_issues.sh arrays
    issues_path = os.path.join(REPO_ROOT, "create_issues.sh")
    print("\n-> Checking GitHub issues script arrays...")
    if not os.path.exists(issues_path):
        errors.append("Missing create_issues.sh script")
    else:
        with open(issues_path, "r", encoding="utf-8") as f:
            script_content = f.read()
            
            # Parse titles array
            titles_match = re.search(r"declare -a titles=\(\s*(.*?)\n\)", script_content, re.DOTALL)
            if not titles_match:
                errors.append("Could not find titles array in create_issues.sh")
            else:
                raw_titles = re.findall(r'"([^"]+)"', titles_match.group(1))
                if len(raw_titles) != 16:
                    errors.append(f"create_issues.sh has {len(raw_titles)} titles instead of 16")
                else:
                    for idx, title in enumerate(raw_titles):
                        week_str = f"Week {idx+1:02d}:"
                        if not title.startswith(week_str):
                            errors.append(f"create_issues.sh title {idx+1} '{title}' does not match prefix '{week_str}'")

            # Parse bodies array
            bodies_match = re.search(r"declare -a bodies=\(\s*(.*?)\n\)", script_content, re.DOTALL)
            if not bodies_match:
                errors.append("Could not find bodies array in create_issues.sh")
            else:
                raw_bodies = re.findall(r'"([^"]+)"', bodies_match.group(1))
                if len(raw_bodies) != 16:
                    errors.append(f"create_issues.sh has {len(raw_bodies)} bodies instead of 16")
                else:
                    for idx, body in enumerate(raw_bodies):
                        expected = expected_notebooks[idx + 1]
                        if expected not in body:
                            errors.append(f"create_issues.sh body {idx+1} is missing reference to notebook: '{expected}'")

    print("\n-------------------------------------------")
    if errors:
        print("❌ CURRICULUM SYNC VALIDATION FAILED:")
        for err in errors:
            print(f"   - {err}")
        sys.exit(1)
    else:
        print("✨ SUCCESS: All metadata links, CSV records, scripts, and notebook files are perfectly in sync!")
        sys.exit(0)

if __name__ == "__main__":
    main()
