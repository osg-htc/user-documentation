---
ospool:
  path: htc_workloads/containers/apptainer.md
---

This guide describes how to create your
own Apptainer/Singularity container "image" (the blueprint for the container).

For an overview and how to execute images on the OSPool, please see
[Containers - Overview][overview]

## Identify Components

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

## Editing the Build Spec

Create a folder in your home directory and inside it, create a blank text file
called `image.def`.

The first lines of this file should include where to get the base image
from.  Then there is a section called `%post` where you put the additional
commands to make the image just like you need it. For example:

    Bootstrap: docker
    From: hub.opensciencegrid.org/htc/ubuntu:22.04

    %post

        # system packages
        apt-get update -y
        apt-get install -y \
                build-essential \
                wget

        # install miniconda
        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
        bash Miniconda3-latest-Linux-x86_64.sh -b -f -p /opt/conda
        rm Miniconda3-latest-Linux-x86_64.sh

        # install conda components - add the packages you need here
        . /opt/conda/etc/profile.d/conda.sh
        conda create -y -n "myenv" python=3.9
        conda activate myenv
        conda update --all
        conda install -y -n "myenv" -c conda-forge pytorch

    %environment

        # set up environment for when using the container
        . /opt/conda/etc/profile.d/conda.sh
        conda activate myenv

    From: hub.opensciencegrid.org/htc/ubuntu:24.04


See the [Apptainer documentation](https://apptainer.org/user-docs/master/definition_files.html)
for a full reference on how to specify build specs. Note that the `%runscript`
section is ignored when the container is executed in the OSPool.

Once your build spec is ready, you can "build" the container image by running this command:

    $ apptainer build my-container.sif image.def

Once the image is built, you can copy it to a data directory, test it on the Access Point,
and use it in your HTCondor jobs. This is all described in
[Containers - Overview][overview].

[overview]: ../overview
