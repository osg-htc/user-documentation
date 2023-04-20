---
ospool:
  path: htc_workloads/submitting_workloads/Slurm_to_HTCondor.md
---

Convert your workflow from Slurm to HTCondor
============================================


# Introduction

[Slurm](https://slurm.schedmd.com/documentation.html) is one of the most popular workload manager for high performance computing (HPC) system while HTCondor
is the scheduler program developed for high throughput computing (HTC) environment. Both being implementations of scheduler/workload managers, they do have
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
- Slurm is good for managing MPI jobs; HTCondor is efficient in running MPI jobs. The parallelization using HTCondor can be achevied without using any specific tools.  

To know more about Slurm please visit their [website](https://slurm.schedmd.com/documentation.html) and for HTCondor take a look at the HTCondor [manual page](https://htcondor.readthedocs.io/en/latest/users-manual/index.html)
Please visit our other guides-especially the [easily submit multiple job page](../submit-multiple-jobs.md) to know more about the modularity of HTCondor scripts.

# General considerations about HTCondor in OSPool
- HTCondor on **OSPool** does not have a **module** and a **shared file system**. User needs to identify every component of their jobs and transfer them from their access point to the execute node. The slides of the [new user training](https://docs.google.com/presentation/d/1z-f81xtk_ZXeJcA1kX60JoScXdGfe-xgsB9g5YemrqI/edit#slide=id.g10c0fd09133_0_7) contians more detils about it.
- Instead of relying on modules, please use the [different conatiners](../../using_software/available-containers-list.md) available on the OSPool or make your own [container](../../using_software/containers-singularity.md). Please remember the faciliation team is here to [support you](../../../support_and_training/support/getting-help-from-RCFs.md).
- By default the [wall time limit](../../workload_planning/jobdurationcategory.md) set on HTCondor jobs are 20 hours on the OSPool.
