---
path:
    path: htc_workloads/specific_resources/gpus.md
---

GPUs
====

The PATh Facility has an increasing number of GPUs available to 
run jobs. 

## Requesting GPUs

To request a GPU for your HTCondor job, you can use the 
HTCondor *request_gpus* attribute in your submit file (along 
with the usual *request_cpus*, *request_memory*, and *request_disk*
attributes). For example:

    request_gpus = 1
    request_cpus = 1
    request_memory = 4 GB
    request_disk = 2 GB

You should only request a GPU if your software has been written to use a GPU.

## Specific GPU Requests

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

### Available GPUs

Description of the available CPUs can be found under the 
[Facility Description](https://path-cc.io/facility/index.html#facility-description).
Currently, A100 is the main GPU available. All of the A100s in the Facility have 
40GB of GPU memory and are Capability 8.0. 

## Software and Data Considerations

### Software for GPUs

For GPU-enabled machine learning libraries, we recommend using 
containers to set up your software for jobs: 

  * [Software Containers](../../../htc_workloads/using_software/containers/)

