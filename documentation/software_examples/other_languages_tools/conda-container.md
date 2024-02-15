---
ospool:
  path: software_examples/other_languages_tools/conda-container.md
---

# Conda with Containers

The Anaconda/Miniconda distribution of Python is a common tool for installing and managing Python-based software and other tools. 

There are two ways of using Conda on the OSPool: with [a tarball](../conda-tarball/), or via a
custom Apptainer/Singularity container. Either works well, but the container
solution might be better if your Conda environment contains non-Python tools.

## Overview
When should you use Miniconda as an installation method in OSG?

 * Your software has specific conda-centric installation instructions.
 * The above is true and the software has a lot of dependencies.
 * You mainly use Python to do your work.

Notes on terminology:

- **conda** is a Python package manager and package ecosystem that exists in parallel with `pip` and [PyPI](https://pypi.org/).
- **Miniconda** is a slim Python distribution, containing the minimum amount of packages necessary for a Python installation that can use conda.
- **Anaconda** is a pre-built scientific Python distribution based on Miniconda that has many useful scientific packages pre-installed.

<p style="color:blue;">To create the smallest, most portable Python installation possible, we recommend starting with Miniconda and installing only the packages you actually require.</p>

To use a Miniconda installation for your jobs, create an Apptainer/Singularity definition file and
build it (general instructions [here](../../../htc_workloads/using_software/containers-singularity/)).

## Apptainer/Singularity Definition File

The definition file tells Apptainer/Singularity how the container should be built,
and what the environment setup should take place when the container is instantiated.
In the following example, the container is based on Ubuntu 22.04. A few base
operating system tools are installed, then Miniconda, followed by a set of 
`conda` commands to define the Conda environment. The `%environment` is used
to ensure jobs are getting the environment activated before the job runs. To build
your own custom image, start by modifing the `conda install` line to include
the packages you need.


    Bootstrap: docker
    From: ubuntu:22.04
    
    %environment
        # set up environment for when using the container
        . /opt/conda/etc/profile.d/conda.sh
        conda activate
    
    %post
        # base os
        apt-get update -y
        apt-get install -y build-essential wget
    
        # install miniconda
        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
        bash Miniconda3-latest-Linux-x86_64.sh -b -f -p /opt/conda
        rm Miniconda3-latest-Linux-x86_64.sh
    
        # install conda components - add the packages you need here
        . /opt/conda/etc/profile.d/conda.sh
        conda activate
        conda install -y -c conda-forge numpy cowpy
        conda update --all 


The next step is to build the image. Run:

    $ apptainer build my-container.sif image.def

You can explore the container locally to make sure it works as expected with the shell subcommand:

    $ apptainer shell my-container.sif

This example will give you an interactive shell. You can explore the
container and test your code with your own inputs from your `/home`
directory, which is automatically mounted (but note - $HOME will not be
available to your jobs later). Once you are down exploring, exit the
container by running `exit` or with `CTRL+D`

It is important to use the correct transfer mechanism to get the 
image to your job. Please make sure you use [OSDF](../../../htc_workloads/managing_data/osdf/)
and version your container in the filename. For example:

    $ cp my-container.sif /ospool/protected/<username>/my-container-v1.sif

### Submit Jobs

An example submit file could look like: 

```
# File Name: conda_submission.sub

# specify the newly built image
+SingularityImage = "osdf:///ospool/protected/<username>/my-container-v1.sif"

# Specify your executable (single binary or a script that runs several
#  commands) and arguments to be passed to jobs. 
#  $(Process) will be a integer number for each job, starting with "0"
#  and increasing for the relevant number of jobs.
executable = science.py
arguments = $(Process)

# Specify the name of the log, standard error, and standard output (or "screen output") files.

log = science_with_conda.log
error = science_with_conda.err
output = science_with_conda.out

# Transfer any file needed for our job to complete. 
transfer_input_files = 

# Specify Job duration category as "Medium" (expected runtime <10 hr) or "Long" (expected runtime <20 hr). 
+JobDurationCategory = “Medium”

# Tell HTCondor requirements your job needs, 
# what amount of compute resources each job will need on the computer where it runs.
requirements = 
request_cpus = 1
request_memory = 1GB
request_disk = 5GB

# Tell HTCondor to run 1 instance of our job:
queue 1
```

      
## Specifying Exact Dependency Versions

An important part of improving reproducibility and consistency between runs is to ensure that you use the correct/expected versions of your dependencies.

When you run a command like `conda install numpy` `conda` tries to install the most recent version of `numpy` For example, `numpy` version `1.22.3` was released on Mar 7, 2022. To install exactly this version of numpy, you would run `conda install numpy=1.22.3` (the same works for `pip` if you replace `=` with `==`). We recommend installing with an explicit version to make sure you have exactly the version of a package that you want. This is often called “pinning” or “locking” the version of the package.

If you want a record of what is installed in your environment, or want to reproduce your environment on another computer, conda can create a file, usually called `environment.yml`, that describes the exact versions of all of the packages you have installed in an environment. An example `environment.yml` file:

    channels:
      - conda-forge
      - defaults
    dependencies:
      - cowpy
      - numpy=1.25.0

To use the `environment.yml` in the build, modify the image definition to copy the file, and
then replace the `conda install` with a `conda env create`. Also note that it is good style
to name the environment. We call it `science` in this example:

    Bootstrap: docker
    From: ubuntu:22.04
    
    %files
        environment.yml
    
    %environment
        # set up environment for when using the container
        . /opt/conda/etc/profile.d/conda.sh
        conda activate science
    
    %post
        # base os
        apt-get update -y
        apt-get install -y build-essential wget
    
        # install miniconda
        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
        bash Miniconda3-latest-Linux-x86_64.sh -b -f -p /opt/conda
        rm Miniconda3-latest-Linux-x86_64.sh
    
        # install conda components - add the packages you need here
        . /opt/conda/etc/profile.d/conda.sh
        conda activate
        conda env create -n science -f environment.yml
        conda update --all 

If you use a source control system like `git`, we recommend checking your `environment.yml` file into source control and making sure to recreate it when you make changes to your environment. Putting your environment under source control gives you a way to track how it changes along with your own code.

More information on conda environments can be found in [their documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#).
