---
ospool:
  path: htc_workloads/using_software/software-overview.md
---

Using Software on the Open Science Pool 
====================================

## Overview of Software Options

There are several options available for managing the software needs of your work within the Open Science Pool (OSPool). For most cases, it will be advantageous for you to install the software needed for your jobs. This not only gives you the greatest control over your computing environment, but will also make your jobs more distributable, allowing you to run jobs at more locations.
* The OSPool can support most popular, open source software that fit the distributed 
high throughput computing model. 
* We do not have or support most commercial software 
due to licensing issues. 

Here we review options, and provide links to additonal information, for using software 
installed by users, software available as precompiled binaries or via containers.

**More details and instructions on installing software from source code, precompiled binaries/prebuilt executables, and on creating and using containers can be found on the [OSPool documentation website](https://portal.osg-htc.org/documentation/), under the "Software" section.**

## Use Precompiled Binaries and Prebuilt Executables

Some software may be available as a precompiled binary or prebuilt executable 
which provides a quick and easy way to run a program without the need for installation 
from source code. Binaries and executables are software files that are ready to 
run as is, however binaries should always be tested beforehand. There are several 
important considerations for using precompiled binaries on the OSPool: 

1) only binary files compiled against a Linux operating system are suitable 
for use on the OSPool, 
2) some softwares have system and hardware dependencies that must 
be met in order to run properly, and 
3) the available binaries may not have been 
compiled with the feaures or configuration needed for your work.

## Install Software from Source Code

When installing software from source code on an OSPool Access Point, your software will be specifically compiled against 
the **Red Hat Enterprise Linux (RHEL) 9 operating system** used on these nodes. In most cases, subsequent 
jobs that use this software will also need to run on a RHEL 9 OS, which can be specified by the 
`requirements` attribute of your HTCondor submit files as described in the guide linked above. 

## Use Docker and Apptainer Containers

Container systems provide users with customizable and reproducable computing and software 
environments. The Open Science Pool is compatible with both Apptainer and Docker containers - the 
latter will be converted to a Apptainer image and added to the OSG container image 
repository. 

For more information about Docker, please see:

* [Docker Home Page](https://www.docker.com/)

and Apptainer/Singularity, please see:

 * [Apptainer Home Page](https://apptainer.org/)
 
Apptainer/ Singularity has become the preferred containerization method in scientific computing. This <a href="//www.youtube.com/embed/DA87Ba2dpNM">talk</a> is an example of how  containers are used in scientific computing. 

Users can choose from a set of [pre-defined containers already available within OSG](../../../htc_workloads/using_software/available-containers-list/), 
or can use published or custom made containers. 

For jobs submitted to the OSPool, it does not matter whether you provide a Docker or
Apptainer/Singularity image. Either is compatible with our system and can be
used with little to no modification. Determining factors on when to
use Apptainer/Singularity images over Docker images include if an image already
exists and if you have
experience building images in one for format and not the other. 

When using a container for your jobs, the container image is
automatically started up when HTCondor matches your job to a slot. The
executable provided in the submit script will be run within the context
of the container image, having access to software and libraries that
were installed to the image, as if they were already on the server where
the job is running. <b>Job executables do not need to run any
commands to start the container.</b>


## Request Help with Installing Software

If you believe none of the options described above are applicable for your software, send an email to
[support@osg-htc.org](mailto:support@osg-htc.org) that describes:
1. the software name, version, and/or website with download and install instructions
2. what science each job does, using the software
3. what you've tried so far (if anything), and what indications of issues you've experienced

We will do our best to help you create a portable installation.

## Additional Resources

**Watch this video from the 2021 OSG Virtual School** for more information about using software on OSG:

[<img src="/images/Software_Video_Thumbnail.png" width="500">](https://www.youtube.com/embed/xUeIQbVXOMQ)
