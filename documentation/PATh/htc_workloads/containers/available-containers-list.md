---
path:
    path: htc_workloads/containers/available-containers-list.md
---

Predefined Containers 
=====================


This is list of commonly used containers. These can be used
directly in your jobs or as base images if you want to define your own. Please
see the pages on [container overview][container-intro] and [creating containers][container-howto]
for detailed instructions on how to use containers and/or have Docker containers added to the OSPool's approved list.

Also note that this list is not complete. There are many images under
`/cvmfs/singularity.opensciencegrid.org/` which are either project specific
or not described well enough to make this list.


## Base

| **Name** | **CVMFS Locations** | **Description** |
|:---------|:--------------------|:----------------|
| <span style="white-space: nowrap">EL 6</span> | <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el6:latest</span> | Enterprise Linux (CentOS) 6 base image<br>[Project Website](https://www.centos.org/)<br>[Container Definition](https://github.com/opensciencegrid/osgvo-el6) |
| <span style="white-space: nowrap">EL 7</span> | <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest</span> | Enterprise Linux (CentOS) 7 base image<br>[Project Website](https://www.centos.org/)<br>[Container Definition](https://github.com/opensciencegrid/osgvo-el7) |
| <span style="white-space: nowrap">EL 8</span> | <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el8:latest</span> | Enterprise Linux (CentOS) 8 base image<br>[Project Website](https://www.centos.org/)<br>[Container Definition](https://github.com/opensciencegrid/osgvo-el8) |
| <span style="white-space: nowrap">Ubuntu 16.04</span> | <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-ubuntu-xenial:latest</span> | Ubuntu 16.04 (Xenial) base image<br>[Project Website](https://www.ubuntu.com)<br>[Container Definition](https://github.com/opensciencegrid/osgvo-ubuntu-xenial) |
| <span style="white-space: nowrap">Ubuntu 18.04</span> | <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-ubuntu-18.04:latest</span> | Ubuntu 18.04 (Bionic) base image<br>[Project Website](https://www.ubuntu.com)<br>[Container Definition](https://github.com/opensciencegrid/osgvo-ubuntu-18.04) |
| <span style="white-space: nowrap">Ubuntu 20.04</span> | <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-ubuntu-20.04:latest</span> | Ubuntu 20.04 (Focal) base image<br>[Project Website](https://www.ubuntu.com)<br>[Container Definition](https://github.com/opensciencegrid/osgvo-ubuntu-20.04) |

## Languages

| **Name** | **CVMFS Locations** | **Description** |
|:---------|:--------------------|:----------------|
| <span style="white-space: nowrap">Julia</span> | <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-julia:latest</span> | Ubuntu based image with Julia<br>[Project Website](https://julialang.org/)<br>[Container Definition](https://github.com/opensciencegrid/osgvo-julia) |
| <span style="white-space: nowrap">Matlab Runtime</span> | <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-matlab-runtime:R2018b</span><br><span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-matlab-runtime:R2019a</span><br><span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-matlab-runtime:R2019b</span><br><span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-matlab-runtime:R2020a</span><br><span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-matlab-runtime:R2020b</span> | This is the Matlab runtime component you can use to execute compiled Matlab codes<br>[Project Website](https://www.mathworks.com/products/compiler/matlab-runtime.html)<br>[Container Definition](https://github.com/opensciencegrid/osgvo-matlab-runtime) |
| <span style="white-space: nowrap">R</span> | <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-r:3.5.0</span><br><span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-r:4.0.2</span> | Example for building R images<br>[Project Website](https://www.r-project.org/)<br>[Container Definition](https://github.com/opensciencegrid/osgvo-r) |

## Project

| **Name** | **CVMFS Locations** | **Description** |
|:---------|:--------------------|:----------------|
| <span style="white-space: nowrap">XENONnT</span> | <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2020.11.06</span><br><span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2020.11.25</span><br><span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:development</span><br><span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:latest</span><br><span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:py38</span> | Base software environment for XENONnT, including Python 3.6 and data management tools<br>[Project Website](http://www.xenon1t.org/)<br>[Container Definition](https://github.com/XENONnT/base_environment) |
| <span style="white-space: nowrap">XENONnT</span> | <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/osg_dev:latest</span> | Base software environment for XENONnT, including Python 3.6 and data management tools<br>[Project Website](http://www.xenon1t.org/)<br>[Container Definition](https://github.com/XENONnT/base_environment) |
| <span style="white-space: nowrap">XENONnT</span> | <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2020.11.06</span><br><span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2020.11.25</span><br><span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:development</span><br><span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:latest</span><br><span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:py38</span> | Base software environment for XENONnT, including Python 3.6 and data management tools<br>[Project Website](http://www.xenon1t.org/)<br>[Container Definition](https://github.com/XENONnT/base_environment) |
| <span style="white-space: nowrap">XENONnT</span> | <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/montecarlo:development</span><br><span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/montecarlo:latest</span> | Base software environment for XENONnT, including Python 3.6 and data management tools<br>[Project Website](http://www.xenon1t.org/)<br>[Container Definition](https://github.com/XENONnT/base_environment) |

## Tools

| **Name** | **CVMFS Locations** | **Description** |
|:---------|:--------------------|:----------------|
| <span style="white-space: nowrap">FreeSurfer</span> | <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-freesurfer:6.0.0</span><br><span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-freesurfer:6.0.1</span><br><span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-freesurfer:7.0.0</span> | A software package for the analysis and visualization of structural and functional neuroimaging data from cross-sectional or longitudinal studies<br>[Project Website](https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferWiki)<br>[Container Definition](https://github.com/opensciencegrid/osgvo-freesurfer) |
| <span style="white-space: nowrap">GROMACS</span> | <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-gromacs:latest</span> | A versatile package to perform molecular dynamics, i.e. simulate the Newtonian equations of motion for systems with hundreds to millions of particles.<br>[Project Website](http://www.gromacs.org/)<br>[Container Definition](https://github.com/opensciencegrid/osgvo-gromacs) |
| <span style="white-space: nowrap">GROMACS GPU</span> | <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-gromacs-gpu:latest</span> | A versatile package to perform molecular dynamics, i.e. simulate the Newtonian equations of motion for systems with hundreds to millions of particles. This is a GPU enabled version.<br>[Project Website](http://www.gromacs.org/)<br>[Container Definition](https://github.com/opensciencegrid/osgvo-gromacs-gpu) |
| <span style="white-space: nowrap">Quantum Espresso</span> | <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-quantum-espresso:6.6</span> | A suite for first-principles electronic-structure calculations and materials modeling<br>[Project Website](https://www.quantum-espresso.org/)<br>[Container Definition](https://github.com/opensciencegrid/osgvo-quantum-espresso) |
| <span style="white-space: nowrap">TensorFlow</span> | <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/tensorflow:2.3</span><br><span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/tensorflow:latest</span> | TensorFlow image (CPU only)<br>[Project Website](https://www.tensorflow.org/)<br>[Container Definition](https://github.com/opensciencegrid/osgvo-tensorflow) |
| <span style="white-space: nowrap">TensorFlow GPU</span> | <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/tensorflow-gpu:2.2-cuda-10.1</span><br><span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/tensorflow-gpu:2.3-cuda-10.1</span><br><span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/tensorflow-gpu:latest</span> | TensorFlow image with GPU support<br>[Project Website](https://www.tensorflow.org/)<br>[Container Definition](https://github.com/opensciencegrid/osgvo-tensorflow-gpu) |


