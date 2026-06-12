import sys
import os

class Tutor:
    @classmethod
    def help(cls, exercise_id=None):
        """
        Socratic Tutor helper class. Evaluates the local scope and tracebacks 
        to print guided, Socratic debugging questions.
        """
        print("🧑‍🏫 [Socratic Help Desk] Scanning notebook workspace...")
        
        # 1. Capture local variables from the caller frame
        caller_frame = sys._getframe(1)
        caller_globals = caller_frame.f_globals
        caller_locals = caller_frame.f_locals
        
        # 2. Extract active traceback if an exception just occurred
        traceback_msg = ""
        if hasattr(sys, "last_value"):
            exc_type = getattr(sys, "last_type", Exception).__name__
            exc_val = str(sys.last_value)
            traceback_msg = f"{exc_type}: {exc_val}"
            print(f"⚠️ Detected last runtime error: '{traceback_msg}'")
            
        print("\n🔍 Socratic Guidance:")
        
        # 3. Provide context-dependent hints
        if exercise_id == "week_06_audio":
            cls._guide_week_6(caller_locals, traceback_msg)
        elif exercise_id == "week_09_ecg":
            cls._guide_week_9(caller_locals, traceback_msg)
        elif exercise_id == "week_10_hrv":
            cls._guide_week_10(caller_locals, traceback_msg)
        else:
            cls._guide_generic(caller_locals, traceback_msg)

    @classmethod
    def _guide_week_6(cls, locs, err):
        print("💡 *Topic: Audio Spectrogram & PyAudio Fallbacks*")
        if "pyaudio" not in sys.modules:
            print("- Have you checked if your runtime caught the ImportError gracefully?")
            print("- If pyaudio is missing, what local file fallback does your code fall back to?")
        if "frames" in locs:
            print(f"- Your current animation frames are set to: {locs['frames']}.")
            print("- If this is executing in a headless preprocessor, how does a high frame count affect execution timeouts?")
        else:
            print("- What parameter controls the animation loop limit to prevent headless execution hangs?")

    @classmethod
    def _guide_week_9(cls, locs, err):
        print("💡 *Topic: ECG Biomedical Signal Preprocessing*")
        if "ecg_data" in locs:
            data = locs["ecg_data"]
            print(f"- Detected variables: ecg_data shape = {getattr(data, 'shape', 'unknown')}")
        print("- If the PhysioNet clinical download fails or times out, does your code have a local synthetic generator fallback?")
        print("- When filtering baseline wander, is your highpass cutoff frequency low enough to preserve the ST-segment?")

    @classmethod
    def _guide_week_10(cls, locs, err):
        print("💡 *Topic: Heart Rate Variability & Peak Detection*")
        print("- Are you using SciPy's `find_peaks` to detect the R-peaks?")
        print("- If so, what distance parameter did you specify? (Hint: at a 500Hz sampling rate, how many samples represent a typical physiological refractory period?)")
        if "peaks" in locs:
            print(f"- Detected peaks count: {len(locs['peaks'])}")

    @classmethod
    def _guide_generic(cls, locs, err):
        print("📝 *General Socratic Checklist*")
        print("- 1. Check dimensions: Are your numpy array shapes matching before matrix/signal multiplication?")
        print("- 2. Check sampling rates: Are your time vectors $t$ synchronized with the frequency variables ($f_s$)?")
        print("- 3. Verify variable scoping: Are you accidentally using a global variable inside a local loop?")
        print("\n*To get targeted advice, pass the exercise ID, e.g.: Tutor.help('week_06_audio')*")
