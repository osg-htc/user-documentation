---
ospool:
  path: htc_workloads/managing_data/overview.md
---

# Overview: Data Staging and Transfer to Jobs 

## Overview

As a distributed system, jobs on the OSPool will run in different
physical locations, where the computers that are executing jobs don't
have direct access to the files placed on the Access Point (e.g. in a
`/home` directory). In order to run on this
kind of distributed system, jobs need to "bring along" the data, code,
packages, and other files from the access point (where the job is
submitted) to the execute points (where the job will run).
HTCondor's file transfer tools and plugins make this possible; input and
output files are specified as part of the job submission and then moved
to and from the execution location.

This guide describes where to place files on the access
points, and how to use these files within jobs, with links to a more 
detailed guide for each use case. 

## Always Submit From `/home`

**Regardless of where data is placed, jobs should only be submitted with 
`condor_submit` from `/home`**

## Use HTCondor File Transfer for Smaller Job Files

You should use your `/home` directory to stage job files where:

  * individual input files per job are less than 1GB per file, and if there 
    are multiple files, they total less than 1GB
  * output files per job are less than 1GB per file

Files can to be transferred to and from the `/home` directory
using HTCondor's file transfer mechanism.  Input files can be 
specified in the submit file and by default, 
files created by your job will automatically be returned
to your `/home` directory. 

See our [Transfer Files To and From /home guide](../file-transfer-via-htcondor/)
for complete details on managing your files this way. 

## Use OSDF for Larger Files and Containers

You should use the OSDF ([Open Science Data Federation](https://osg-htc.org/services/osdf.html))
to stage job files where:

  * individual input files per job are greater than 1GB per file
  * an input file (of any size) is used by many jobs
  * output files per job are greater than 1GB per file

You should also always use the OSDF to stage Singularity/Apptainer container 
files (with the ending `.sif`) for jobs. 

> **Important Note:**
> Files in OSDF are cached, so it is important to use a
> descriptive file name (possibly using version names or dates within the file name), or
> a directory structure with unique names to
> ensure you know what version of the file you are using within your job.

To use the OSDF, files are placed (or returned to) a local path, and moved to 
and from the job using a URL notation in the submit file. 

To see where to place your files in the OSDF and how to use 
OSDF URLs in `transfer_input_files`/`transfer_output_files`, 
please see the [OSDF](../osdf) guide.

## Quotas

`/home` and OSDF origins all have quota limits. `/home` is usually
limited to 50 GBs, while OSDF limits vary. You can find out your current
usage by running `quota` or `quota -vs`

Note that jobs will go on hold if quotas are exceeded.

If you want an increase in your quota, please send a request with
justification to the ticket system [support@osg-htc.org](mailto:support@osg-htc.org)

## External Data Transfer to/from Access Point

In general, common Unix tools such as `rsync`, `scp`, Putty, WinSCP,
`gFTP`, etc. can be used to upload data from your computer to access
point, or to download files from the access point.

See our [Data Transfer Guide](../scp) for more details. 

## FAQ

For additional data information, see also the "Data Storage and Transfer" section of 
our [FAQ](../../../overview/references/frequently-asked-questions/#data-storage-and-transfer). 

## Data Policies

Please see the [OSPool Polices](../../../overview/references/policy/) for important
usage polices.

