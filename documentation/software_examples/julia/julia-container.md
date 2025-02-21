---
ospool:
  path: software_examples/other_languages_tools/julia-on-osg.md
---

Build and Use Julia in a Container
====================================

## Overview

[Containers](htc_workloads/using_software/software-overview/#use-docker-and-apptainer-containers) are an efficient way of ensuring a consistent software environment across different machines. This guide shows how to create a Julia software environment in containers for use on the OSPool.

## Building your Julia environment in a Container Image

### Identify Components

* A list of your Julia packages or the Project.toml and Manifest.toml
* A list of other dependencies, such as.
   * System packages/libraries
   * Git repositories

### Build Julia in an Apptainer image

To build an Apptainer image, follow [our guide](htc_workloads/using_software/containers-singularity/) and use one of the definition files listed below.

#### Example recipe: installing a list of packages

```
Bootstrap: docker
From: julia:1.10

%post
    # Install any needed system packages first
    apt-get update -y
    apt-get install -y wget \
            git \
            cmake \
            g++

    # Install Julia packages
    export JULIA_DEPOT_PATH="/opt/julia"
    julia -e 'using Pkg; Pkg.add(["DifferentialEquations", "DataFrames", "StaticArrays"]); Pkg.instantiate(); Pkg.precompile()'

%environment
    export JULIA_DEPOT_PATH=":/opt/julia"
```

#### Example recipe: installing from a Project.toml and Manifest.toml

```
Bootstrap: docker
From: julia:1.10

%files
   Project.toml /opt/julia/environments/v1.10/
   Manifest.toml /opt/julia/environments/v1.10/

%post
    # Install any needed system packages first
    apt-get update -y
    apt-get install -y wget \
            git \
            cmake \
            g++

    # Install Julia packages
    export JULIA_DEPOT_PATH="/opt/julia"
    julia -e 'using Pkg; Pkg.instantiate(); Pkg.precompile()'

%environment
    export JULIA_DEPOT_PATH=":/opt/julia"
```

### Build Julia in Docker

The OSPool is using Apptainer/Singularity to execute containers. It is recommended that if you are building your own custom container, you use the Apptainer/Singularity image defintion format. However, you can still build a Julia environment within a Docker image.

#### Example Dockerfile: installing a list of packages

```
FROM julia:1.10

RUN apt-get update -y
RUN apt-get install -y wget git cmake g++

ENV JULIA_DEPOT_PATH=":/opt/julia"

RUN julia -e 'using Pkg; Pkg.add(["DifferentialEquations", "DataFrames", "StaticArrays"]); Pkg.instantiate(); Pkg.precompile()'
```

#### Example Dockerfile: installing from a Project.toml or Manifest.toml

```
FROM julia:1.10

RUN apt-get update -y
RUN apt-get install -y wget git cmake g++

ENV JULIA_DEPOT_PATH=":/opt/julia"

ADD Project.toml Manifest.toml /opt/julia/environments/v1.10/

RUN julia -e 'using Pkg; Pkg.instantiate(); Pkg.precompile()'
```