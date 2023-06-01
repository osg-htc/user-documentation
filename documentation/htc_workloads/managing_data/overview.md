---
ospool:
  path: htc_workloads/managing_data/overview.md
---

# Overview: Data Staging and Transfer to Jobs 

## Overview

As a distributed system, jobs can run in different
physical locations, where the computers that are executing jobs don't
have direct access to the files placed on the Access Point (e.g. in a
/home directory). In order to run on this
kind of distributed system, jobs need to "bring along" the data, code,
packages, and other files from the access point (where the job is
submitted) to the execute points (where the job will run).
HTCondor's file transfer tools and plugins make this possible; input and
output files are specified as part of the job submission and then moved
to and from the execution location.

This guide describes where to place files on the access
points, and how to use these files within jobs.

## Always Submit From `/home`

**Regardless of where data is placed, jobs should only be submitted with `condor_submit` from `/home`**

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
files (`.sif`) for jobs. 

> **Important Note:**
> Files in OSDF are cached, so it is important to use a
> descriptive file name (possibly using version names or dates within the file name), or
> a directory structure with unique names to
> ensure you know what version of the file you are using within your job.

To use the OSDF, files are placed (or returned to) a local path, and moved to 
and from the job using a URL notation in the submit file. 

The local path and the base URL for the OSDF transfer varies by access point.
Please find the access point entry below. *Protected* means that data is
only accessible by your user, while *Public* means that the data is 
publicly discoverable and accessible to anyone.

<table>
<tr>
  <th>Access Point</th>
  <th>OSDF Origin</th>
</tr>
<tr>
  <td>ap40.uw.osg-htc.org</td>
  <td>Protected:
      <ul>
        <li><nobr>Local Path: <code>/mnt/stash/ospool/PROTECTED/[USERNAME]</code></nobr></li>
        <li><nobr>Base URL: <code>osdf:///ospool/PROTECTED/[USERNAME]</code></nobr></li>
      </ul>
  <td>
</tr>
<tr>
  <td>ap20.uc.osg-htc.org</td>
  <td>Protected:
      <ul>
        <li><nobr>Local Path: <code>/ospool/ap20/data/[USERNAME]</code></nobr></li>
        <li><nobr>Base URL: <code>osdf:///ospool/ap20/data/[USERNAME]</code></nobr></li>
      </ul>
      Protected Project:
      <ul>
        <li><nobr>Local Path: <code>/ospool/uc-shared/projects/[PROJECT]</code></nobr></li>
        <li><nobr>Base URL: <code>osdf:///ospool/uc-shared/projects/[PROJECT]</code></nobr></li>
      </ul>
      Public Project:
      <ul>
        <li><nobr>Local Path: <code>/ospool/uc-shared/public/[PROJECT]</code></nobr></li>
        <li><nobr>Base URL: <code>osdf:///ospool/uc-shared/public/[PROJECT]</code></nobr></li>
      </ul>
  <td>
</tr>
<tr>
  <td>ap21.uc.osg-htc.org</td>
  <td>Protected:
      <ul>
        <li><nobr>Local Path: <code>/ospool/ap20/data/[USERNAME]</code></nobr></li>
        <li><nobr>Base URL: <code>osdf:///ospool/ap20/data/[USERNAME]</code></nobr></li>
      </ul>
      Protected Project:
      <ul>
        <li><nobr>Local Path: <code>/ospool/uc-shared/projects/[PROJECT]</code></nobr></li>
        <li><nobr>Base URL: <code>osdf:///ospool/uc-shared/projects/[PROJECT]</code></nobr></li>
      </ul>
      Public Project:
      <ul>
        <li><nobr>Local Path: <code>/ospool/uc-shared/public/[PROJECT]</code></nobr></li>
        <li><nobr>Base URL: <code>osdf:///ospool/uc-shared/public/[PROJECT]</code></nobr></li>
      </ul>
  <td>
</tr>
<tr>
  <td>login04.osgconnect.net</td>
  <td>Protected:
      <ul>
        <li><nobr>Local Path: <code>/protected/[USERNAME]</code></nobr></li>
        <li><nobr>Base URL: <code>osdf:///osgconnect/protected/[USERNAME]</code></nobr></li>
      </ul>
      Public:
      <ul>
        <li><nobr>Local Path: <code>/public/[USERNAME]</code></nobr></li>
        <li><nobr>Base URL: <code>osdf:///osgconnect/public/[USERNAME]</code></nobr></li>
      </ul>
  </td>
</tr>
<tr>
  <td>login05.osgconnect.net</td>
  <td>Protected:
      <ul>
        <li><nobr>Local Path: <code>/protected/[USERNAME]</code></nobr></li>
        <li><nobr>Base URL: <code>osdf:///osgconnect/protected/[USERNAME]</code></nobr></li>
      </ul>
      Public:
      <ul>
        <li><nobr>Local Path: <code>/public/[USERNAME]</code></nobr></li>
        <li><nobr>Base URL: <code>osdf:///osgconnect/public/[USERNAME]</code></nobr></li>
      </ul>
  </td>
</tr>
</table>

To see how to use OSDF URLs in `transfer_input_files` and
`transfer_output_files`, please see the [OSDF](../osdf) guide.


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


<br> 
<br>

**Watch this video from the 2021 OSG Virtual School** for more information about Handling Data on OSG:

[<img src="https://raw.githubusercontent.com/OSGConnect/connectbook/master/images/Handling_Data_Video_Thumbnail.png" width="500">](https://www.youtube.com/embed/YBGWycYZRD4)


