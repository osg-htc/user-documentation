---
path:
  path: htc_workloads/containers/available-containers-list.md
---

Existing OSPool-Supported Containers 
====================================

This is list of commonly used containers in the Open Science Pool. These can be used
directly in your jobs or as base images if you want to define your own. Please
see the pages on [Apptainer containers][container-apptainer] and [Docker containers][container-docker]
for detailed instructions on how to use containers and/or have Docker containers added to the OSPool's approved list.

Also note that this list is not complete. There are many images under
`/cvmfs/singularity.opensciencegrid.org/` which are either project specific
or not described well enough to make this list.


## Base


??? info "Debian 12 (htc/debian:12)"
    Debian 12 base image
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/htc/debian:12</span><br>
    <br>[Project Website](https://debian.org/)<br>
    <br>[Container Definition](https://github.com/osg-htc/htc-images)<br>

??? info "EL 7 (htc/centos:7)"
    Enterprise Linux (CentOS) 7 base image
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/htc/centos:7</span><br>
    <br>[Project Website](https://www.centos.org/)<br>
    <br>[Container Definition](https://github.com/opensciencegrid/osgvo-el7)<br>

??? info "Rocky 8 (htc/rocky:8)"
    Rocky Linux 8 base image
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/htc/rocky:8</span><br>
    <br>[Project Website](https://rockylinux.org/)<br>
    <br>[Container Definition](https://github.com/osg-htc/htc-images)<br>

??? info "Rocky 8 / CUDA 11.0.3 (htc/rocky:8-cuda-11.0.3)"
    Rocky Linux 8 / CUDA 11.0.3 image
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/htc/rocky:8-cuda-11.0.3</span><br>
    <br>[Project Website](https://rockylinux.org/)<br>
    <br>[Container Definition](https://github.com/osg-htc/htc-images)<br>

??? info "Rocky 9 (htc/rocky:9)"
    Rocky Linux 9 base image
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/htc/rocky:9</span><br>
    <br>[Project Website](https://rockylinux.org/)<br>
    <br>[Container Definition](https://github.com/osg-htc/htc-images)<br>

??? info "Ubuntu 20.04 (htc/ubuntu:20.04)"
    Ubuntu 20.04 (Focal) base image
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/htc/ubuntu:20.04</span><br>
    <br>[Project Website](https://www.ubuntu.com)<br>
    <br>[Container Definition](https://github.com/osg-htc/htc-images)<br>

??? info "Ubuntu 22.04 (htc/ubuntu:22.04)"
    Ubuntu 22.04 (Focal) base image
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/htc/ubuntu:22.04</span><br>
    <br>[Project Website](https://www.ubuntu.com)<br>
    <br>[Container Definition](https://github.com/osg-htc/htc-images)<br>

## AI


??? info "Tensorflow 2.15 (htc/tensorflow:2.15)"
    Tensorflow image from the Tensorflow project, with OSG additions
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/htc/tensorflow:2.15</span><br>
    <br>[Project Website](https://www.tensorflow.org/)<br>
    <br>[Container Definition](https://github.com/osg-htc/htc-images)<br>

??? info "scikit-learn:1.3.2 (htc/scikit-learn:1.3)"
    scikit-learn, configured for execution on OSG
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/htc/scikit-learn:1.3</span><br>
    <br>[Project Website](https://scikit-learn.org/)<br>
    <br>[Container Definition](https://github.com/osg-htc/htc-images)<br>

## Languages


??? info "Julia (opensciencegrid/osgvo-julia)"
    Ubuntu based image with Julia
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-julia:1.0.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-julia:1.5.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-julia:1.7.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-julia:latest</span><br>
    <br>[Project Website](https://julialang.org/)<br>
    <br>[Container Definition](https://github.com/opensciencegrid/osgvo-julia)<br>

??? info "Julia (m8zeng/julia-packages)"
    Ubuntu based image with Julia
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/m8zeng/julia-packages:latest</span><br>
    <br>[Project Website](https://julialang.org/)<br>
    <br>[Container Definition](https://github.com/opensciencegrid/osgvo-julia)<br>

??? info "Matlab Runtime (opensciencegrid/osgvo-matlab-runtime)"
    This is the Matlab runtime component you can use to execute compiled Matlab codes
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-matlab-runtime:R2018b</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-matlab-runtime:R2019a</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-matlab-runtime:R2019b</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-matlab-runtime:R2020a</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-matlab-runtime:R2020b</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-matlab-runtime:R2021b</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-matlab-runtime:R2022b</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-matlab-runtime:R2023a</span><br>
    <br>[Project Website](https://www.mathworks.com/products/compiler/matlab-runtime.html)<br>
    <br>[Container Definition](https://github.com/opensciencegrid/osgvo-matlab-runtime)<br>

??? info "Matlab Runtime (htc/matlab-runtime:R2023a)"
    This is the Matlab runtime component you can use to execute compiled Matlab codes
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/htc/matlab-runtime:R2023a</span><br>
    <br>[Project Website](https://www.mathworks.com/products/compiler/matlab-runtime.html)<br>
    <br>[Container Definition](https://github.com/opensciencegrid/osgvo-matlab-runtime)<br>

??? info "R (opensciencegrid/osgvo-r)"
    Example for building R images
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-r:3.5.0</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-r:4.0.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-r:latest</span><br>
    <br>[Project Website](https://www.r-project.org/)<br>
    <br>[Container Definition](https://github.com/opensciencegrid/osgvo-r)<br>

??? info "R (clkwisconsin/spacetimer)"
    Example for building R images
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/clkwisconsin/spacetimer:latest</span><br>
    <br>[Project Website](https://www.r-project.org/)<br>
    <br>[Container Definition](https://github.com/opensciencegrid/osgvo-r)<br>

## Project


??? info "XENONnT (opensciencegrid/osgvo-xenon)"
    Base software environment for XENONnT, including Python 3.6 and data management tools
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2020.11.06</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2020.11.25</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2020.12.21</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2020.12.23</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.01.04</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.01.06</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.01.11</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.04.18</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.05.04</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.06.25</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.07.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.08.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.08.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.10.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.10.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.10.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.10.4</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.10.5</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.11.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.11.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.11.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.11.4</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.11.5</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.11.6</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.12.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.12.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2021.12.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.01.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.01.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.01.4</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.02.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.02.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.02.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.02.4</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.03.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.03.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.03.4</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.03.5</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.04.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.04.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.04.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.05.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.05.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.06.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.06.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.06.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.06.4</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.06.5</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.06.6</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.07.27</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.09.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:2022.11.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:add_latex</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:gpu</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:latex_test3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:py38</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:stable</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:straxen_0-13-1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:straxen_v100</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:switch_deployhq_user</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-xenon:upgrade-boost</span><br>
    <br>[Project Website](http://www.xenon1t.org/)<br>
    <br>[Container Definition](https://github.com/XENONnT/base_environment)<br>

??? info "XENONnT (xenonnt/base-environment)"
    Base software environment for XENONnT, including Python 3.6 and data management tools
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2020.11.06</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2020.11.25</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2020.12.21</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2020.12.23</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2020.12.24</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.01.04</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.01.06</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.01.11</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.04.18</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.05.04</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.06.25</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.07.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.08.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.08.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.10.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.10.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.10.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.10.4</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.10.5</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.11.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.11.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.11.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.11.4</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.11.5</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.11.6</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.12.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.12.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2021.12.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.01.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.01.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.01.4</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.02.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.02.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.02.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.02.4</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.03.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.03.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.03.4</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.03.5</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.04.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.04.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.04.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.05.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.05.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.06.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.06.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.06.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.06.4</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.06.5</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.06.6</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.07.27</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.09.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:2022.11.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:add_latex</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:gpu</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:latex_test3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:py38</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:stable</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:straxen_v100</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:switch_deployhq_user</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:testing</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/base-environment:upgrade-boost</span><br>
    <br>[Project Website](http://www.xenon1t.org/)<br>
    <br>[Container Definition](https://github.com/XENONnT/base_environment)<br>

??? info "XENONnT (xenonnt/osg_dev)"
    Base software environment for XENONnT, including Python 3.6 and data management tools
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/xenonnt/osg_dev:latest</span><br>
    <br>[Project Website](http://www.xenon1t.org/)<br>
    <br>[Container Definition](https://github.com/XENONnT/base_environment)<br>

## Tools


??? info "FreeSurfer (opensciencegrid/osgvo-freesurfer)"
    A software package for the analysis and visualization of structural and functional neuroimaging data from cross-sectional or longitudinal studies
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-freesurfer:6.0.0</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-freesurfer:6.0.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-freesurfer:7.0.0</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-freesurfer:7.1.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-freesurfer:latest</span><br>
    <br>[Project Website](https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferWiki)<br>
    <br>[Container Definition](https://github.com/opensciencegrid/osgvo-freesurfer)<br>

??? info "GROMACS (opensciencegrid/osgvo-gromacs)"
    A versatile package to perform molecular dynamics, i.e. simulate the Newtonian equations of motion for systems with hundreds to millions of particles.
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-gromacs:2018.4</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-gromacs:2020.2</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-gromacs:latest</span><br>
    <br>[Project Website](http://www.gromacs.org/)<br>
    <br>[Container Definition](https://github.com/opensciencegrid/osgvo-gromacs)<br>

??? info "GROMACS GPU (opensciencegrid/osgvo-gromacs-gpu)"
    A versatile package to perform molecular dynamics, i.e. simulate the Newtonian equations of motion for systems with hundreds to millions of particles. This is a GPU enabled version.
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-gromacs-gpu:latest</span><br>
    <br>[Project Website](http://www.gromacs.org/)<br>
    <br>[Container Definition](https://github.com/opensciencegrid/osgvo-gromacs-gpu)<br>

??? info "Gromacs 2023.4 (htc/gromacs:2023.4)"
    Gromacs 2023.4 for use on OSG
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/htc/gromacs:2023.4</span><br>
    <br>[Project Website](https://www.gromacs.org/)<br>
    <br>[Container Definition](https://github.com/osg-htc/htc-images)<br>

??? info "Gromacs 2024.2 (htc/gromacs:2024.2)"
    Gromacs 2024.2 for use on OSG
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/htc/gromacs:2024.2</span><br>
    <br>[Project Website](https://www.gromacs.org/)<br>
    <br>[Container Definition](https://github.com/osg-htc/htc-images)<br>

??? info "Quantum Espresso (opensciencegrid/osgvo-quantum-espresso)"
    A suite for first-principles electronic-structure calculations and materials modeling
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-quantum-espresso:6.6</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-quantum-espresso:6.8</span><br>
    <br>[Project Website](https://www.quantum-espresso.org/)<br>
    <br>[Container Definition](https://github.com/opensciencegrid/osgvo-quantum-espresso)<br>

??? info "RASPA2 (opensciencegrid/osgvo-raspa2)"
    General purpose classical simulation package. It can be used for the simulation of molecules in gases, fluids, zeolites, aluminosilicates, metal-organic frameworks, carbon nanotubes and external fields.
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-raspa2:2.0.41</span><br>
    <br>[Project Website](https://github.com/iraspa/RASPA2)<br>
    <br>[Container Definition](https://github.com/opensciencegrid/osgvo-raspa2)<br>

??? info "TensorFlow (opensciencegrid/tensorflow)"
    TensorFlow image (CPU only)
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/tensorflow:2.3</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/tensorflow:latest</span><br>
    <br>[Project Website](https://www.tensorflow.org/)<br>
    <br>[Container Definition](https://github.com/opensciencegrid/osgvo-tensorflow)<br>

??? info "TensorFlow (rynge/tensorflow-cowsay)"
    TensorFlow image (CPU only)
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/rynge/tensorflow-cowsay:latest</span><br>
    <br>[Project Website](https://www.tensorflow.org/)<br>
    <br>[Container Definition](https://github.com/opensciencegrid/osgvo-tensorflow)<br>

??? info "TensorFlow (jiahe58/tensorflow)"
    TensorFlow image (CPU only)
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/jiahe58/tensorflow:latest</span><br>
    <br>[Project Website](https://www.tensorflow.org/)<br>
    <br>[Container Definition](https://github.com/opensciencegrid/osgvo-tensorflow)<br>

??? info "TensorFlow GPU (opensciencegrid/tensorflow-gpu)"
    TensorFlow image with GPU support
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/tensorflow-gpu:2.2-cuda-10.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/tensorflow-gpu:2.3-cuda-10.1</span><br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/opensciencegrid/tensorflow-gpu:latest</span><br>
    <br>[Project Website](https://www.tensorflow.org/)<br>
    <br>[Container Definition](https://github.com/opensciencegrid/osgvo-tensorflow-gpu)<br>

??? info "TensorFlow GPU (efajardo/astroflow)"
    TensorFlow image with GPU support
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/efajardo/astroflow:latest</span><br>
    <br>[Project Website](https://www.tensorflow.org/)<br>
    <br>[Container Definition](https://github.com/opensciencegrid/osgvo-tensorflow-gpu)<br>

??? info "TensorFlow GPU (ssrujanaa/catsanddogs)"
    TensorFlow image with GPU support
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/ssrujanaa/catsanddogs:latest</span><br>
    <br>[Project Website](https://www.tensorflow.org/)<br>
    <br>[Container Definition](https://github.com/opensciencegrid/osgvo-tensorflow-gpu)<br>

??? info "TensorFlow GPU (weiphy/skopt)"
    TensorFlow image with GPU support
    <br>
    <br>
    CVMFS Locations:<br>
    <span style="white-space: nowrap">/cvmfs/singularity.opensciencegrid.org/weiphy/skopt:latest</span><br>
    <br>[Project Website](https://www.tensorflow.org/)<br>
    <br>[Container Definition](https://github.com/opensciencegrid/osgvo-tensorflow-gpu)<br>


[container-apptainer]: ../../../htc_workloads/using_software/containers-singularity/
[container-docker]: ../../../htc_workloads/using_software/containers-docker/

