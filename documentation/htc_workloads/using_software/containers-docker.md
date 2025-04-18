---
ospool:
  path: htc_workloads/using_software/containers-docker.md
---

Containers - Docker
===================

The OSPool is using Apptainer/Singularity to execute containers. It is recommended
that if you are building your own custom container, you use the 
[Apptainer/Singularity image defintion format](../containers-singularity). 
However, Docker images can also be used on the OSPool and a Docker image is 
sometimes the more appropriate choice. For example:

 * There is an existing image on Docker Hub
 * You found a Dockerfile which meets your requirements
 * You have Docker installed on your own machine and want to 
   develop the code/image locally before using it on the OSPool

This guide contains examples on how to build your own Docker image, how
to convert a Docker image to Apptainer/Singularity, and how to import a
Docker image from the Docker Hub.

## Building Your Own Docker Image

If you already have an existing Docker container image, skip
to [Preparing Docker Containers for HTCondor Jobs](#preparing-docker-containers-for-htcondor-jobs). Otherwise, continue reading. 

!!! warning "Warning: Build Docker containers on your local machine"

    The steps below must be run **on your local computer**, not on the OSPool Access Point.  
    Docker is not available on the Access Point, and these commands will fail if run there.

### Identify Components

What software do you want to install? Make sure that you have either the source 
code or a command that can be used to install it through Linux (like `apt-get` or 
`yum`). You'll also need to choose a "base" container, on which to add your particular 
software or tools.

### Building

There are two main methods for generating your own container image. 

1. Editing the `Dockerfile`
2. Editing the default image using local Docker

We recommend the first option, as it is more reproducible, but the second option 
can be useful for troubleshooting or especially tricky installs.

#### Dockerfile

Create a folder on your computer and inside it, create a blank text file 
called `Dockerfile`.  

The first line of this file should include the keyword `FROM` and then 
the name of a Docker image (from Docker Hub) you want 
to use as your starting point. If using the OSG's Ubuntu 22.04 image that 
would look like this: 

	FROM hub.opensciencegrid.org/htc/ubuntu:22.04

Then, for each command you want to run to add libraries or software, use the 
keyword `RUN` and then the command. Sometimes it makes sense to string 
commands together using the `&&` operator and line breaks `\`, like so:

	RUN apt-get update -y && \
	    apt-get install -y build-essentials

or

	RUN wget https://cran.r-project.org/src/base/R-3/R-3.6.0.tar.gz && \
	    tar -xzf R-3.6.0.tar.gz && \
	    cd R-3.6.0 && \
	    ./configure && \
	    make && \
	    make install

Typically it's good to group together commands installing the same kind of thing 
(system libraries, or software packages, or an installation process) under one `RUN` command, 
and then have multiple `RUN` commands, one for each of the different type of 
software or package you're installing. 

(For all the possible Dockerfile keywords, see the [Docker Documentation](https://docs.docker.com/engine/reference/builder/))

Once your Dockerfile is ready, you can "build" the container image by running this command: 

    $ docker build -t namespace/repository_name .

Note that the naming convention for Docker images is your Docker Hub username and then 
a name you choose for that particular container image. So if my Docker Hub username 
is `alice` and I created an image with the NCBI `blast` tool, I might use this name: 

    $ docker build -t alice/NCBI-blast .

#### Editing an Image Interactively

You can also build an image interactively, without a Dockerfile. First, get 
the desired starting image from Docker Hub. Again, we will
look at the OSG Ubuntu 22.04 image. 

    $ docker pull hub.opensciencegrid.org/htc/ubuntu:22.04

We will run the image in a docker interactive session

    $ docker run -it --name <docker_session_name_here> hub.opensciencegrid.org/htc/ubuntu:22.04 /bin/bash

Giving the session a name is important because it will make it easier to 
reattach the session later and commit the changes later on. Now you will 
be greeted by a new command line prompt that will look something like this

    [root@740b9db736a1 /]#

You can now install the software that you need through the default package 
manager, in this case `apt-get`. 

    [root@740b9db736a1 /]# apt-get install build-essentials

Once you have installed all the software, you simply `exit`

    [root@740b9db736a1 /]# exit

Now you can commit the changes to the image and give it a name: 

    docker commit <docker_session_name_here> namespace/repository_name

You can also use the session's hash as found in the command prompt (`740b9db736a1` 
in the above example) in place of the docker session name. 


## Preparing Docker Containers for HTCondor Jobs

Once you have a Docker container image, whether created by you or found 
on DockerHub, you should convert it to the "sif" image format for 
the best experience on the OSpool. 

### Convert Docker containers on Docker Hub or online

!!! note "Note: Complete on the AP"

    The steps below should be completed on the OSPool Access Point. As we will
    prepare our Docker container to be converted to an Apptainer container and ran
    on the OSPool infrastructure. 

If the Docker container you want to use is online, on a site like Docker Hub, you can 
log in to your Access Point and run a single command to convert it to a `.sif` image: 

	$ apptainer build my-container.sif docker://owner/repository:tag

Where the path at the end of the command is customized to be the container image
you want to use. 

### Convert Docker containers on your computer

!!! note "Note: On Your Computer"

    The steps below should be completed on the OSPool Access Point. As we will
    prepare our Docker container to be converted to an Apptainer container and ran
    on the OSPool infrastructure. 

If you have built a Docker image on your own host, you can save it as a 
tar file and then convert it to an Apptainer/Singularity SIF image. First
find the image id:

    $ docker image list
    REPOSITORY              IMAGE ID
    awesome/science         f1e7972c55bc

Using the image id, save the image to a tar file:

    $ docker save f1e7972c55bc -o my-container.tar

!!! note "Note: On The Access Point"

    The steps below should be completed on the OSPool Access Point. As we will
    prepare our Docker container to be converted to an Apptainer container and ran
    on the OSPool infrastructure. 

Transfer `my-container.tar` to the OSPool access point, and use
Apptainer to convert it to a SIF image:

    $ apptainer build my-container.sif docker-archive://my-container.tar

## Using Containers in HTCondor Jobs

After converting the Docker image to a sif format, you can use the 
image in your job as described in the
[Apptainer/Singularity Guide](../containers-singularity#using-singularity-or-apptainer-images-in-an-htcondor-job). 

## Special Cases

### ENTRYPOINT and ENV

Two options that can be used in the Dockerfile to set the environment or 
default command are `ENTRYPOINT` and `ENV`. Unfortunately, both of these 
aspects of the Docker container are deleted when it is converted to a 
Singularity image in the Open Science Pool.

### Apptainer/Singularity Environment

One approach for setting up the environment for an image which will
be converted to Apptainer/Singularity, is to put a file under
`/.singularity.d/env/`. These files will be sourced when the container
get instantiated. For example, if you have Conda environment, add this
to the end of your Dockerfile:

    # set up environment for when using the container, this is for when 
    # we invoke the container with Apptainer/Singularity
    RUN mkdir -p /.singularity.d/env && \
        echo ". /opt/conda/etc/profile.d/conda.sh" >>/.singularity.d/env/91-environment.sh && \
        echo "conda activate" >>/.singularity.d/env/91-environment.sh


[osg-containers]: ../../../htc_workloads/using_software/available-containers-list/
