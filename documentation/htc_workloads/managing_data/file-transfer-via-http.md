---
ospool:
  path: htc_workloads/managing_data/file-transfer-via-http.md
---

Transfer HTTP-available Files up to 1GB In Size 
====================================

# Overview

If some of the data or software your jobs depend on is available via the web, 
you can have such files transferred by HTCondor using the appropriate HTTP address! 

## Important Considerations

While our [Overview of Data Mangement on the OSPool](../../../htc_workloads/managing_data/overview/) 
describes how you can stage data, files, or even software on OSG data locations, 
any web-accessible file can be transferred directly to your jobs **IF**:

- the file is accessible via an HTTP address
- the file is less than 1GB in size (if larger, you'll need to pre-stage them for [OSDF](../../../htc_workloads/managing_data/osdf/))
- the server or website they're on can handle large numbers of your jobs accessing them simultaneously

Importantly, you'll also want to make sure your job executable knows how to handle the file 
(un-tar, etc.) from within the working directory of the job, just like it would for any other input file.

## Transfer Files via HTTP

To download a file available by HTTP into a job, use an HTTP URL in 
combination with the `transfer_input_files` statement in your HTCondor submit file. 

For example:

	# submit file example
	
	# transfer software tarball from public via http
	transfer_input_files = http://www.website.com/path/file.tar.gz
	
	...other submit file details...

Multiple URLs can 
be specified using a comma-separated list, and a combination of URLs and 
files from `/home` directory can be provided in a comma separated list. For example,

	# transfer software tarball from public via http
	# transfer additional data from AP /home via htcondor file transfer
	transfer_input_files = http://www.website.com/path/file1.tar.gz, http://www.website.com/path/file2.tar.gz, my_data.csv
