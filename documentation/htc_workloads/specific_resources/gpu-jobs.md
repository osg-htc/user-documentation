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
other special requirement, there is a special submit file line to
request these capabilities, `require_gpus`. A few attributes that may
be useful: 

  * `Capability`: this is NOT the GPU library, but rather a measure of the GPU's "Compute Capability"
  * `DriverVersion`: maximum version of the GPU libraries that can be supported
  * `GlobalMemoryMb`: amount of GPU memory available on the GPU device

If you want a certain type or family of GPUs, we usually recommend using the GPU's 
'Compute Capability', known as the `Capability` by HTCondor. An A100 GPU has a 
Compute Capability of 8.0, so if you wanted to run on an A100 GPU specifically, 
the submit file requirement would be: 

    require_gpus = (Capability >= 8.0)

Multiple requirements can be specified by using && statements:

    require_gpus = (Capability >= 7.5) && (GlobalMemoryMb >= 11000)

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
   
    # specify both general requirements and gpu requirements 
    requirements = True
    require_gpus = (Capability > 7.5)
    
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
system as a whole.

### GPU Types

Because the composition of the OSPool can change from day to day, we do
not know exactly what specific GPUs are available at any given time.
Based on previous GPU job executions, you might land on one of the
following types of GPUs:

* GeForce GTX 1080 Ti (Capability: 6.1)
* V100 (Capability: 7.0)
* GeForce GTX 2080 Ti (Capability: 7.5)
* Quadro RTX 6000 (Capability: 7.5)
* A100 (Capability: 8.0)
* A40 (Capability: 8.6)
* GeForce RTX 3090 (Capability: 8.6)

## Software and Data Considerations

### Software for GPUs

For GPU-enabled machine learning libraries, we recommend using 
containers to set up your software for jobs: 

  * [Containers - Apptainer/Singularity](../../../htc_workloads/using_software/containers-singularity/)
  * [Sample TensorFlow GPU Container Image Definition](https://github.com/opensciencegrid/osgvo-tensorflow-gpu/blob/master/Dockerfile)
  * [TensorFlow Example Job](../../../software_examples/machine_learning/tutorial-tensorflow-containers/)

### Data Needs for GPU Jobs

As with any kind of job submission, check your data sizes (per job) before submitting 
jobs and choose the appropriate file transfer method for your data. 

See our [Data Staging and Transfer guide](../../../htc_workloads/managing_data/osgconnect-storage/) for
details and contact the Research Computing Facilitation team with questions.
