---
path:
    path: htc_workloads/submitting_workloads/quickstart.md
---

# Quickstart - Submit Example HTCondor Jobs


## Job 1: A simple, nonparallel job

First create a `short.sh` file to use as en executable for our sample job:


	#!/bin/bash
	# short.sh: a short discovery job
        set -e
	printf "Start time: "; /bin/date
	printf "Job is running on node: "; /bin/hostname
	printf "Job running as user: "; /usr/bin/id
	printf "Job is running in directory: "; /bin/pwd
	echo
	echo "Working hard..."
	sleep 20
	echo "Science complete!"

Now, make the script executable.

	chmod +x short.sh


### Run the job locally

When setting up a new job submission, it's important to test your job outside
of HTCondor before submitting into pool. 

	$ ./short.sh
	Start time: Wed Aug 21 09:21:35 CDT 2013
	Job is running on node: ap1.path-facility
	Job running as user: uid=54161(netid) gid=1000(users)
	Job is running in directory: /home/netid/quickstart
	Working hard...
	Science complete!

### Create an HTCondor submit file

So far, so good! Let's create a simple (if verbose) HTCondor submit file. Name it `tutorial01.submit`.

	# Our executable is the main program or script that we've created
	# to do the 'work' of a single job.
	executable = short.sh

	# We need to name the files that HTCondor should create to save the
	#  terminal output (stdout) and error (stderr) created by our job.
	#  Similarly, we need to name the log file where HTCondor will save
	#  information about job execution steps.
	error = short.error
	output = short.output
	log = short.log

	# We need to request the resources that this job will need:
	request_cpus = 1
	request_memory = 100 MB
	request_disk = 1 GB

	# The last line of a submit file indicates how many jobs of the above
	#  description should be queued. We'll start with one job.
	queue 1

### More about projects

The PATh Facility is using projects to track usage and charge the
correct allocation. If you only have one project, you do not need to 
worry about this - the system will map your jobs automatically to 
that one project. However, if you have multiple ones, you will
have to add an attribute to your submit file to indicate which 
project to charge. The attribtute name is `accounting_group`.
For example, if your project is `AmazingScience`, the line in
the submit file (somewhere before the `queue` line) should
be:

    accounting_group = AmazingScience

### Submit the job 

Submit the job using `condor_submit`:

	$ condor_submit tutorial01.submit
	Submitting job(s). 
	1 job(s) submitted to cluster 144121.

### Check the job status

The `condor_q` command tells the status of currently running jobs.
Generally you will want to limit it to your own jobs: 

	$ condor_q netid
	OWNER	   BATCH_NAME     SUBMITTED   DONE   RUN    IDLE  TOTAL JOB_IDS
	netid	 ID: 1441271  12/10 14:18	 _	1      _      1 1441271.0

	Total for query: 1 jobs; 0 completed, 0 removed, 0 idle, 1 running, 0 held, 0 suspended
	Total for netid: 1 jobs; 0 completed, 0 removed, 0 idle, 1 running, 0 held, 0 suspended
	Total for all users: 3001 jobs; 0 completed, 0 removed, 2189 idle, 754 running, 58 held, 0 suspended

You can also get status on a specific job cluster: 

	$ condor_q 1441271
	OWNER	   BATCH_NAME     SUBMITTED   DONE   RUN    IDLE  TOTAL JOB_IDS
	netid	 ID: 1441271  12/10 14:18	 _	1      _      1 1441271.0

	Total for query: 1 jobs; 0 completed, 0 removed, 0 idle, 1 running, 0 held, 0 suspended
	Total for netid: 1 jobs; 0 completed, 0 removed, 0 idle, 1 running, 0 held, 0 suspended
	Total for all users: 3001 jobs; 0 completed, 0 removed, 2189 idle, 754 running, 58 held, 0 suspended
	

Note the `DONE`, `RUN`, and `IDLE` columns. Your job will be listed in the `IDLE` column if
it hasn't started yet. If it's currently scheduled and running, it will
appear in the `RUN` column. As it finishes up, it will then show in the `DONE` column.
Once the job completes completely, it will not appear in `condor_q`. 

Let's wait for your job to finish – that is, for `condor_q` not to show
the job in its output. A useful tool for this is watch – it runs a
program repeatedly, letting you see how the output differs at fixed
time intervals. Let's submit the job again, and watch `condor_q` output
at two-second intervals: 

	$ condor_submit tutorial01.submit
	Submitting job(s). 
	1 job(s) submitted to cluster 1441272
	$ watch -n2 condor_q netid 
	... 

