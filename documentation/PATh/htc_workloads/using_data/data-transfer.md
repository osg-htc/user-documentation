---
path:
  path: htc_workloads/using_data/data-transfer.md
---

# Data Staging and Transfer to Jobs

Table of Contents: 
[TOC]

# Overview

As a distributed system, jobs in the PATh Facility can run in different physical locations, where the computers that are executing jobs don't have direct access to the files placed on the Access Point (e.g. in a /home directory on ap1.facility.path-cc.io). In order to run on this kind of distributed system, jobs need to "bring along" the data, code, packages, and other files from the Access Point (where the job is submitted) to the PATh Facility execute points (where the job will run).  HTCondor's file transfer tools and plugins make this possible; input and output files are specified as part of the job submission and then moved to and from the execution location. 

This guide describes where to place files on PATh Facility Access Points, and how to use these files within jobs. 

# Transferring Data To/From HTCondor Jobs

There are two spaces for placing files on the PATh Facility Access Point, and each has a corresponding transfer method for referencing files in the submit file. 

<table>
<tr>
  <th>Location</th>
  <th>File Sizes</th>
  <th>Transfer Method</th>
  <th>Initial Quota</th>
</tr>
<tr>
  <td rowspan="2"><code>/home/$USER</code></td>
  <td>Input: less than 1Gb per job</td>
  <td rowspan="2">file paths in <code>transfer_input_files</code></td>
  <td rowspan="2">50GB</td>
</tr>
<tr>
  <td>Output: less than 1Gb per job</td>
</tr>
<tr>
  <td rowspan="2"><code>/data/$USER</code></td>
  <td>greater than 1Gb per job <br> OR shared files used by many jobs </td>
  <td rowspan="2"><code>stash:///</code> links in <code>transfer_input_files</code></td>
  <td rowspan="2">500GB / 250k items</td>
</tr>
<tr>
  <td> greater than 1Gb per job</td>
</tr>
</table>

**Regardless of where data is placed, jobs should only be submitted with `condor_submit` from `/home`.**

## Transfer Smaller Job Input and Output Files to/from /home 

You should use your `/home` directory to stage job files where: 
* individual input files per job are less than 1GB per file, and if there 
are multiple files, they total less than 1GB
* output files per job are less than 1GB per file

### Input Files from `/home`

To transfer input files from `/home`, list the files by name in the `transfer_input_files` submit file option. You can use either absolute or relative paths to your input files. Multiple files can be specified using a comma-separated list. 

Some examples: 

* Transferring multiple files from the submission directory
		transfer_input_files = my_data.csv, my_software.tar.gz, my_script.py
* Transferring a file using an absolute path is useful if a file is not in the same directory tree as your submit file: 
		transfer_input_files = /home/username/path/to/my_software.tar.gz

### Output Files to `/home`

By default, files created by your job will automatically be returned to your `/home` directory. If you would like a file to return to a diffrent subfolder within your `/home` directory, use HTCondor's `transfer_output_remaps` option. 

<!--For more information, see below.
Link to different guide??? --> 

## Transfer Larger Job Input and Output Files to/from `/path-facility/data`

You should use your `/path-facility/data` directory to stage job files where: 
* individual input files per job are greater than 1GB per file
* an input file (of any size) is used by many jobs
* output files per job are greater than 1GB per file

> **Important Note:** 
> Large files stored in `/path-facility/data` are cached, so it is important to use a 
> descriptive file name (possibly using version names or dates within the file name), or 
> a directory structure with unique names to 
> ensure you know what version of the file you are using within your job. 

### Input Files from `/path-facility/data` 

To transfer input files from `/path-facility/data`, use the `stash:///` plugin syntax as part of the `transfer_input_files` submit file option. 

Some examples: 

* Transferring one file from `/path-facility/data`

		transfer_input_files = stash:///path-facility/data/<username>/InFile.txt

* When using multiple files from `/path-facility/data`, it can be useful to use 
	HTCondor submit file variables to make your list of files more readable: 

		# Define a variable (example: STASH_LOCATION) equal to the 
		# path you would like files transferred to, and call this 
		# variable using $(variable)
		STASH_LOCATION = stash:///path-facility/data/<username>
		transfer_input_files = $(STASH_LOCATION)/InputFile.txt, $(STASH_LOCATION)/database.sql

### Output Files to `/path-facility/data`

If you would like a job to transfer a large file back to your `/path-facility/data` directory, in your HTCondor submit file, use the same `stash:///` plugin syntax as for input files, but with the HTCondor `transfer_output_remaps` submit file option. When 
transferring multiple files back to `/path-facility/data` in this way, you will separate
the different files/remaps with a semi-colon. 

Some examples: 
	
* Transferring one output file (`OutFile.txt`) back to `/path-facility/data`: 

		transfer_output_remaps = "OutFile.txt=stash:///ospool/protected/<username>/OutFile.txt"

* When using multiple files from `/path-facility/data`, it can be useful to use 
	HTCondor submit file variables to make your list of files more readable. Also note 
	the semi-colon separator in the list of output files. 

		# Define a variable (example: STASH_LOCATION) equal to the 
		# path you would like files transferred to, and call this 
		# variable using $(variable)
		STASH_LOCATION = stash:///path-facility/data/<username>
		transfer_output_remaps = "file1.txt = $(STASH_LOCATION)/file1.txt; file2.txt = $(STASH_LOCATION)/file2.txt; file3.txt = $(STASH_LOCATION)/file3.txt"

# Moving Data to/from PATh Facility Access Points

In general, common Unix tools such as rsync, scp, PuTTY, WinSCP, gFTP, etc. can be used to upload data from your computer or another server to your PATh Facility Access Point or to download files. Files should be uploaded/created and staged in `/home` or `/path-facility` for preparation to use in jobs (as described above). 

# Check Your Quota and Available Space

## Check your `/home` quota

To check your home quota and usage, run: 

	$ quota -vs

##  Check your `/path-facility/data` quota

*coming soon!*

## Request Quota Increase

Contact us at support@path-cc.io if you think you need a quota increase. We have space for substantial workloads when communicated with in advance. 

# Data Policies

In general, users are responsible for managing data and for using appropriate mechanisms for delivering data to/from jobs. Each space for data is controlled with a quota and should be treated as temporary storage for *active* job execution. The PATh Facility has no routine backup of data in these locations, and users should remove old data after jobs complete. 

Data stored within `/home` and `/path-facility/data` is available only to your jobs, but highly sensitive data (e.g. HIPPA) should never be uploaded to OSG resources. 

PATh staff reserve the right to monitor and/or remove data without notice to the user if doing so is necessary for ensuring proper use or to quickly fix a performance or security issue. Additionally, users should not use PATh resources or services for long-term data storage (see above). 

