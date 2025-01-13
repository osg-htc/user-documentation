---
path:
   path: overview/references/credit-account-charges.md
---

# Credit Account Charges

This page describes the specific credit charges for certain resources on the 
[PATh Facility](https://path-cc.io/facility/). For details on how to request 
credits for your project, see [Request PATh Facility Credits](../account-setup/request-credits)

Credits may be requested and used under the CPU Credit category or the GPU Credit category. Credits are
specific to each node type – CPU Credits are not transferable to GPU Credits, and vice-versa. CPU Credit charges
are defined by a combination of per-job cores and memory request, while GPU Credit charges are defined by a combination
of per-job GPU, CPU, and memory request.

## CPU Credits

|Cores per job|Credit charge per core hour|
|--- |--- |
|1|1.0|
|2-8|1.2|
|8-32|1.5|
|>32|2.0|


When running on a resource with hyperthreaded cores, a 40% discount is applied;
e.g., 1 hyperthreaded core for 1 hour costs 0.6 credits.


## Additional CPU Credit Charge

### Memory Per Core

When more than 2GB per core of memory is requested by the job,
there’s an additional per-GB charge for memory.

|Memory (GB) per job|Credit charge per hour, per GB|
|--- |--- |
|Up to 2GB per core ("nominal")|No charge|
|2-8 GB greater then nominal|0.125|
|8-32|0.25|
|32-128|0.375|
|128-512|0.50|


## CPU Credit Example

If an 8 core job requests 128 GB of RAM, there is an additional
charge for 128 – (8 * 2) = 112 GB of RAM.  If the job ran for an hour, it would
use 0.375 * 112 = 42 credits total for memory and 1.2 * 8 = 9.6 credits for
CPU.


## GPU Credits

|GPUs per job|Credit charge per GPU hour|
|--- |--- |
|1|1.0|
|2|1.2|
|3|1.5|
|4|2.0|


## Additional GPU Credit Charge

### CPUS per GPU

When more than 16 cores per GPU is requested by the job, there’s an additional
per-core charge for the CPU cores beyond the nominal.

|CPUs per GPU|Credit charge per hour, per core|
|--- |--- |
|Up to 16 cores per GPU ("nominal")|No charge|
|16-48 cores per GPU|0.125|
|48-64|0.20|

### Memory per GPU

When more than 2 GB per core of memory is requested by the job, there’s an additional
per-GB charge for memory for the beyond-nominal memory usage.

|Memory (GB) per job|Credit charge per hour, per GB|
|--- |--- |
|Up to 128GB per GPU ("nominal")|No charge|
|128-384 GB per GPU|0.012|
|384-512|0.020|


## GPU Credit Example

If a 1 GPU job requests 256 GB of RAM and 32 cores, there is an additional
charge for 256 – (1 * 128) = 128 GB of RAM and an additional charge for 32 – (1 * 16) = 16 cores.
If the job ran for an hour, it would use 0.012 * 128 = 1.536 credits total for
memory, 0.125 * 16 = 2 credits for CPU, and 1.0 * 1 = 1.0 credits for GPU.
