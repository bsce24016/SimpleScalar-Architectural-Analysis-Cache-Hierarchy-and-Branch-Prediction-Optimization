📌 Project Overview
This project evaluates the performance trade-offs of various Cache Hierarchies and Branch Prediction strategies using the SimpleScalar (PISA) out-of-order simulator. By simulating the ijpeg benchmark, the study quantifies how hardware complexity impacts execution efficiency (CPI) and total clock cycles.

🛑 The Problem: Workload Starvation
A significant hurdle in architectural simulation is the "22k Instruction Trap." Standard benchmarks often fail to locate input files (e.g., .ppm images), causing the simulator to exit prematurely after approximately 22,341 instructions.

Impact of the Problem:
Cold Starts: Caches and branch predictors do not have enough time to "warm up," resulting in skewed accuracy data.

Startup Noise: Statistics reflect program initialization and error handling rather than the core computational workload.

Invalid Trends: Hardware scaling (e.g., moving from 4kB to 512kB cache) appears to have zero impact because the workload is too small to stress the memory hierarchy.

✅ The Solution: Workload-Driven Automation
To ensure valid, steady-state data, this project implements a three-part architectural solution:

1. Workload Injection
The ijpeg benchmark is explicitly paired with the vgrind.ppm workload. This ensures the CPU processes actual image data rather than idling or error-looping, forcing the pipeline to perform real computational work.

2. Steady-State Warm-up (The 1M Threshold)
Every simulation utilizes the -max:inst 1000000 flag. This guarantees a sample size of 1,000,000 instructions, allowing the branch predictor and cache hierarchy to reach a stable, "warmed-up" state.

3. Automated Validation Suite
A custom Python Automation Script was developed to:

Execute 12+ unique hardware configurations (Small, Medium, Large, Excessive, and various BTB layouts) sequentially.

Act as a Data Validator, parsing the sim_num_insn count in each output file to confirm the 1,000,000 instruction threshold was met before the data is accepted for analysis.

⚙️ Requirements
Simulator: SimpleScalar 3.0 (sim-outorder)

ISA: PISA
This is a professional, structured README.md file for your GitHub repository. It clearly defines the architecture problem you faced and the automated, workload-driven solution you developed.

SimpleScalar Architectural Analysis: Cache & Branch Prediction Optimization
📌 Project Overview
This project evaluates the performance trade-offs of various Cache Hierarchies and Branch Prediction strategies using the SimpleScalar (PISA) out-of-order simulator. By simulating the ijpeg benchmark, the study quantifies how hardware complexity impacts execution efficiency (CPI) and total clock cycles.

🛑 The Problem: Workload Starvation
A significant hurdle in architectural simulation is the "22k Instruction Trap." Standard benchmarks often fail to locate input files (e.g., .ppm images), causing the simulator to exit prematurely after approximately 22,341 instructions.

Impact of the Problem:
Cold Starts: Caches and branch predictors do not have enough time to "warm up," resulting in skewed accuracy data.

Startup Noise: Statistics reflect program initialization and error handling rather than the core computational workload.

Invalid Trends: Hardware scaling (e.g., moving from 4kB to 512kB cache) appears to have zero impact because the workload is too small to stress the memory hierarchy.

✅ The Solution: Workload-Driven Automation
To ensure valid, steady-state data, this project implements a three-part architectural solution:

1. Workload Injection
The ijpeg benchmark is explicitly paired with the vgrind.ppm workload. This ensures the CPU processes actual image data rather than idling or error-looping, forcing the pipeline to perform real computational work.

2. Steady-State Warm-up (The 1M Threshold)
Every simulation utilizes the -max:inst 1000000 flag. This guarantees a sample size of 1,000,000 instructions, allowing the branch predictor and cache hierarchy to reach a stable, "warmed-up" state.

3. Automated Validation Suite
A custom Python Automation Script was developed to:

Execute 12+ unique hardware configurations (Small, Medium, Large, Excessive, and various BTB layouts) sequentially.

Act as a Data Validator, parsing the sim_num_insn count in each output file to confirm the 1,000,000 instruction threshold was met before the data is accepted for analysis.

⚙️ Requirements
Simulator: SimpleScalar 3.0 (sim-outorder)

ISA: PISA

Benchmark: ijpeg.ss and corresponding .ppm workloads

Environment: Linux/WSL with Python 3.x

🚀 How to Run
Initialize Project:

Bash
python3 scripts/init_project.py
Execute Simulation Suite:
Bash
   python3 scripts/run_experiments.py
View Results: All raw data is logged in the results/ directory, categorized by task.

📈 Key Findings
Cache Scaling: Demonstrated a clear reduction in CPI as L1/L2 miss rates decreased, up until the point of diminishing returns in the "Excessive" model.

BTB Sensitivity: Confirmed that a 4-way associative BTB (64x4) significantly outperforms a direct-mapped BTB (256x1) by reducing conflict misses, even though total capacity remains equal.

Predictor Efficiency: Achieved stable branch prediction hit rates of approximately 95%, providing a realistic profile of superscalar performance.

Benchmark: ijpeg.ss and corresponding .ppm workloads

Environment: Linux/WSL with Python 3.x