When your job has completed, it will disappear from the list. 

*Note*: To close watch, hold down Ctrl and press C. 

### Job history

Once your job has finished, you can get information about its execution
from the `condor_history` command: 

	$ condor_history 1441272
	 ID      OWNER            SUBMITTED     RUN_TIME ST   COMPLETED CMD           
	 1441272.0   netid     12/10 14:18   0+00:00:29 C  12/10 14:19 /home/netid/tutorial-quickstart/short.sh 

*Note*: You can see much more information about your job's final status
using the `-long` option. 


### Check the job output

Once your job has finished, you can look at the files that HTCondor has
returned to the working directory. The names of these files were specified in our
submit file. If everything was successful, it should have returned:

* a log file from HTCondor for the job cluster: short.log
* an output file for each job's output: short.output
* an error file for each job's errors: short.error

Read the output file. It should be something like this: 

	$ cat short.output
	Start time: Mon Dec 10 20:18:56 UTC 2018
	Job is running on node: osg-84086-0-cmswn2030.fnal.gov
	Job running as user: uid=12740(osg) gid=9652(osg) groups=9652(osg)
	Job is running in directory: /srv

	Working hard...
	Science complete!
	
Job 2: Passing arguments to executables 
---------------------------------------

Sometimes it's useful to pass arguments to your executable from your
submit file. For example, you might want to use the same job script
for more than one run, varying only the parameters. You can do that
by adding Arguments to your submission file.

First, let's edit our existing `short.sh` script to accept arguments. To
avoid losing our original script, we make a copy of the file under the
name `short_transfer.sh`

	$ cp short.sh short_transfer.sh
	
Now, edit the file to include the added lines below:

	#!/bin/bash
	# short.sh: a short discovery job
    set -e
	printf "Start time: "; /bin/date
	printf "Job is running on node: "; /bin/hostname
	printf "Job running as user: "; /usr/bin/id
	printf "Job is running in directory: "; /bin/pwd
	printf "The command line argument is: "; $1
	printf "Contents of $1 is "; cat $1
	cat $1 > output.txt
	printf "Working hard..."
	ls -l $PWD
	sleep 20
	echo "Science complete!"

We need to make our new script executable just as we did before:

	$ chmod +x short_transfer.sh

Notice that with our changes, the new script will now print out the
contents of whatever file we specify in our arguments, specified by the
`$1`. It will also copy the contents of that file into another file
called `output.txt`.

Make a simple text file called `input.txt` that we can pass to our script:

	"Hello World"

Once again, before submitting our job we should test it locally to ensure it runs as we expect:

	$ ./short_transfer.sh input.txt
	Start time: Tue Dec 11 10:19:12 CST 2018
	Job is running on node: ap.path-facility
	Job running as user: uid=100279(netid) gid=1000(users)
	Job is running in directory: /home/netid/tutorial-quickstart
	The command line argument is: Contents of input.txt is "Hello World"Working hard...total 28
	drwxrwxr-x 2 netid users   34 Oct 15 09:37 Images
	-rw-rw-r-- 1 netid users   13 Oct 15 09:37 input.txt
	drwxrwxr-x 2 netid users  114 Dec 11 09:50 log
	-rw-r--r-- 1 netid users   13 Dec 11 10:19 output.txt
	-rwxrwxr-x 1 netid users  291 Oct 15 09:37 short.sh
	-rwxrwxr-x 1 netid users  390 Dec 11 10:18 short_transfer.sh
	-rw-rw-r-- 1 netid users  806 Oct 15 09:37 tutorial01.submit
	-rw-rw-r-- 1 netid users  547 Dec 11 09:49 tutorial02.submit
	-rw-rw-r-- 1 netid users 1321 Oct 15 09:37 tutorial03.submit
	Science complete!

Now, let's edit our submit file to properly handle these new arguments and output files and save this as `tutorial02.submit`

	# We need the job to run our executable script, with the
	#  input.txt filename as an argument, and to transfer the
	#  relevant input and output files:
	executable = short_transfer.sh
	arguments = input.txt
	transfer_input_files = input.txt
	transfer_output_files = output.txt

	error = job.error
	output = job.output
	log = job.log

	# The below are good base requirements for first testing jobs, 
	#  if you don't have a good idea of memory and disk usage.
	request_cpus = 1
	request_memory = 1 GB
	request_disk = 1 GB

	# Queue one job with the above specifications.
	queue 1


