---
ospool:
  path: htc_workloads/managing_data/data-transfer.md
---

# Data Staging and Transfer to Jobs¶

Due to the distributed configuration of the OSG, more often than not, your jobs will need to bring along a copy (i.e. transfer a copy) of data, code, packages, software, etc. from the Access Point (e.g. login04.osgconnect.net) where the job is submitted to the OSPool execute node where the job will run. This requirement applies to all files that are needed to successfully execute and complete your job that do not otherwise exist on OSG execute servers. This guide describes where OSG Connect users can store files on OSG-operatated Access Points, and how to use these files within jobs. 

Table of Contents: 
[TOC]

## Overview

OSG-managed Access Points have two locations for uploading data and software files that are needed for running  your jobs, `/home` and `/protected`. Where you store your files and how your files are made accessible to your jobs depends on how much data is needed or produced by your jobs.

In general, users are responsible for managing data in these folders and for using appropriate mechanisms for delivering data to/from jobs. Each is controlled with a quota and should be treated as temporary storage for *active* job execution. OSG Connect has no routine backup of data in these locations, and users should remove old data after jobs complete. **If you think you'll need more space for a set of concurrently-queued jobs, even after cleaning up old data, please send a request to [support@osg-htc.org](mailto:support@osg-htc.org)!**

**Notice: Depreciation of `/public`**
Prior to January 2023, OSG Connect users stored files in `/home` and `/public` directories. Users with accounts created prior to 2023 are highly encouraged to move files in `/public` to `/protected` to prepare for the eventual depreciation of `/public`. Users with accounts created in January 2023 and after should only use `/home` and `/protected`.

# Uploading/Downloading Data to/from OSG-operated Access Points
In general, common Unix tools such as rsync, scp, PuTTY, WinSCP, gFTP, etc. can be used to upload data from your computer or another server to your OSG Access Point (e.g. `login05.osgconnect.net`), or to download files from your OSG Access Point. Files should be uploaded/created and staged in `/home` or `/protected` for preparation to use in jobs. 

# Transferring Data To/From HTCondor Jobs
Use the following table to determine where to stage input files for jobs and where to store output files from jobs:  

|  Location  | Job Input/Output Data Sizes   | Transfer to/from Jobs | Initial Quota |
| :---------- | :----------------------------------- | :------ | :------ |
| `/home`    | Less than 500 MB per job  | **Input Files**:`transfer_input_files = InFile.txt`<br>**Output Files**: Files created in job return to `/home` by default. |  50 GB |
| `/protected` | Greater than 500 MB per job | **Input Files**: `transfer_input_files = stash:///ospool/protected/<username>/InFile.txt`<br>**Output Files**: `transfer_output_remaps = stash:///stash:///ospool/protected/<username>/OutFile.txt` | 500 GB |

**Important Details:** 
* Data stored within `/home` and `/protected` is available only to your jobs, but highly sensitive data (e.g. HIPPA) should never be uploaded to OSG resources. 
* Large files stored in `/protected` are cached, so it is important to use a descriptive file name (possibly using version names or dates within the file name) to ensure you know what version of the file you are using within your job. 


## Transfer Job Input and Output Files to/from /home 

**`/home`**
  * *Jobs should only be submitted with condor_submit from /home*, so HTCondor submit files should only be created in `/home`
  * *Job Input Files*: use HTCondor's `transfer_input_files` submit file option with either absolute or relative paths to your input files. For example, `transfer_input_files = /home/<username>/InFile.txt`

Multiple files can be specified using a comma-separated list, for example:

```
transfer_input_files = my_data.csv, my_software.tar.gz, my_script.py
```

When using transfer_input_files to transfer files located in `/home`, keep in mind that the path to the file is relative to the location of the submit file. If you have files located in a different /home subdirectory, we recommend specifying the full path to those files, which is also a matter of good practice, for example:

```
transfer_input_files = /home/username/path/to/my_software.tar.gz
```







  * *Job Output Files*: By default, files created by your job will automatically be returned to your `/home` directory. If you would like a file to return to a diffrent subfolder within your `/home` directory, use HTCondor's `transfer_output_remaps` option. For more information, see below. 

## Transfer Job Input and Output Files to/from `/protected`

**`/protected`** 
  * *Job Input Files*: Transfer files from /protected using `transfer_input_files = stash:///ospool/protected/<username>/InFile.txt`. This combines HTCondor's `transfer_input_files` with a stash file transfer protocol, `stash:///`. 
  * *Job Output Files*: If you would like a job to transfer a large file back to your `/protected` directory, in your HTCondor submit file, use `transfer_output_remaps` with the stash transfer mechanism (`stash:///ospool/protected/<username>`). For example, `transfer_output_remaps = stash:///ospool/protected/<username>/OutFile.txt`. 

