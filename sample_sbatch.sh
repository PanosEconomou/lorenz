#!/bin/bash

#SBATCH --job-name=Comphys     # Job name (appears in the queue)
#SBATCH --output=lorenz-%j.out # Standard output file (%j is replaced with job ID)
#SBATCH --error=lorenz-%j.err  # Standard error file
#SBATCH --time=00:10:00        # Maximum runtime (HH:MM:SS)
#SBATCH --nodes=1              # Number of nodes requested
#SBATCH --ntasks-per-node=20   # Number of processes per node
#SBATCH --mem=1G               # Memory limit per node

# --- Executable commands start below this line ---

# Load necessary software modules
module load python

# Change to the submission directory
cd $SLURM_SUBMIT_DIR

# Run your program
srun python my_script.py arg1 arg2

echo "Job finished"
