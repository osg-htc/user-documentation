---
ospool:
  path: htc_workloads/specific_resource/gpu-jobs.md
---

GPU Jobs
========

GPUs (Graphical Processing Units) are a special kind of computer
processor that are optimized for running very large numbers of simple
calculations in parallel, which often can be applied to problems related
to image processing or machine learning. Well-crafted GPU programs for
suitable applications can outperform implementations running on CPUs
by a factor of ten or more, but only when the program is written and
designed explicitly to run on GPUs using special libraries like CUDA.

## Requesting GPUs

To request a GPU for your HTCondor job, you can use the 
HTCondor *request_gpus* attribute in your submit file (along 
with the usual *request_cpus*, *request_memory*, and *request_disk*
attributes). For example:

    request_gpus = 1
    request_cpus = 1
    request_memory = 4 GB
    request_disk = 2 GB

Users can request one or multiple GPU cores on a single GPU machine.

### Specific GPU Requests

If your software or code requires a certain type of GPU, or has some
other special requirement, there are options to specify this. 

	gpus_minimum_capability = <version>
	gpus_maximum_capability = <version>
	gpus_minimum_memory = <quantity in MB>

The first two options relate to GPU capability; the last to GPU memory 

**1) Capability**

If you want a certain type or family of GPUs, we usually recommend using the GPU's 
"Capability". This value is NOT the CUDA library, but rather a measure of the 
GPU's "Compute Capability," which is related to hardware generation. See the 
[table below](#gpu-types) for examples of GPU capability values. 

For example, an NVIDIA A100 GPU has a 
Compute Capability of 8.0, so if you wanted to run on an A100 GPU specifically, 
the submit file requirement would be: 

    gpus_minimum_capability = 8.0

If you wanted *only* to use that type of GPU (not anything newer), you could also set the 
maximum capability: 

	gpus_maximum_capability = 8.0

**2) GPU Memory**

GPU memory (also sometimes called "vram") is the amount of memory available on 
the GPU device. In HTCondor, GPU Memory is in units of megabytes. 

If you didn't care about the age of the GPU, but just the amount of available memory
(at least, say 20GB or 20,000MB), you would use something like: 

	gpus_minimum_memory = 20000

There are additional attributes that can be used to select GPU types; email the 
facilitation team if the above options do not satisfy your use case. 

**Note that the more requirements you include, the fewer resources will be available 
to you! It's always better to set the minimal possible requirements (ideally, none!) 
in order to access the greatest amount of computing capacity.**

### Sample Submit File

    universe = container
    container_image = /cvmfs/singularity.opensciencegrid.org/htc/tensorflow:1.3

    log = job_$(Cluster)_$(Process).log
    error = job_$(Cluster)_$(Process).err
    output = job_$(Cluster)_$(Process).out
    
    executable = run_gpu_job.py
    #arguments = 

    +JobDurationCategory = "Medium"
   
    # specify both general requirements and gpu requirements if there are any
    # in this example, we are running on GPUs with at least 12GB of GPU memory
    # requirements =
    # gpus_minimum_capability = <version>
	# gpus_maximum_capability = <version>
	gpus_minimum_memory = 12000
    
    request_gpus = 1
    request_cpus = 1
    request_memory = 4GB
    request_disk = 4GB
    
    queue 1

## Available GPUs

### Capacity

There are multiple OSPool contributors providing GPUs on a regular
basis to the OSPool. Some of these contributors will make their GPUs
available only when there is demand in the job queue, so after initial
small-scale job testing, we strongly recommend submitting a signficant
batch of test jobs to explore how much throughput you can get in the
system as a whole. As a reminder, because the OSPool is dynamic, the more jobs submitted requesting GPUs, the more GPU machines will be pulled into the OSPool as execution points.

### GPU Types

Because the composition of the OSPool can change from day to day, we do
not know exactly what specific GPUs are available at any given time.
Based on previous GPU job executions, you might land on one of the
following types of GPUs:

| GPU Type | Capability | Memory | 
| -------- | ---------- | ------ | 
| V100 | 7.0 | 16 GB | 
| GeForce GTX 2080 Ti | 7.5 | 10GB | 
| A100 | 8.0 | 40GB or 80GB | 
| A10 | 8.6 | 22GB | 
| GeForce RTX 3090 | 8.6 | 24GB |
| GeForce RTX 4090 | 8.9 | 24GB | 

## Software and Data Considerations

### Software for GPUs

For GPU-enabled machine learning libraries, we recommend using 
software containers to set up your software for jobs: 

  * [Containers - Apptainer/Singularity](../../../htc_workloads/using_software/containers-singularity/)
  * [Sample TensorFlow GPU Container Image Definition](https://github.com/opensciencegrid/osgvo-tensorflow-gpu/blob/master/Dockerfile)
  * [TensorFlow Example Job](../../../software_examples/machine_learning/tutorial-tensorflow-containers/)
