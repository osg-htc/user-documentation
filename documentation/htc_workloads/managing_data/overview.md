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

!!! danger "Jobs should always be submitted from the `/home` directory"

    Regardless of where your data is placed, you should only submit jobs (`condor_submit`) from the `/home` directory.

## Use `/home` for Smaller Files

You should use your `/home` directory to stage input and output files where:

  * individual input files per job are less than 1GB per file, and if there 
    are multiple files, they total less than 1GB
  * output files per job are less than 1GB per file

Files can to be transferred to and from the `/home` directory using HTCondor's file transfer mechanism, which can easily handle smaller files (<1GB). By default, files created by your job will automatically be returned to your `/home` directory. 

See our [Transfer Files To and From /home guide](../file-transfer-via-htcondor/)
for complete details on managing your files this way. 

## Use the OSDF for Larger Files and Containers

You should use the OSDF ([Open Science Data Federation](https://osg-htc.org/services/osdf.html))
to stage job files where:

  * individual input files per job are greater than 1GB per file
  * an input file (of any size) is used by many jobs
  * output files per job are greater than 1GB per file
  * a Singularity/Apptainer container image (`.sif`) is used

!!! warning "Important Note"

    Files in OSDF are **cached**, so it is important to use a descriptive file name (i.e. version, dates) or a directory structure with unique names to ensure you know what version of the file you are using within your job.

See our guide on where to place your files in the OSDF and how to use 
OSDF URLs in `transfer_input_files`/`transfer_output_files`.

[OSDF guide](../osdf#where-to-put-your-files){.md-button .md-button--primary}

## Quotas

The `/home` directory and OSDF origins all have quota limits. The `/home` directory is
limited to 50 GBs, while OSDF limits vary. You can view your current
usage on the access point with the command `quota` or `quota -vs`.

Jobs will go on hold if quotas are exceeded.

To request an increase in your quota, please send a request with
justification to the ticket system at [support@osg-htc.org](mailto:support@osg-htc.org).

## External Data Transfer to/from Access Point

Most common Unix tools or file transfer programs such as `rsync`, `scp`, Putty, WinSCP,
`gFTP`, etc. can be used to upload data from your computer to access
point, or to download files from the access point.

See our [Data Transfer Guide](../scp) for more details. 

## FAQ

For additional data information, see also the "Data Storage and Transfer" section of 
our [FAQ](../../../overview/references/frequently-asked-questions/#data-storage-and-transfer). 

## Data Policies

Please see the [OSPool Polices](../../../overview/references/policy/) for important
usage polices.

