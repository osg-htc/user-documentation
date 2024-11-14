---
ospool:
  path: htc_workloads/using_software/containers-singularity.md
---

# Containers - Apptainer/Singularity

This guide is meant to accompany the instructions for using containers
in the Open Science Pool. You can use your own custom container to run
jobs in the Open Science Pool. This guide describes how to create your
own Apptainer/Singularity container "image" (the blueprint for the container).

## Do You Need to Build a Container? 

If there is an existing Docker container or Apptainer/Singularity container with 
the software you need, you can proceed with using these options to submit a job. 
* [See OSPool-provided containers here](../available-containers-list/)
* [Using an existing Docker container](../containers-docker/)
* [Using an existing Apptainer/Singularity container](#using-singularity-or-apptainer-images-in-an-htcondor-job)

If you can't find a good option among existing containers, you may need to 
build your own. See [this section of the guide](#building-your-own-apptainer-singularity-container) for more information. 

## OSG-Provided Apptainer/Singularity Images

The OSG Team maintains a set of images that are already in the OSG
Apptainer/Singularity repository. [A list of ready-to-use containers can be found on this page](../available-containers-list/).

If the software you need isn't already supported in a listed container,
you can create your own container or use any container image in Docker Hub.

How to explore these containers is shown [below](#exploring-apptainer-singularity-images-on-the-access-points). 

## Building Your Own Apptainer/Singularity Container

### Identify Components

What software do you want to install? Make sure that you have either the source
code or a command that can be used to install it through Linux (like `apt-get` or
`yum`).

You'll also need to choose a "base" container, on which to add your particular
software or tools. We recommend using one of the OSG's published containers
as your starting point. See the available containers on Docker Hub here:
[OSG Docker Containers](https://hub.docker.com/u/opensciencegrid)
The best candidates for you will be containers that have "osgvo" in the name.

### Apptainer/Singularity Build

If you are building an image for the first time, the temporary cache directory of the apptainer image needs to be defined. The following commands define the cache location of the apptainer image to be built. Please run the commands in the terminal of your access point.

```
$mkdir $HOME/tmp
$export TMPDIR=$HOME/tmp
$export APPTAINER_TMPDIR=$HOME/tmp
$export APPTAINER_CACHEDIR=$HOME/tmp
```

To build a custom a Apptainer/Singularity image, create a folder on your access point. Inside it, create a blank text file
called `image.def`.

The first lines of this file should include where to get the base image
from. If using the OSG's Ubuntu 20.04 image that  would look like this:

    Bootstrap: docker
    From: hub.opensciencegrid.org/htc/ubuntu:22.04

Then there is a section called `%post` where you put the additional
commands to make the image just like you need it. For example:

    %post
    
        # system packages
        apt-get update -y
        apt-get install -y \
                build-essential \
                cmake \
                g++
    
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


Another good section to include is `%environment`. This is executed before
your job and lets the container configure the environment. Example:

    %environment
    
        # set up environment for when using the container
        . /opt/conda/etc/profile.d/conda.sh
        conda activate myenv


See the [Apptainer documentation](https://apptainer.org/user-docs/master/definition_files.html)
for a full reference on how to specify build specs. Note that the `%runscript`
section is ignored when the container is executed on OSG.

The final `image.def` looks like:

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


Once your build spec is ready, you can "build" the container image by running this command:

    $ apptainer build my-container.sif image.def

Once the image is built, test it on an OSG-managed access point,
and use it in your HTCondor jobs.

## Exploring Apptainer/Singularity Images on the Access Points

Just like it is important to test your codes and jobs at a small scale,
you should make sure that your Apptainer/Singularity container is working correctly before using it in jobs. One way
to test your container image on our system is to test it on
an OSG-managed access point. 

To do so, first log in to your assigned access point. Start an interactive session with the
Apptainer/Singularity "shell" mode. The recommended command line, similar
to how containers are started for jobs, is:

    apptainer shell my-container.sif

If you want to test an existing container produced by OSG Staff, use the 
full path provided in [this guide](../available-containers-list/). 

This example will give you an interactive shell. You can explore the
container and test your code with your own inputs from your `/home`
directory, which is automatically mounted (but note - $HOME will not be
available to your jobs later). Once you are down exploring, exit the
container by running `exit` or with `CTRL+D`. 

## Using Singularity or Apptainer Images in an HTCondor Job

Once you have a ".sif" container image file with all your needed software, 
you can use this file as part of an HTCondor job. 

### Upload the Container Image to the OSDF

The image will be resused for
each job, and thus the preferred transfer method is [OSDF](../../managing_data/osdf/).
Store the .sif file under your personal data area on your access point
(see table [here](../../managing_data/osdf/#where-to-put-your-files)). 

### Use the Container in an HTCondor Job

Once the image is placed in your OSDF space, you can use an OSDF 
url directly in the `+SingularityImage` attribute. Note that you can not
use shell variable expansion in the submit file - be sure to replace the
username with your actual OSPool username. Example:

    +SingularityImage = "osdf:///ospool/apXX/data/USERNAME/my-custom-image-v1.sif"

    <other usual submit file lines>
    queue

**Be aware that OSDF aggressively caches the image based on file naming.
If you need to do quick changes, please use versioning of the .sif file
so that the caches see a "new" name.** In this example, replacing
`my-custom-image-v1.sif` with new content will probably mean that some
nodes get the old version and some nodes the new version. Prevent this
by creating a new file named with v2.

## Common Issues

<details>
<summary>FATAL: kernel too old </summary>
<br>
If you get a *FATAL: kernel too old* error, it means that the glibc version in the
image is too new for the kernel on the host. You can work around this problem by
specifying the minimum host kernel. For example, if you want to run the Ubuntu 18.04
image, specfy a minimum host kernel of 3.10.0, formatted as 31000
(major * 10000 + minor * 100 + patch):
<br>
  <code>Requirements = HAS_SINGULARITY == True && OSG_HOST_KERNEL_VERSION >= 31000</code>
<br>
</details>






[osg-containers]: ../../../htc_workloads/using_software/available-containers-list/
