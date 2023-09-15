---
ospool:
  path: htc_workloads/managing_data/file-transfer-via-htcondor.md
---

Transfer Smaller Job Files To and From /home
=======================

As described in the [Overview: Data Staging and Transfer to Jobs](../overview/) 
any data, files, or even software that is <1GB should be staged in 
your `/home` directory on your Access Point. Files in your 
`/home` directory can be transferred to jobs via your HTCondor submit file.

## Transfer Files From `/home` Using HTCondor

### Transfer Input Files from `/home`

To transfer input files from `/home`, list the files by name in the
`transfer_input_files` submit file option. You can use either absolute
or relative paths to your input files. Multiple files can be specified
using a comma-separated list.

To transfer files from your `/home` directory use the `transfer_input_files` 
statement in your HTCondor submit file. For example:

	# submit file example
	
	# transfer small file from /home 
	transfer_input_files = my_data.csv

Multiple files can be specified using a comma-separated list, for example:

	# transfer multiple files from /home
	transfer_input_files = my_data.csv, my_software.tar.gz, my_script.py

When using `transfer_input_files` to transfer files located in `/home`, 
keep in mind that the path to the file is relative to the location of 
the submit file. If you have files located in a different `/home` subdirectory, 
we recommend specifying the full path to those files, which is also a matter 
of good practice, for example:

	transfer_input_files = /home/username/path/to/my_software.tar.gz

Note that the path is not replicated on the remote side. The job will only
see `my_software.tar.gz` in the top level job directory.

Above, `username` refers to your access point username.

## Use HTCondor To Transfer Outputs

By default, HTCondor will transfer any new or modified files in the     
job's top-level directory back to your `/home` directory location from  
which the `condor_submit` command was performed. **This behavior only   
applies to files in the top-level directory of where your job executes, 
meaning HTCondor will ignore any files created in subdirectories of the 
job's top-level directory.** Several options exist for modifying this   
default output file transfer behavior, including those described in     
this guide.                                                             

### What is the top-level directory of a job?

Before executing a job, HTCondor will create a new directory on the execute 
node just for your job - this is the top-level directory of the job and the 
path is stored in the environment variable `_CONDOR_SCRATCH_DIR`. All of the 
input files transferred via `transfer_input_files` will first be written to 
this directory and it is from this path that a job starts to execute. After 
a job has completed the top-level directory and all of it's contents are 
deleted.

### Select Specific Output Files To Transfer to `/home` Using HTCondor

As described above, HTCondor will, by default, transfer any files
that are generated during the execution of your job(s) back to your
`/home` directory. If your job(s) will produce multiple output files but
you only need to retain a subset of these output files, you can use a submit
file option to only transfer back this file: 

	transfer_output_files = output.svg

Alternatively, you can delete the unrequired output files or move them to a subdirectory as
a step in the bash executable script of your job - only the output files
that remain in the top-level directory will be transferred back to your
`/home` directory.

### Organize Output Files in `/home`

By default, output files will be copied back to the directory in `/home`
where you ran the `condor_submit` command. To modify these behavior, 
you can use the `transfer_output_remaps` option in the HTCondor submit file. 
The syntax for `transfer_output_remaps` is: 

    transfer_output_remaps = "Output1.txt = path/to/save/file/under/output.txt; Output2.txt = path/to/save/file/under/RenamedOutput.txt"

### What if my output file(s) are not written to the top-level directory?

If your output files are written to a subdirectory, use the steps described 
[below](#group-multiple-output-files-for-convenience) to convert the output 
directory to a "tarball" that is written to the top-level directory. 

Alternatively, you can include steps in the executable bash script of 
your job to move (i.e. `mv`) output files from a subdirectory to 
the top-level directory. For example, if there is an output file that 
needs to be transferred back to the login node named `job_output.txt` 
written to `job_output/`:

	#! /bin/bash
	
	# various commands needed to run your job
	
	# move csv files to scratch dir
	mv job_output/job_output.txt $_CONDOR_SCRATCH_DIR

### Group Multiple Output Files For Convenience

If your jobs will generate multiple output files, we recommend combining
all output into a compressed tar archive for convenience, particularly
when transferring your results to your local computer from your login
node. To create a compressed tar archive, include commands in your your
bash executable script to create a new subdirectory, move all of the
output to this new subdirectory, and create a tar archive. For example:

	#! /bin/bash
	
	# various commands needed to run your job
	
	# create output tar archive
	mkdir my_output
	mv my_job_output.csv my_job_output.svg my_output/
	tar -czf my_job.output.tar.gz my_ouput/

The example above will create a file called `my_job.output.tar.gz` that
contains all the output that was moved to `my_output`. Be sure to create
`my_job.output.tar.gz` in the top-level directory of where your job
executes and HTCondor will automatically transfer this tar archive back
to your `/home` directory.




