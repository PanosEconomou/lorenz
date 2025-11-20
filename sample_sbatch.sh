#!/bin/bash

#SBATCH --job-name=Comphys     # Job name (appears in the queue)
#SBATCH --output=lorenz-%j.out # Standard output file (%j is replaced with job ID)
#SBATCH --error=lorenz-%j.err  # Standard error file
#SBATCH --time=00:10:00        # Maximum runtime (HH:MM:SS)
#SBATCH --nodes=1              # Number of nodes requested
#SBATCH --ntasks-per-node=20   # Number of processes per node
#SBATCH --mem=1G               # Memory limit per node

# --- Executable commands start below this line ---


module load python
srun python lorenz.py
echo "Job finished"
