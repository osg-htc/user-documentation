---
ospool:
  path: htc_workloads/managing_data/data-storage.md
---
# Data Staging and Transfer to Jobs¶


# Overview of Locations to Place Data Files

OSG-managed Access Points have two locations for uploading files (data and software) that are needed for running jobs, `/home` and `/protected`. Where you store your files and how your files are made accessible to your jobs depends on how much data is needed or produced by your jobs.

In general, users are responsible for managing data in these folders and for using appropriate mechanisms for delivering data to/from jobs, as detailed below. Each is controlled with a quota and should be treated as temporary storage for active job execution. OSG Connect has no routine backup of data in these locations, and users should remove old data after jobs complete, in part, to make room for future submissions. 

# Check Your Quota and Available Space

Users have the following default quotas: 

| Location | Default Quota |
| :---------- | :---------- |
| /home | 50 GB |
| /protected | 500 GB |

There are two primary ways to check your remaining disk space: 

## Option 1: Quota Usage Displayed Upon Login

Your quota status will be automatically displayed when you login:

```
Disk utilization for username:
/public   : [                        ] 0% (0/500000 MB)
/home     : [ #                      ] 4% (2147/53687 MB)
```

## Option 2: Display usage with `quota` command 

You can also display your quota usage at any time using the command `quota` while connected to your login node.

## Request Quota Increase

Contact us at support@osg-htc.org if you think you need a quota increase. We can support very large amounts of data!


# Uploading/Downloading Data to/from OSG-operated Access Points

In general, common Unix tools such as rsync, scp, Putty, WinSCP, gFTP, etc. can be used to upload data from your computer to your OSG Access Point (e.g. `login05.osgconnect.net`), or to download files from your OSG Access Point. Files should be uploaded/created and staged in `/home` or `/public` for preparation to use in jobs. 

# Transferring Data To/From Jobs¶
Use the following table to determine where to stage input files for jobs and where to store output files from jobs:  

| File Location  | Job Input/ Output Data Sizes   | Transfer to/from Jobs | Availability |
| :---------- | :----------------------------------- | :------ | :------ | Files available only to your jobs. |
| `/home`    | Less than 500 MB per job  | **Input Files**:`transfer_input_files = InFile.txt`<br>**Output Files**: Files created in job return to `/home` by default. |
| `/protected` | Greater than 500 MB per job | **Input Files**: `transfer_input_files = stash:///ospool/protected/user/InFile.txt`<br>**Output Files**: `transfer_output_remaps = stash:///stash:///ospool/protected/user/OutFile.txt` |

**Important Details:** 
* Data stored within `/home` and `/protected` is available only to your jobs. 
* Large files stored in `/protected` are cached, so it is important to use a descriptive file name (possibly using version names or dates within the file name) to ensure you know what version of the file you are using within your job. 


## Transfer Small Job Input and Output Files to/from /home 
/home: 
  * Only job input and output data less than 500 MB should be stored in `/home`
  * *Job Input files*: use HTCondor's `transfer_input_files` submit file option with either absolute or relative paths to your input files. For example, `transfer_input_files = /home/<username>/InFile.txt`
  * *Job Output files*: By default, files created by your job will automatically be returned to your `/home` directory. If you would like a file to return to a diffrent subfolder within your `/home` directory, use HTCondor's `transfer_output_remaps` option. For more information, see {Guide}

## Transfer Large Job Input and Output Files to/from /protected 
/protected: 
  * Only job input and output data greater than 500 MB should be stored in `/protected`
  * *Job Input files*: Transfer files from /protected using `transfer_input_files = stash:///ospool/protected/<username>/InFile.txt`. This combines HTCondor's `transfer_input_files` with a file transfer protocol, `stash:///ospool/protected/<username>/`. 
  * *Job Output files*: If you would like a job to transfer a large file back to your /protected directory, in your HTCondor submit file, use `transfer_output_remaps = stash:///ospool/protected/<username>/OutFile.txt`. 
  

# HTCondor's Transfer_output_remaps 

For output, users can use the `transfer_output_remaps` option within their job's submit file, which will transfer the user's specified file to a different location than the default `/home/username`. 

By using `transfer_output_remaps`, it is possible to specify what path to save a file to and what name to save it under. Using this approach, it is possible to save files back to specific locations in `/public` (as well as your `/home` directory, if desired).

The syntax for transfer_output_remaps is:

```
transfer_output_remaps = "Output.txt = path/to/save/file/under/output.txt; Output.txt = path/to/save/file/under/RenamedOutput.txt"
```
When saving large output files back to `/protected`, the path provided will look like:

```
transfer_output_remaps = "Output.txt = stash:///ospool/protected/<username>/Output.txt"
```


## Submit File Example for /protected` Input/Output Files

```
log = my_job.$(Cluster).$(Process).log
error = my_job.$(Cluster).$(Process).err
output = my_job.$(Cluster).$(Process).out

requirements = (OSGVO_OS_STRING =?= "RHEL 7")

transfer_input_files = stash:///ospool/protected/<username>/InputFile.txt
transfer_output_remaps = "Output.txt = stash:///osgconnect/public/<username>/Output.txt"

...other submit file details...
```



## Submit File Example for many /protected` Input/Output Files

If you have several output files being sent to `/protected`, you may wish to define a new submit file variable to avoid having to re-write the stash:/// path repeatedly. For example,

```
log = my_job.$(Cluster).$(Process).log
error = my_job.$(Cluster).$(Process).err
output = my_job.$(Cluster).$(Process).out

requirements = (OSGVO_OS_STRING =?= "RHEL 7")

STASH_LOCATION = stash:///ospool/protected/<username>
transfer_input_files = $(STASH_LOCATION)/InputFile.txt
transfer_output_remaps = "file1.txt = $(STASH_LOCATION)/file1.txt; file2.txt = $(STASH_LOCATION)/file2.txt; file3.txt = $(STASH_LOCATION)/file3.txt"

...other submit file details...
```

# Phase Out of /public and Stashcp Command¶

* As of Fall 2022, it is recommended that users use the new /protected file storage location instead of /public. 

* Historically, output files could be transferred from a job to a `/public` location using the stashcp command within the job's executable, however, this mechanism is no longer encouraged for OSPool users. Instead, jobs should use `transfer_output_remaps` (an HTCondor feature) to transfer output files to `/public`. By using `transfer_output_remaps`, HTCondor will manage the output data transfer for your jobs. Data transferred via HTCondor is more likely to be transferred successfully and errors with transfer are more likely to be reported to the user.
