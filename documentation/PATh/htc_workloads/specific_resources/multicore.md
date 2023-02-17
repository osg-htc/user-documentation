---
path:
    path: htc_workloads/specific_resources/multicore.md
---

Multicore
=========

Please note, the PATh Facility has limited support for multicore jobs. Multicore jobs
can be submitted for threaded or OpenMP applications. To request multiple cores
(aka cpus) use the HTCondor *request_cpus* attribute in your submit file. 

Example:

    request_cpus = 8

We recommend requesting a maximum of 8 cpus.


**Important considerations**    

When submitting multicore jobs please note that you will also have to tell 
your code or application to use the number of cpus requested in your submit 
file. Do not use core auto-detection as it might detect more cores than what 
were actually assigned to your job.
