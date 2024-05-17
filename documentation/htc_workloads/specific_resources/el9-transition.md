---
ospool:
  path: htc_workloads/specific_resource/el9-transition.md
---

EL9 Transition
==============

During May 2024, the OSPool will transition to be mostly EL9 based. The
access points will be upgraded, and the execution points will mostly
shift to EL9.

Note that `EL9` in this context refers to Enterprise Linux 9, and is
an umbrella term for CentOS Stream 9 and derived distributions such as 
AlmaLinux 9 and RockyLinux 9.


## What You Need to Do

The access point transitions will be mostly transparent. You will get
an email about when the switchover will happen, and the access point
will be offline for about 8 hours. Data and jobs will be retained, so no
action is required.


### If your jobs use containers (Apptainer/Singularity, Docker)

**No action is needed for researchers already using a
Apptainer/Singularity or Docker software containers in their jobs.** Becuase
software containers have a small operating system installed inside of
them, these jobs carry everything they need with them and do not rely
signifcantly on the host operating system. By default, your jobs will
match to any operating system in the HTC pool, including the new EL9
hosts.


### All other jobs (not using containers)

**Researchers not already using a Docker or Apptainer software container** will need to either:

 * Test their software/code on an EL9 machine to see their software needs to be rebuilt, and
   then update the job requirements line to refer to `RHEL 9`. See 
   [Requirements](../requirements/#requirements)

or

 * Switch to using a software container (recommended). See the below for additional information.

If you would like to access as much computing capacity as possible,
consider using an Apptainer or Docker software container for your jobs so
that your jobs can match to a variety of operating systems.


## Options For Transitioning Your Jobs

### Option 1: Use a Software Container (Recommended)

Using a software container to provide a base version of Linux will allow
you to run on any nodes in the OSPool regardless of the operating
system it is running, and not limit you to a subset of nodes.

 * [Apptainer/Singularity](../../using_software/containers-singularity/)
 * [Docker](../../using_software/containers-docker/)

### Option 2: Transition to a New Operating System

At any time, you can require a specific operating system version
(or versions) for your jobs. Instructions for requesting a specific
operating system(s) are outlined here:

 * [Requirements](../requirements/#requirements)

This option is more limiting because you are restricted to operating
systems used by OSPool, and the number of nodes running that operating
system.

Alternativly, you can make your job run in a provided base OS
container. For example, if you want your job to always run in RHEL 8,
remove the `requirements` and add `+SingularityImage` in your submit
file. Example:

    +SingularityImage = "/cvmfs/singularity.opensciencegrid.org/htc/rocky:8"
    requirements = True



