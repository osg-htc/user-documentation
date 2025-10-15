---
ospool:
  path: htc_workloads/specific_resource/retry-request-memory.md
---

Automatically Rerunning a Job That Used Too Much Memory
=======================================================

Some workloads have variable memory requirements across jobs.
For example, most jobs may need only 2 GB of RAM, but a small
subset, perhaps a few percent, might require 6 GB or more to complete
successfully. The challenge is that you often do not know in advance
which jobs will need additional memory.

HTCondor provides a built-in mechanism to handle this: the
`retry_request_memory` feature. When enabled, HTCondor will automatically
retry a job that exceeds its initial memory request, increasing the
requested memory on subsequent runs.

Use this feature only if a small fraction (typically less than 20%) of
your jobs require additional memory. If the majority of jobs exceed the
baseline, you should instead increase the default `request_memory` value.

For example, using the submit file below, the initial job execution
requests 2 GBs of memory. If the job exceeds this limit, HTCondor will
place it on hold with the reason `memory usage exceeded request_memory`.
The job will then be automatically released, and the subsequent
execution (and any further retries) will run with a memory limit of 6
GBs.

```
executable = my-job.sh

log        = job.log
output     = job.out
error      = job.err

request_cpus   = 1
request_memory = 2 GB
request_disk   = 5 GB

# provide higher memory when retrying
retry_request_memory = 6 GB

queue
```

Keep in mind that OSG resources have limited availability for
large-memory jobs. Requests for higher memory will generally experience
longer queue times compared to lower memory jobs.



