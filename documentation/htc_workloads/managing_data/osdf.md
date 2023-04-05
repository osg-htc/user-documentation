---
ospool:
  path: htc_workloads/managing_data/osdf.md
---

Transfer Larger Job Files and Containers (OSDF)
===========================================

For input files >1GB and output files >1GB in size, the default HTCondor
file transfer mechanisms run the risk of over-taxing the login nodes and
their network capacity. And this is exactly why the OSDF
([Open Science Data Federation](https://osg-htc.org/services/osdf.html))
exists for researchers with larger per-job data!

Users on an access point can handle such files via the **data caching
origin** and use OSG's caching tools to scalably transfer them between
the running jobs and the origin. The OSG caching tools ensure faster
delivery to and from execute nodes by taking adantage of regional
data caches in the OSG Data Federation, while preserving login node
performance.

Data origins and local mount points varies between the different
access points. **Please see the table under the 
[Overview: Data Staging and Transfer to Jobs](../overview/) for the
details on your assigned access point.**

## Important Considerations and Best Practices

1. **User must never submit jobs from the OSDF locations,** and should continue to
   ONLY submit jobs from within their `/home` directory. All `log`, `error`, `output`
   files and any other files smaller than the above values should ONLY ever
   exist within the user's /home directory.

2. **Files placed within a *Public* OSDF directory are publicly accessible**,
   discoverable and readable by anyone, via the web. Data is made public via `osdf`
   transfer (and, thus, via http addresses), and mirrored to a shared data repository
   which is available on a large number of systems around the world.
	
3. **OSDF files are cached across the Open Science Pool,
   any changes or modifications that you make might not be propagated.**
   This means that if you add a new version of a file the OSDF
   directory, it must first be given a unique name (or directory path) to
   distinguish it from previous versions of that file. Adding a date or
   version number to directories or file names is strongly encouraged to
    manage your files uniqness.

## Use a 'osdf://' URL to Transfer Large Files To Jobs

Jobs will transfer data from the origin when files are indicated
with an appropriate `osdf://` URL (or the older `stash://`) in the
`transfer_input_files` line of the submit file. Make sure to customize the 
data path based on your Access Point, as described in the [Data Overview](../overview/). 

1. Upload your larger files to the local OSDF directory path. This will be something 
like `/protected` or `/ospool/ap40/data`.

2. Add the necessary details to your HTCondor submit file to tell 
   HTCondor which files to transfer, and that your jobs must run on executes nodes that 
   have access to the Open Science Data Federation.

		# Submit file example of large input/software transfer
		
		#Transfer input files
		transfer_input_files = osdf:///ospool/protected/<username>/<dir>/<filename>, <other files>
		
		...other submit file details...

## Use `transfer_output_remaps` and 'osdf://' URL for Outputs

To move output files into an OSDF data origin, users should use the **`transfer_output_remaps`** option
within their job's submit file, which will transfer the user's
specified file to the specific location in the data origin.

By using `transfer_output_remaps`, it is possible to specify what path
to save a file to and what name to save it under. Using this approach,
it is possible to save files back to specific locations in for example
`/protected` (as well as your `/home` directory, if desired).

The syntax for `transfer_output_remaps` is: 

    transfer_output_remaps = "Output1.txt = path/to/save/file/under/output.txt; Output2.txt = path/to/save/file/under/RenamedOutput.txt"

When saving large output files back to `/protected`, the path provided will look like: 

    transfer_output_remaps = "Output.txt = osdf:///ospool/protected/<username>/Output.txt"
	
1. Using `transfer_output_remaps`, tell HTCondor which output files need
   to be transferred back to your OSDF directory and what name you
   want these files to be saved under.

		# submit file example for large output
		
		transfer_output_remaps = "Output.txt = stash:///ospool/protected/<username>/Output.txt"
		
		...other submit file details...

2. If you have several output files being sent to `/protected`, you may
   wish to define a new submit file variable to avoid having to re-write
   the `osdf:///` path repeatedly. For example,

		# submit file example for large output
		
		OSDF_LOCATION = osdf:///ospool/protected/<username>
		transfer_output_remaps = "file1.txt = $(OSDF_LOCATION)/file1.txt; file2.txt = $(OSDF_LOCATION)/file2.txt; file3.txt = $(OSDF_LOCATION)/file3.txt"
		
		...other submit file details...


## Phase out of stash:// and Stashcp command

Historically, output files could be transferred from a job to a
`/public` location using the `stashcp` command within the job's
executable, however, this mechanism is no longer encouraged for OSPool
users. Instead, jobs should use `transfer_output_remaps` (an HTCondor
feature) to transfer output files to your assigned OSDF origin. By using
`transfer_output_remaps`, HTCondor will manage the output data transfer
for your jobs. Data transferred via HTCondor is more likely to be
transferred successfully and errors with transfer are more likely to be
reported to the user.

`osdf://` is the new format for these kind of transfers, and is 
equivalent of the old `stash://` format (which will keep on being
supported for the short term).

