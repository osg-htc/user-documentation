---
ospool:
  path: software_examples/python/manage-python-packages.md
---

Run Python Scripts on the OSPool 
====================================

## Overview

This guide will show you two examples of how to run jobs that use Python in the Open Science Pool.
The first example will demonstrate how to submit a job that uses base Python.
The second example will demonstrate the workflow for jobs that use specific Python packages, including
how to install a custom set of Python packages to your home directory and how to add them to a Python job submission.  

Before getting started, you should know which Python packages you need to run your job.  

## Running Base Python on the Open Science Pool

### Create a bash script to run Python 
To submit jobs that use a module to run base Python, first create a bash executable - for
this example we'll call it `run_py.sh` - which will run our Python script called `myscript.py`.  

For example, `run_py.sh`:

	#!/bin/bash

	# Run the Python script 
	python3 myscript.py

> If you need to use Python 2, 
> replace the `python3` above with `python2`.

### Create an HTCondor submit file

In order to submit `run_py.sh` as part of a job, we need to create an HTCondor 
submit file. This should include the following: 

* `run_py.sh` specified as the executable    
* use `transfer_input_files` to bring our Python script `myscript.py`to wherever the job runs   
* include a standard container image that has Python installed. 

All together, the submit file will look something like this: 

	container_image = /cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-ubuntu-20.04:latest
	   
	executable 	= run_py.sh

	transfer_input_files = myscript.py

	log         = job.log
	output      = job.out
	error       = job.error

	+JobDurationCategory = "Medium"

	request_cpus 	= 1 
	request_memory 	= 2GB
	request_disk 	= 2GB

	queue 1

Once everything is set up, the job can be submitted in the usual way, by running 
the `condor_submit` command with the name of the submit file. 

## Running Python Jobs That Use Additional Packages

It's likely that you'll need additional Python packages that are not
present in the base Python installations. This portion of the
guide describes how to install your packages using [Apptainer](https://apptainer.org/documentation/) and 
then include them as part of your jobs. 

### Install Python packages

Apptainer is installed on the access point and users can use Apptainer to either build an image from the definition file or use apptainer pull to create a `.sif` file from Docker images.**Please note that the docker build will not work on the access point.** More details about the apptainer or building a container image can be found in our [container guide](https://portal.osg-htc.org/documentation/htc_workloads/using_software/containers-singularity/) Before building a container image it is a good practice to set up the cache directory of Apptainer. Run the following command while connected to your login node

     [user@ap]$ mkdir $HOME/tmp
	 [user@ap]$ export TMPDIR=$HOME/tmp
	 [user@ap]$ export APPTAINER_TMPDIR=$HOME/tmp
	 [user@ap]$ export APPTAINER_CACHEDIR=$HOME/tmp$ 

Next, create a definition file for your python package. For this example we are using `python 3.13` and we are installing the `numpy` package using `pip` install. The definition file is given below

    BootStrap: docker
    From: python:3.13

	%post
        # Update the system package index
        apt-get update
        # Install pip if its not already included
        apt-get install -y python3-pip
        # Upgrade pip
        pip3 install --upgrade pip
        # Install NumPy
        pip3 install numpy
     
> You can install each package that you need for your job using the `pip3 install <packagename>` command in your definition file. Save the definition file as `python_3p13.def`. Now, we need to create the container image using `apptainer build python_3p13.sif python_3p13.def`. Feel free to use a name that best describes your python software. 
> If you would like to test the package installation, you can invoke the container using the `apptainer shell` command. To invoke this container please run `apptainer shell python_3p13.sif` and afterwards run the `python3` command 
> and then try importing the packages you just installed. To exit the Python console, 
> type "quit()"

Once you are done, you can close the virtual environment: 

    Singularity> exit

### Modify the HTCondor submit file to transfer Python packages
The submit file for this job will be similar to the base Python job submit file shown above
with one change - we need to modify the `container_image` expression so that it uses our newly built `python_3p13.sif` image. For that we need to upload the Container Image to the [OSDF](https://portal.osg-htc.org/documentation/htc_workloads/managing_data/osdf/)
The image will be resused for each job, and thus the preferred transfer method is OSDF. Store the .sif file under your personal data area on your access point (see table [here](https://portal.osg-htc.org/documentation/htc_workloads/managing_data/osdf/#where-to-put-your-files)).
As an example: 

	container_image = osdf:///ospool/apXX/data/USERNAME/python_3p13.sif
	
	executable 	= run_py.sh

	transfer_input_files = myscript.py

	log         = job.log
	output      = job.out
	error       = job.error

	+JobDurationCategory = "Medium"

	request_cpus 	= 1 
	request_memory 	= 2GB
	request_disk 	= 2GB

	queue 1

## Other Considerations

This guide mainly focuses on the nuts and bolts of running Python, but it's important 
to remember that additional files needed for your jobs (input data, setting files, etc.) 
need to be transferred with the job as well. See our [Introduction to Data Management 
on OSG](https://portal.osg-htc.org/documentation/htc_workloads/managing_data/overview/) for details on the different ways to deliver inputs to your jobs. 

When you've prepared a real job submission, make sure to run a test job and then check 
the `log` file for disk and memory usage; if you're using significantly more or less 
than what you requested, make sure you adjust your requests. 

## Getting Help

For assistance or questions, please email the OSG Research Facilitation
team  at [support@osg-htc.org](mailto:support@osg-htc.org) or visit the [help desk and community forums](http://support.opensciencegrid.org).

[module-guide]: ../../../htc_workloads/using_software/software-request/
[data-intro]: ../../../htc_workloads/managing_data/osgconnect-storage/
