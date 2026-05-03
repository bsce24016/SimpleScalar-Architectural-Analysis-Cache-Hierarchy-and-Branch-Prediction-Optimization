import subprocess
import os

# --- 1. CONFIGURATION & PATHS ---
SIM_EXE = "./sim-outorder"
BENCHMARK = "ijpeg.ss"
WORKLOAD = "vgrind.ppm"
MAX_INST = "1000000"
RESULTS_DIR = "results"

# Ensure directories exist
os.makedirs(f"{RESULTS_DIR}/task1_cache", exist_ok=True)
os.makedirs(f"{RESULTS_DIR}/task2_bpred", exist_ok=True)

def run_simulation(args, output_filename):
    """Executes the simulator and redirects output to a text file."""
    print(f"🚀 Starting Simulation: {output_filename}...")
    
    # Construct command: sim + flags + workload
    full_cmd = [SIM_EXE, "-max:inst", MAX_INST] + args + [BENCHMARK, WORKLOAD]
    
    try:
        with open(output_filename, "w") as f:
            # SimpleScalar outputs stats to stderr, so we redirect it to our file
            subprocess.run(full_cmd, stdout=f, stderr=subprocess.STDOUT, check=True)
        
        # Immediate Validation
        verify_success(output_filename)
    except Exception as e:
        print(f"❌ Error running {output_filename}: {e}")

def verify_success(filename):
    """Checks if the simulation actually reached the 1M instruction target."""
    with open(filename, "r") as f:
        content = f.read()
        if "sim_num_insn" in content:
            # Extract number from line: 'sim_num_insn             1000000'
            line = [l for l in content.split('\n') if "sim_num_insn" in l][0]
            count = int(line.split()[1])
            if count >= int(MAX_INST):
                print(f"✅ Success: {count} instructions processed.")
            else:
                print(f"⚠️ Warning: Only {count} instructions. Check workload files!")

# --- 2. EXPERIMENT DEFINITIONS ---

# TASK 1: Cache Configurations (Example: Small vs Large)
cache_configs = [
    {
        "name": "cache_small",
        "flags": ["-cache:dl1", "dl1:128:32:1:l", "-cache:il1", "none", "-cache:dl2", "none"]
    },
    {
        "name": "cache_large",
        "flags": ["-cache:dl1", "dl1:512:32:4:l", "-cache:il1", "il1:512:32:4:l", "-cache:dl2", "ul2:2048:64:4:l"]
    }
]

# TASK 2: BTB Sensitivity (Example: Conflict Analysis)
btb_configs = [
    {
        "name": "btb_256x1_direct", # 256 sets, 1-way (Total 256)
        "flags": ["-bpred", "bimod", "-bpred:btb", "256", "1"]
    },
    {
        "name": "btb_64x4_assoc",   # 64 sets, 4-way (Total 256)
        "flags": ["-bpred", "bimod", "-bpred:btb", "64", "4"]
    }
]

# --- 3. EXECUTION LOOP ---

if __name__ == "__main__":
    print("--- Starting Architecture Simulation Suite ---")
    
    # Run Cache Experiments
    for cfg in cache_configs:
        out = f"{RESULTS_DIR}/task1_cache/{cfg['name']}.txt"
        run_simulation(cfg['flags'], out)
    
    # Run BTB Experiments
    for cfg in btb_configs:
        out = f"{RESULTS_DIR}/task2_bpred/{cfg['name']}.txt"
        run_simulation(cfg['flags'], out)

    print("\n--- All Experiments Completed ---")