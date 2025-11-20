#!/bin/bash

#SBATCH --job-name=Comphys     # Job name (appears in the queue)
#SBATCH --output=lorenz-%j.out # Standard output file (%j is replaced with job ID)
#SBATCH --error=lorenz-%j.err  # Standard error file
#SBATCH --time=00:10:00        # Maximum runtime (HH:MM:SS)
#SBATCH --nodes=1              # Number of nodes requested
#SBATCH --ntasks-per-node=1    # Number of times the script will be run per node
#SBATCH --cpus-per-task=20     # Number of CPUS per program run
#SBATCH --mem=2G               # Memory limit per node

# --- Executable commands start below this line ---

module purge
module load anaconda3/2024.02
echo "Loaded Modules"
srun --unbuffered python lorenz_hpc.py
echo "Job finished"


# --- NYU GREENE ---
# https://sites.google.com/nyu.edu/nyu-hpc/hpc-systems/greene/hardware-specs?authuser=0
