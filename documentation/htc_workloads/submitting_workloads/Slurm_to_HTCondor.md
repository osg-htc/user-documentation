---
ospool:
  path: htc_workloads/submitting_workloads/Slurm_to_HTCondor.md
---

Convert your workflow from Slurm to HTCondor
============================================


# Introduction

[Slurm](https://slurm.schedmd.com/documentation.html) is a common workload manager for high performance computing (HPC) system while HTCondor
is a scheduler program developed for a high throughput computing (HTC) environment. Both being implementations of scheduler/workload managers, they do have
some similarities. For both program the user needs to specify the computing resources required for a job but the syntaxes used for this purposes are different

# Common Diffences between Slurm and HTCondor
- Slurm is suitable to schedule multi-core jobs with high degree of parallelism while not good at handling large quantity of jobs.
- HTCondor is good at dealing with **large quantity** of single core jobs.
- Slurm requires a **shared file system** to operate, HTCondor does not.
- Slurm script has a **certain order**- all the requirements on the top then the code execution step; HTCondor script does not have any order. The only requirement is that it ends with the **queue** statement.
- Every requirement line in the Slurm script starts with **#SBATCH**. In HTCondor only the system requirements (RAM, Cores, Disk space) line starts with **request_**
- The **queue** statement in HTCondor can be modified (include variables) to make it behave like an array job in Slurm.
- Basic job submission and queue checking command starts with a **condor_** prefix in HTCondor. Slurm does not have a specific prefix for this regard.
- HTCondor can have thousands of jobs **running within minutes**. The wait time in the queue for many Slurm jobs is usually much longer.
- Slurm is good for managing MPI jobs; HTCondor is efficient in running HTC jobs. The parallelization using HTCondor can be achieved without using any specific tools, but requires codes to be pleasantly parallel (no inter-node communication)

To know more about Slurm please visit their [website](https://slurm.schedmd.com/documentation.html) and for HTCondor take a look at the HTCondor [manual page](https://htcondor.readthedocs.io/en/latest/users-manual/index.html)
Please visit our other guides-especially the [easily submit multiple job page](../submit-multiple-jobs.md) to know more about the modularity of HTCondor scripts.

# General considerations about HTCondor in OSPool
- HTCondor on **OSPool** does not have a **module** and a **shared file system**. User needs to identify every component of their jobs and transfer them from their access point to the execute node. The slides of the [new user training](https://docs.google.com/presentation/d/1z-f81xtk_ZXeJcA1kX60JoScXdGfe-xgsB9g5YemrqI/edit#slide=id.g10c0fd09133_0_7) contians more detils about it.
- Instead of relying on modules, please use the [different conatiners](../../using_software/available-containers-list/) available on the OSPool or make your own [container](../../using_software/containers-singularity.md). Please remember the faciliation team is here to [support you](../../../support_and_training/support/getting-help-from-RCFs/).
- By default the [wall time limit](../../workload_planning/jobdurationcategory/) set on HTCondor jobs are 20 hours on the OSPool.

# Sample SLURM Scripts
A sample Slurm scripts is presented here with the equivalent HTCondor transformation is shown in the comments.  

<table>
<tr>
<td>
<pre>
#!/bin/bash
#SBATCH --nodes=1              #HTCondor equivalent does not exist                     
#SBATCH --ntasks-per-node=8          
#SBATCH --mem-per-cpu=2gb            
#SBATCH --time=160:00:00       
#SBATCH --job-name=sample_slurm	 #Optional in HTCondor     
#SBATCH --error=job.%J.error	    
#SBATCH --output=job.%J.out          
#SBATCH --partition=batch     #HTCondor equivalent does not exist

module load matlab/r2020a		     
matlab -nodisplay -r "matlab_program(input_arguments),quit"

%%%%%%%%%%%%%%%%%highlights for submitting an array jobs %%%%%%%%%%%%%%%%%%%%%%%%%%%
#SBATCH --array =1-10
module load matlab/r2020a	
matlab -nodisplay -r "matlab_program(input_arguments,$SLURM_ARRAY_TASK_ID),quit"
</pre>
</td>
<td>
<pre>
+SingularityImage = "/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-matlab-runtime:R2020a"
executable = matlab_program
arguments = input_arguments

request_cpus = 8
request_memory = 16 GB
request_disk = 2 GB
+JobDurationCategory = "Long" #The maximum allowed time is 40 hours

error = job.$(ProcID).error
output = job.$(ProcID).out
log = job.$(ProcID).log

queue 1

%%%%%%%%%%%%%%% equivalent changes to HTCondor for array jobs%%%%%%%%%%%%%%%%%%%%%%%%%%
executable = matlab_program
arguments = input_arguments, $(ProcID)
queue 10
</pre>
</td>
</tr>
<table>