Notice the added `arguments = input.txt` information. The `arguements` option specifies what arguments should be passed to the executable. 

The `transfer_input_files` and `transfer_output_files` options need to be included as well.  When jobs are executed on the Open Science Pool via HTCondor, they are sent only with files that are specified. Additionally, only the specified output files are returned with the job. **Any output not transferred back, with the exception of our `error`, `output`, and `log` files, are discarded at the end of the job.**

Submit the new submit file using `condor_submit`. Be sure to check your output files once the job completes.

	$ condor_submit tutorial02.submit
	Submitting job(s).
	1 job(s) submitted to cluster 1444781.
	
	

Job 3: Submitting jobs concurrently
-----------------------------------

What do we need to do to submit several jobs simultaneously? In the
first example, Condor returned three files: out, error, and log. If we
want to submit several jobs, we need to track these three files for each
job. An easy way to do this is to add the `$(Cluster)` and `$(Process)`
macros to the HTCondor submit file. Since this can make our working
directory really messy with a large number of jobs, let's tell HTCondor
to put the files in a directory called log. Here's what the third submit
file looks like, called `tutorial03.submit`:

	# We need the job to run our executable script, arguments and files.
	#  Also, we'll specify unique filenames for each job by using
	#  the job's 'cluster' value.
	executable = short_transfer.sh
	arguments = input.txt
	transfer_input_files = input.txt
	transfer_output_files = output.txt

	error = log/job.$(Cluster).$(Process)error
	output = log/job.$(Cluster).$(Process).output
	log = log/job.$(Cluster).$(Process).log

	request_cpus = 1
	request_memory = 1 GB
	request_disk = 1 GB

	# Let's queue ten jobs with the above specifications
	queue 10

Before submitting, we also need to make sure the log directory exists.

	$ mkdir -p log

You'll see something like the following upon submission:

	$ condor_submit tutorial03.submit
	Submitting job(s)..........
	10 job(s) submitted to cluster 1444786.
	
Look at the output files in the log directory and notice how each job received its own separate output file:

    $ ls ./log
    job.1444786.0.error   job.1444786.1.error   job.1444786.2.error
    job.1444786.3.error   job.1444786.4.error   job.1444786.5.error
    job.1444786.6.error   job.1444786.7.error	job.1444786.8.error
    job.1444786.9.error   job.1444786.0.log     job.1444786.1.log
    job.1444786.2.log     job.1444786.3.log	    job.1444786.4.log
    job.1444786.5.log     job.1444786.6.log     job.1444786.7.log
    job.1444786.8.log     job.1444786.9.log     job.1444786.0.output
    job.1444786.1.output  job.1444786.2.output  job.1444786.3.output
    job.1444786.4.output  job.1444786.5.output  job.1444786.6.output
    job.1444786.7.output  job.1444786.8.output  job.1444786.9.output

### Where did jobs run? 

It might be interesting to see where our jobs actually ran. To get that
information for a single job, we can use the command `condor_history`.
First, select a job you want to investigate and then run `condor_history
-long jobid`. In this example, we will investigate the job ID 1444786.9.
Again the output is quite long:

	$ condor_history -limit 1 -long 1444786.9
	BlockWriteKbytes = 0
	BlockReads = 0
	DiskUsage_RAW = 36
	... 
	MATCH_EXP_JOBGLIDEIN_ResourceName = "Georgia_Tech_PACE_CE_2"
	...
	
Looking through here for a hostname, we can see that the parameter
`MATCH_EXP_JOBGLIDEIN_ResourceName`. The output of this parameter is
the slot our job ran on. In this example, our job ran on a slot at the
Georgia Institute of Technology.

Removing jobs
--------------

On occasion, jobs will need to be removed for a variety of reasons
(incorrect parameters, errors in submission, etc.). In these instances,
the `condor_rm` command can be used to remove an entire job submission
or just particular jobs in a submission. The `condor_rm` command accepts
a cluster id, a job id, or username and will remove an entire cluster
of jobs, a single job, or all the jobs belonging to a given user
respectively. E.g. if a job submission generates 100 jobs and is
assigned a cluster id of 103, then `condor_rm 103.0` will remove the
first job in the cluster. Likewise, `condor_rm 103` will remove all
the jobs in the job submission and `condor_rm [username]` will remove
all jobs belonging to the user. The `condor_rm` documenation has more
details on using `condor_rm` including ways to remove jobs based on other
constraints.


