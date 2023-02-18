---
path:
    path: htc_workloads/containers/containers-singularity.md
---

# Apptainer/Singularity Container Images

This guide is meant to accompany the instructions for using containers
under the PATh Facility. You can use your own custom container to run
jobs. This guide describes how to create your
own Apptainer/Singularity container "image" (the blueprint for the container).

For an overview and how to execute images on OSG, please see
[Containers - Overview][osg-containers]

## Identify Components

What software do you want to install? Make sure that you have either the source
code or a command that can be used to install it through Linux (like `apt-get` or
`yum`).

You'll also need to choose a "base" container, on which to add your particular
software or tools.
See the available containers on Docker Hub here:
[OSG Docker Containers](https://hub.docker.com/u/opensciencegrid)
The best candidates for you will be containers that have "osgvo" in the name.

### Editing the Build Spec

Create a folder on your computer and inside it, create a blank text file
called `image.def`.

The first lines of this file should include where to get the base image
from. If using the OSG's Ubuntu 20.04 image that  would look like this:

    Bootstrap: docker
    From: opensciencegrid/osgvo-ubuntu-20.04:latest

Then there is a section called `%post` where you put the additional
commands to make the image just like you need it. For example:

    %post
        apt-get update -y
        apt-get install -y \
                build-essential \
                cmake \
                g++ \
                r-base-dev

        R -e "install.packages('cowsay', dependencies=TRUE, repos='http://cran.rstudio.com/')"

See the [Apptainer documentation](https://apptainer.org/user-docs/master/definition_files.html)
for a full reference on how to specify build specs. Note that the `%runscript`
section is ignored when the container is executed under the PATh Facility.

The final `image.def` looks like:

    Bootstrap: docker
    From: opensciencegrid/osgvo-ubuntu-20.04:latest

    %post
        apt-get update -y
        apt-get install -y \
                build-essential \
                cmake \
                g++ \
                r-base-dev

        R -e "install.packages('cowsay', dependencies=TRUE, repos='http://cran.rstudio.com/')"

Once your build spec is ready, you can "build" the container image by running this command:

    $ apptainer build my-container.sif image.def

Once the image is built, you can copy it to a data directory, test it on the Access Point,
and use it in your HTCondor jobs. This is all described in
[Containers - Overview][osg-containers].

[osg-containers]: ../../../htc_workloads/using_software/containers/