# HTCondors Transfer_output_remaps 
For output, users can use the `transfer_output_remaps` option in their job's submit file to specify what (1) path to save a file to and/ or (2) what name to save it under. Using this approach, it is possible to save files back to specific locations in `/home` or `/protected`. 

The syntax for `transfer_output_remaps` is:

```
transfer_output_remaps = "Output.txt = path/to/save/file/under/Output.txt"
```

When saving large output files back to `/protected`, it is necessary to combine `transfer_output_remaps` with a stash transfer mechanism. Therefore, the path provided will look like:

```
transfer_output_remaps = "Output.txt = stash:///ospool/protected/<username>/Output.txt"
```

# Submit File Examples for transferring data in/out of /home and /protected

## Submit File Example for `/protected` Input/Output Files

```
#Example submit file tranferring data to/from /protected
executable = myscript.sh

# Transfer an input file from /protected to a job
transfer_input_files = stash:///ospool/protected/<username>/InputFile.txt

# Transfer a job output file from a job to /protectedd
transfer_output_remaps = "Output.txt = stash:///osgconnect/public/<username>/Output.txt"

error = job.error
output = job.output
log = job.log

requirements = (OSGVO_OS_STRING =?= "RHEL 7")

request_cpus = 1
request_memory = 1 MB
request_disk = 1 MB

queue 1
```

## Submit File Example for many `/protected` Input/Output Files per Job

If you have several output files being sent to `/protected`, you may wish to define a new submit file variable to avoid having to re-write the stash:/// path repeatedly. For example,

```
#Example submit file tranferring *many* files to/from /protected
executable = myscript.sh

#Define a variable (example: STASH_LOCATION) equal to the path you would like files saved to/pulled from, and call this variable using $(variable) to transfer input and/or output files  
STASH_LOCATION = stash:///ospool/protected/<username>
transfer_input_files = $(STASH_LOCATION)/InputFile.txt
transfer_output_remaps = "file1.txt = $(STASH_LOCATION)/file1.txt; file2.txt = $(STASH_LOCATION)/file2.txt; file3.txt = $(STASH_LOCATION)/file3.txt"

error = job.error
output = job.output
log = job.log

requirements = (OSGVO_OS_STRING =?= "RHEL 7")

request_cpus = 1
request_memory = 1 MB
request_disk = 1 MB

queue 1
```

# Check Your Quota and Available Space
There are two primary ways to check your remaining `/home` and `/protected` disk space: 

## Option 1: Quota Usage Displayed Upon Login
Your quota status will be automatically displayed when you login:

Disk utilization for username:
/protected   : [                        ] 0% (0/500000 MB)
/home     : [ #                      ] 4% (2147/53687 MB)


## Option 2: Display usage with `quota` command 
You can also display your quota usage at any time using the command `quota` while connected to your login node.

## Request Quota Increase
Contact us at support@osg-htc.org if you think you need a quota increase. We can support very large amounts of data!
  
# Data Policies
* **Right to Delete Data:**
OSG staff reserve the right to monitor and/or remove data without notice to the user if doing so is necessary for ensuring proper use or to quickly fix a performance or security issue. Additionally, users should not use OSG resources or services for long-term data storage. Files and directories that have not been accessed for over six months may be deleted by OSG staff with or without notifying the user. 
* **Jobs should only be submitted from /home:** Jobs should only ever be submitted from /home, never /protected. Users are also prohibited from making their `/home` directory world-readable due to security concerns. 
  
# Phase Out of /public and Stashcp Command
* **/public phase out:** As of Fall 2022, it is recommended that users use the new `/protected` file storage location instead of `/public`. `/protected` users will still have access to the same amount of data storage space as `/public`, but files will not be publically accessable, will have enhanced security, and other benefits. `/public` will be deprecated in the future. 
* **Stashcp command phase out:** Historically, output files could be transferred from a job to a `/public` location using the stashcp command within the job's executable, however, this mechanism is no longer encouraged for OSPool users. Instead, jobs should use `transfer_output_remaps` (an HTCondor feature) to transfer output files to `/protected`. By using `transfer_output_remaps`, HTCondor will manage the output data transfer for your jobs. Data transferred via HTCondor is more likely to be transferred successfully and errors with transfer are more likely to be reported to the user. Additionally, users should no longer use `/public`, as it is being replaced by `/protected` and will be depreciated in the future. 





# Questions and Get Help
For additional data information, see the "Data Storage and Transfer" section of our FAQ.

For assistance or questions, please email the OSG Research Facilitation team at support@osg-htc.org.
