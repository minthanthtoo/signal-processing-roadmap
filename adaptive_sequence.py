#!/usr/bin/env python3
"""
adaptive_sequence.py
Implements the adaptive progression engine, analyzing progress and recommending
optimized learning paths (Core Pareto -> Domain Branches -> Advanced Deep Dives).
"""
import os
import csv

REPO_ROOT = "/Users/min/projects/mth-signal-processing"
CSV_PATH = os.path.join(REPO_ROOT, "Learning_Tracker_progress.csv")

def main():
    print("🧠 [Adaptive Progression Engine] Analyzing your learning path...")
    
    if not os.path.exists(CSV_PATH):
        print("❌ Error: Learning_Tracker_progress.csv not found in repository root.")
        return
        
    completed_weeks = set()
    pending_weeks = set()
    total_weeks = 0
    
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            week = int(row["Week"])
            total_weeks += 1
            if row["Completed"].strip().lower() == "true":
                completed_weeks.add(week)
            else:
                pending_weeks.add(week)
                
    completion_rate = (len(completed_weeks) / total_weeks) * 100
    
    # Render Progress Bar
    bar_length = 20
    filled_length = int(round(bar_length * len(completed_weeks) / total_weeks))
    bar = "█" * filled_length + "-" * (bar_length - filled_length)
    print(f"\n📊 Overall Progress: |{bar}| {completion_rate:.1f}% ({len(completed_weeks)}/{total_weeks} Weeks)")
    
    print("\n🗺️ Path Evaluation:")
    
    # 1. Check Core Pareto Track (Weeks 1-3)
    core_pareto = {1, 2, 3}
    core_completed = core_pareto.intersection(completed_weeks)
    if len(core_completed) < len(core_pareto):
        missing = sorted(list(core_pareto - completed_weeks))
        print("⚠️  Status: Core Foundations Track INCOMPLETE.")
        print("👉 Recommended Next Action:")
        print(f"   - You must complete Week {missing[0]:02d} before entering specialized branches.")
        return
        
    print("✅ Status: Core Foundations Completed!")
    
    # 2. Offer Domain-Specific Branches
    print("\n🚀 Branch Recommendations:")
    
    audio_weeks = {7, 8}
    biomed_weeks = {9, 10}
    telecom_weeks = {11, 12}
    
    # Evaluate Audio
    audio_done = audio_weeks.intersection(completed_weeks)
    if len(audio_done) == 0:
        print("   🎵 [AUDIO & SPEECH BRANCH]: Ready to start. Begin with Week 07 (Audio Basics).")
    elif len(audio_done) < len(audio_weeks):
        missing = sorted(list(audio_weeks - completed_weeks))
        print(f"   🎵 [AUDIO & SPEECH BRANCH]: In-progress. Next: Week {missing[0]:02d}.")
    else:
        print("   🎵 [AUDIO & SPEECH BRANCH]: Completed!")
        
    # Evaluate Biomedical
    biomed_done = biomed_weeks.intersection(completed_weeks)
    if len(biomed_done) == 0:
        print("   🏥 [BIOMEDICAL BRANCH]: Ready to start. Begin with Week 09 (ECG/EEG).")
    elif len(biomed_done) < len(biomed_weeks):
        missing = sorted(list(biomed_weeks - completed_weeks))
        print(f"   🏥 [BIOMEDICAL BRANCH]: In-progress. Next: Week {missing[0]:02d}.")
    else:
        print("   🏥 [BIOMEDICAL BRANCH]: Completed!")
        
    # Evaluate Telecom
    telecom_done = telecom_weeks.intersection(completed_weeks)
    if len(telecom_done) == 0:
        print("   📡 [TELECOM & RADAR BRANCH]: Ready to start. Begin with Week 11 (Radar FMCW).")
    elif len(telecom_done) < len(telecom_weeks):
        missing = sorted(list(telecom_weeks - completed_weeks))
        print(f"   📡 [TELECOM & RADAR BRANCH]: In-progress. Next: Week {missing[0]:02d}.")
    else:
        print("   📡 [TELECOM & RADAR BRANCH]: Completed!")

    # 3. Check Deep Dives (Weeks 13-16)
    deep_dives = {13, 14, 15, 16}
    deep_done = deep_dives.intersection(completed_weeks)
    if len(completed_weeks) >= 9:  # If student has done foundations and at least one full branch
        print("\n🔬 Advanced Deep Dives (Unlocked):")
        missing_deep = sorted(list(deep_dives - completed_weeks))
        if missing_deep:
            print(f"   - Recommended advanced track: Week {missing_deep[0]:02d}.")
        else:
            print("   - All advanced tracks completed!")
    else:
        print("\n🔒 Advanced Deep Dives (Locked): Complete at least one domain branch to unlock.")

if __name__ == "__main__":
    main()
