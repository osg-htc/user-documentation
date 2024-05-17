---
ospool:
  path: htc_workloads/specific_resource/requirements.md
---

Control Where Your Jobs Run / Job Requirements 
====================================

By default, your jobs will match any available slot in the OSG. This is fine
for very generic jobs. However, in some cases a job may have one or more system
requirements in order to complete successfully. For instance, your job may need to run
on a node with a specific operating system.

HTCondor provides several options for "steering" your jobs to appropriate
nodes and system environments. The `request_cpus`, `request_gpus`, `request_memory`, and `request_disk`
submit file attributes should be used to specify the hardware needs of your jobs.
Please see our guides [Multicore Jobs](../../../htc_workloads/specific_resource/multicore-jobs/) and [Large Memory Jobs](../../../htc_workloads/specific_resource/large-memory-jobs/)
for more details.

HTCondor also provides a `requirements` attribute and feature-specific
attributes that can be added to your submit files to target specific environments in
which to run your jobs. 

Lastly, there are some custom attributes you can add to your submit file to
either focus on, or avoid, certain execution sites.

## Requirements

The `requirements` attribute is formatted as an expression, so you can use logical
operators to combine multiple requirements where `&&` is used for AND and
`||` used for OR. For example, the following `requirements` statement will direct
jobs only to 64 bit RHEL (Red Hat Enterprise Linux) 9 nodes.

    requirements = OSGVO_OS_STRING == "RHEL 9" && Arch == "X86_64"

Alternatively, if you have code which can run on either RHEL 8 or 9, you can use OR:

    requirements = (OSGVO_OS_STRING == "RHEL 8" || OSGVO_OS_STRING == "RHEL 9") && Arch == "X86_64"

Note that parentheses placement is important for controling how the logical operations
are interpreted by HTCondor. If you are interested in seeing a list of currently
available operating systems (these are just the default ones, you can create a custom
container image if you want something else):

    $ condor_status -autoformat OSGVO_OS_STRING | sort | uniq -c
 
Another common requirement is to land on a node which has CVMFS.
Then the `requirements` would be:

    requirements = HAS_oasis_opensciencegrid_org == True


## x86\_64 Micro Architecture Levels

The x86\_64 set of CPUs contains a large number of different CPUs with 
different capabilities. Instead of trying to match on on individual attributes
like the AVX/AVX2 ones in the previous section, it can be useful to match
against a family of CPUs. There are currently 4 levels to chose from:
x86\_64-v1, x86\_64-v2, x86\_64-v3, and x86\_64-v4. A description of the levels
is available on [Wikipedia](https://en.wikipedia.org/wiki/X86-64#Microarchitecture_levels).

HTCondor advertises an attribute named `Microarch`. An example on how make jobs
running on the two highest levels is:

    requirements = (Microarch >= "x86_64-v3")

Note that in the past, it was recommended to use the `HAS_AVX` and `HAS_AVX2`
attributes to target CPUs with those capabilities. This is no longer
recommended, with the replacement being `Microarch >= "x86_64-v3"`.


## Additional Feature-Specific Attributes

There are many attributes that you can use with `requirements`. To see what values
you can specify for a given attribute you can run the following command while
connected to your login node:

    $ condor_status -af {ATTR_NAME} | sort -u

For example, to see what values you can specify for the `Microarch` attribute run:

    $ condor_status -af Microarch | sort -u
    x86_64-v1
    x86_64-v2
    x86_64-v3
    x86_64-v4

You will find many attributes will take the boolean values `true` or `false`.

Below is a list of common attributes that you can include in your submit file `requirements` statement. 

- **Microarch** - See above. x86\_64-v1, x86\_64-v2, x86\_64-v3, and x86\_64-v4

- **OSGVO_OS_NAME** - The name of the operating system of the compute node. 
  The most common name is _RHEL_

- **OSGVO_OS_VERSION** - Version of the operating system

- **OSGVO_OS_STRING** - Combined OS name and version. Please see the
  requirements string above on the recommended setup.

- **OSGVO_CPU_MODEL** - The CPU model identifier string as presented in
  /proc/cpuinfo

- **HAS_CVMFS_oasis_opensciencegrid_org** - Attribute specifying
  the need to access specific oasis /cvmfs file system repositories. Other
  common CVMFS repositories are `HAS_CVMFS_singularity_opensciencegrid_org`
  and project ones like `HAS_CVMFS_xenon_opensciencegrid_org`.

For GPU attribtues, such as GPUs' compute capability, see our
[GPU guide](../../../htc_workloads/specific_resource/gpu-jobs/).


## Non-x86 Based Architectures

Within the computing community, there's a growing interest in exploring
non-x86 architectures, such as ARM and PowerPC. As of now, the OSPool
does not host resources based on these architectures; however, it
is designed to accommodate them once available. The OSPool operates
under a system where all tasks are configured to execute on the
same architecture as the host from which they were submitted. This
compatibility is ensured by HTCondor, which automatically adds the
appropriate architecture to the job's requirements. By inspecting the
classad of any given job, one would notice the inclusion of
`(TARGET.Arch == "X86_64")` among its requirements, indicating the
system's current architectural preference.

If you do wish to specify a different architechure, just add it to
your job requirements:

    requirements = Arch == "PPC"

You can get a list of current architechures by running:

    $ condor_status -af Arch | sort | uniq
    X86_64


## Specifying Sites / Avoiding Sites

To run your jobs on a list of specific execution sites, or avoid a set of 
sites, use the `+DESIRED_Sites`/`+UNDESIRED_Sites` attributes in your job
submit file. **These attributes should only be used as a last resort.** For
example, it is much better to use feature attributes (see above) to make
your job go to nodes matching what you really require, than to broadly
allow/block whole sites. We encourage you to contact the facilitation team before taking this action, to make sure it is right for you. 

To avoid certain sites, first find the site names. You can find a 
current list by querying the pool:

    condor_status -af GLIDEIN_Site | sort -u

In your submit file, add a comma separated list of sites like:

    +UNDESIRED_Sites = "ISI,SU-ITS"

Those sites will now be exluded from the set of sites your job can
run at.

Similarly, you can use `+DESIRED_Sites` to list a subset of sites
you want to target. For example, to run your jobs at the SU-ITS site,
and only at that site, use:


    +DESIRED_Sites = "ISI,SU-ITS"

Note that you should only specify one of `+DESIRED_Sites`/`+UNDESIRED_Sites`
in the submit file. Using both at the same time will prevent the job from
running.
