#!/usr/bin/env python3
"""
compile_curriculum.py
Compiles master notebooks from the master/ directory into student-facing exercise notebooks
in the root directory and completed solution notebooks in the solutions/ directory.
Supports comment tags:
  # [SOLUTION_START]
  ...
  # [SOLUTION_END]
And cell metadata:
  "curriculum": "solution"
"""
import os
import json
import glob

REPO_ROOT = "/Users/min/projects/mth-signal-processing"
MASTER_DIR = os.path.join(REPO_ROOT, "master")
SOLUTIONS_DIR = os.path.join(REPO_ROOT, "solutions")

def compile_notebook(master_path):
    filename = os.path.basename(master_path)
    print(f"⚙️ Compiling {filename}...")
    
    # Load master notebook
    with open(master_path, "r", encoding="utf-8") as f:
        nb = json.load(f)
        
    # Create solution version (keep everything intact, clear nothing)
    solution_nb = json.loads(json.dumps(nb))  # Deep copy
    
    # Create student version (strip solutions)
    student_nb = json.loads(json.dumps(nb))  # Deep copy
    
    for cell in student_nb.get("cells", []):
        # 1. Check metadata tags
        metadata = cell.get("metadata", {})
        if metadata.get("curriculum") == "solution":
            if cell.get("cell_type") == "code":
                cell["source"] = ["# TODO: Write your solution here\n"]
                cell["outputs"] = []
                cell["execution_count"] = None
            continue
            
        # 2. Check comment tags in code source
        if cell.get("cell_type") == "code":
            source_lines = cell.get("source", [])
            new_source = []
            in_solution = False
            has_tags = False
            
            for line in source_lines:
                if "[SOLUTION_START]" in line:
                    in_solution = True
                    has_tags = True
                    new_source.append("    # TODO: Write your code here\n")
                    continue
                if "[SOLUTION_END]" in line:
                    in_solution = False
                    continue
                if not in_solution:
                    new_source.append(line)
                    
            if has_tags:
                cell["source"] = new_source
                cell["outputs"] = []
                cell["execution_count"] = None

    # Write student version to root
    student_path = os.path.join(REPO_ROOT, filename)
    with open(student_path, "w", encoding="utf-8") as f:
        json.dump(student_nb, f, indent=1)
        
    # Write solution version to solutions/
    solution_path = os.path.join(SOLUTIONS_DIR, filename)
    with open(solution_path, "w", encoding="utf-8") as f:
        json.dump(solution_nb, f, indent=1)
        
    print(f"   [OK] Compiled student version -> {student_path}")
    print(f"   [OK] Compiled solution version -> {solution_path}")

def main():
    print("🚀 Starting AST Curriculum Compilation...")
    os.makedirs(SOLUTIONS_DIR, exist_ok=True)
    
    master_files = sorted(glob.glob(os.path.join(MASTER_DIR, "*.ipynb")))
    if not master_files:
        print("❌ Error: No master notebooks found in master/")
        return
        
    for master_path in master_files:
        compile_notebook(master_path)
        
    print("✨ Compilation complete!")

if __name__ == "__main__":
    main()
