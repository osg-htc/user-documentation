---
ospool:
    path: htc_workloads/containers/docker.md
---

## Create/Register a Docker Container Image 

This guide is meant to accompany the instructions for using containers 
in the OSPool.  You can use your own custom container to run jobs in the 
OSPool, and we assume that those containers are built using Docker.  This 
guide describes how to create your own Docker container "image" (the blueprint for 
the container) and how to convert it to a Singularity/Apptainer image. 

For an overview and how to execute images , please see
[Containers - Overview][overview]

## Use an Existing Docker Container

If a Docker container image already exists with the software you need, it can 
be converted to a Singularity/Apptainer image format using this command: 

	apptainer build my-custom-image.sif docker://owner/repo:tag

Replace `my-custom-image.sif` with a name of your choice (keeping the `.sif` suffix) 
and the `docker://owner/repo:tag` can be the identifier for any publicly hosted 
Docker image, including those on `quay.io` and the NVIDIA NGC Catalog `nvcr.io`. 

Once the `.sif` file is created, you can copy it to a data directory, 
test it on the Access Point,
and use it in your HTCondor jobs as described in
[Containers - Overview][overview].

## Build a Docker Container

### Install Docker and Get a Docker Hub Account

You'll need a Docker Hub account in order to download Docker and share your 
Docker container images: [DockerHub](https://hub.docker.com/)

Install Docker Desktop to your computer using the appropriate version for your 
operating system. **Note that OSPool does not provide any Docker build hosts.**

**Note that Apple silicon Macs has to be configured specifically to produce
x86_64 Docker containers.**

### Identify Components

What software do you want to install? Make sure that you have either the source 
code or a command that can be used to install it through Linux (like `apt-get` or 
`yum`). 

You'll also need to choose a "base" container, on which to add your particular 
software or tools. 

We suggest using one of the following as base containers - these have common
packages installed as well as some OSPool specifics like OSDF:

```
hub.opensciencegrid.org/htc/debian:12
hub.opensciencegrid.org/htc/rocky:9
hub.opensciencegrid.org/htc/ubuntu:24.04
```

### Build the Image

There are two ways to build a Docker container image: 

1. Edit a `Dockerfile` and use it to produce an image
2. Edit a default image using local Docker

We recommend the first option, as it is more reproducible, but the second option 
can be useful for troubleshooting or especially tricky installs. 

#### Option 1: Editing the `Dockerfile`

Create a folder on your computer and inside it, create a blank text file 
called `Dockerfile`.  

The first line of this file should include the keyword `FROM` and then 
the name of a Docker image (from Docker Hub) you want 
to use as your starting point. If using the OSG's Ubuntu 24.04 image that 
would look like this: 

	FROM hub.opensciencegrid.org/htc/ubuntu:24.04

Then, for each command you want to run to add libraries or software, use the 
keyword `RUN` and then the command. Sometimes it makes sense to string 
commands together using the `&&` operator and line breaks `\`, like so:

	RUN apt-get update && \
	    apt-get install -yy build-essentials

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


#### Option 2: Editing the default image using local Docker

You can also build an image interactively, without a Dockerfile. First, get 
the desired starting image from Docker Hub. Again, we will
look at the OSG Ubuntu 24.04 image. 

    $ docker pull hub.opensciencegrid.org/htc/ubuntu:24.04

We will run the image in a docker interactive session

    $ docker run -it --name <docker_session_name_here> hub.opensciencegrid.org/htc/ubuntu:24.04 /bin/bash

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

### Upload Docker Container to Docker Hub

Once your container is complete and tagged, it should appear in the list of local Docker 
container images, which you can see by running:

	$ docker images

From there, you need to put it in Docker Hub, which can be done via the `docker push` 
command:

	$ docker push namespace/repository_name

From here, if you're planning to use this container in OSG, see the 
[first section of this guide][overview]. 

### ENTRYPOINT and ENV

Two options that can be used in the Dockerfile to set the environment or 
default command are `ENTRYPOINT` and `ENV`. Unfortunately, both of these 
aspects of the Docker container are deleted when it is converted to a 
Singularity image in the Open Science Pool.

[overview]: ../overview
