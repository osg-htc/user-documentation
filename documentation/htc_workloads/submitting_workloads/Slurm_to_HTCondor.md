---
ospool:
  path: htc_workloads/submitting_workloads/Slurm_to_HTCondor.md
---

Convert Your Workflow From Slurm to HTCondor
============================================


## Introduction

[Slurm](https://slurm.schedmd.com/documentation.html) is a common workload manager for high performance computing (HPC) systems while HTCondor
is a scheduler program developed for a high throughput computing (HTC) environment. As they are both implementations of scheduler/workload managers, they have some similarities, like needing to specify the computing resources required for a job. Some differences include the syntax for describing a job, and some of the system assumptions made by 
the scheduling program. In this guide, we will go through some general similarities 
and differences and provide an example of "translating" an existing Slurm submit file 
into HTCondor. [Skip to this example](#comparing-slurm-and-htcondor-files).

## General Diffences Between Slurm and HTCondor

- HTCondor is good at managing a **large quantity** of single-node jobs; Slurm is suitable for scheduling multi-node and multi-core jobs, and can struggle when managing a large quantity of jobs
- Slurm requires a **shared file system** to operate, HTCondor does not.
- Slurm script has a **certain order**- all the requirements on the top then the code execution step; HTCondor script does not have any order. The only requirement is that it ends with the **queue** statement.
- Every requirement line in the Slurm script starts with **#SBATCH**. In HTCondor only the system requirements (RAM, Cores, Disk space) line starts with **request_**
- The **queue** statement in HTCondor can be modified (include variables) to make it behave like an array job in Slurm.
- Basic job submission and queue checking command starts with a **condor_** prefix in HTCondor; Slurm commands generally start with the letter `s`. 

> To know more about Slurm please visit their [website](https://slurm.schedmd.com/documentation.html) and for HTCondor take a look at the HTCondor [manual page](https://htcondor.readthedocs.io/en/latest/users-manual/index.html)

## Special Considerations for the OSPool

- HTCondor on **OSPool** does not use **modules** and a **shared file system**. A user needs to identify every component of their jobs and transfer them from their access point to the execute node. The slides of the [new user training](https://docs.google.com/presentation/d/1z-f81xtk_ZXeJcA1kX60JoScXdGfe-xgsB9g5YemrqI/edit#slide=id.g10c0fd09133_0_7) contians more detils about it.
- Instead of relying on modules, please use the [different conatiners](../../using_software/available-containers-list/) available on the OSPool or make your own [container](../../using_software/containers-singularity/). Please remember the faciliation team is here to [support you](../../../support_and_training/support/getting-help-from-RCFs/).
- By default the [wall time limit](../../workload_planning/jobdurationcategory/) on 
the OSPool is 10 hours. 

## Comparing Slurm and HTCondor Files

A sample Slurm script is presented below with the equivalent HTCondor transformation.    

### Submitting One Job

The scenario here is submitting one Matlab job, requesting 
8 cores, 16GB of memory (or RAM), planning 
to run for 20 hours, specifying where to save standard output and error

#### Slurm Example

<pre>
#!/bin/bash
#SBATCH --job-name=sample_slurm	 # Optional in HTCondor     
#SBATCH --error=job.%J.error	    
#SBATCH --output=job.%J.out
#SBATCH --time=20:00:00       
#SBATCH --nodes=1                # HTCondor equivalent does not exist                     
#SBATCH --ntasks-per-node=8          
#SBATCH --mem-per-cpu=2gb            
#SBATCH --partition=batch        # HTCondor equivalent does not exist

module load matlab/r2020a		     
matlab -nodisplay -r "matlab_program(input_arguments),quit"
</pre>

#### HTCondor Example

<pre>
+SingularityImage = "/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-matlab-runtime:R2020a"
executable = matlab_program
arguments = input_arguments

# optional
batch_name = sample_htcondor

error = job.$(ClusterID).$(ProcID).error
output = job.$(ClusterID).$(ProcID).out
log = job.$(ProcID).log

# transfer_input_files = 

+JobDurationCategory = "Long"

request_cpus = 8
request_memory = 16 GB
request_disk = 2 GB

queue 1
</pre>

Notice that: 
- Using a Singularity image replaces module loading
- The Matlab command becomes executable and arguments in the submit file
- HTCondor has its own custom "log" format in addition to saving standard output 
and standard error. 
- If there are additional input files, they would need to be added in the 
"transfer_input_files" line. 
- Note that memory is *total*
 not per-core. We also need to request disk 
 space for the job's working directory, as it is not 
 running on a shared file system. 

### Submit Multiple Jobs

Using the same base example, what options are needed if you wanted to run multiple 
copies of the same basic job? 

#### Slurm Example

In Slurm, multiple tasks are expressed as an array job: 

<pre>
%%%%%%%%%%%%%%%%%highlights for submitting an array jobs %%%%%%%%%%%%%%%%%%%%%%%%%%%
#SBATCH --array=0-9

module load matlab/r2020a	
matlab -nodisplay -r "matlab_program(input_arguments,$SLURM_ARRAY_TASK_ID),quit"
</pre>

#### HTCondor Example

In HTCondor, multiple tasks are submitted as many independent jobs. The 
`$(ProcID)` variable takes the place of `$SLURM_ARRAY_TASK_ID` above. 
<pre>
%%%%%%%%%%%%%%% equivalent changes to HTCondor for array jobs%%%%%%%%%%%%%%%%%%%%%%%%%%
executable = matlab_program
arguments = input_arguments, $(ProcID)

queue 10
</pre>

HTCondor has many more ways to submit multiple jobs, behind this simple numerical 
approach. See our other HTCondor guides for more details. 
