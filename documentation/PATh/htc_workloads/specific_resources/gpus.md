---
path:
    path: htc_workloads/specific_resources/gpus.md
---

GPUs
====

The PATh Facility has an increasing number of GPUs available to 
run jobs. 

# Requesting GPUs

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

HTCondor records different GPU attributes that can be used to select 
specific types of GPU devices. A few attributes that may be useful: 

* `GPUs_Capability`: this is NOT the GPU library, but rather a measure of the GPU's "Compute Capability"
* `GPUs_DriverVersion`: maximum version of the GPU libraries that can be supported
* `GPUs_GlobalMemoryMb`: amount of GPU memory available on the GPU device

Any of the attributes above can be used in the submit file's `requirements` line to 
select a specific kind of GPU. For 
example, to request a GPU with more than 8GB of GPU memory, one could use: 

    requirements = (GPUs_GlobalMemoryMb >= 8192)
    
If you want a certain type or family of GPUs, we usually recommend using the GPU's 
'Compute Capability', known as the `GPUs_Capability` by HTCondor. An A100 GPU has a 
Compute Capability of 8.0, so if you wanted to run on an A100 GPU or higher, 
the submit file requirement would be: 

    requirements = versioncmp("8.0", GPUs_Capability) >= 0

**Note that the more requirements you include, the fewer resources will be available 
to you! It's always better to set the minimal possible requirements (ideally, none!) 
in order to access the greatest amount of computing capacity.**

# Available GPUs

Description of the available CPUs can be found under the 
[Facility Description](https://path-cc.io/facility/index.html#facility-description).
Currently, A100 is the main GPU available.

# Software and Data Considerations

## Software for GPUs

For GPU-enabled machine learning libraries, we recommend using 
containers to set up your software for jobs: 

  * [Software Containers](../../../htc_workloads/using_software/containers/)

