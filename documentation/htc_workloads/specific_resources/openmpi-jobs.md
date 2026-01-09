---
ospool:
  path: htc_workloads/specific_resource/openmpi-jobs.md
---

OpenMPI Jobs 
====================================

Even though the Open Science Pool is a high throughput computing system, sometimes
there is a need to run small OpenMPI based jobs. OSG has limited support for
this, as long as the core count is small (4 is known to work well, 8 and 16 
becomes more difficult due to the limited number of resources).

## Find an MPI-based Container

To get started, first compile your code using an OpenMPI container. You can create your own OpenMPI container or use the one that is available on DockerHub. Use your desired Docker [image](https://registry.hub.docker.com/r/mfisherman/openmpi/tags)and do `apptainer pull`. More information about using *apptainer pull* can be found [here](https://apptainer.org/docs/user/main/cli/apptainer_pull.html). 

## Compile the Code

To compile your code, start running the container first. Then run `mpicc` to compile the code: 

    $ apptainer shell /ospool/ap40/data/username/openmpi.sif
    Apptainer> mpicc -o hello hello.c 

The `hello.c` is an example hello world code that can be executed using multiple processors. The code is given below:

```
#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
        MPI_Init(NULL, NULL);
        int world_size;
        MPI_Comm_size(MPI_COMM_WORLD, &world_size);
        int world_rank;
        MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
        char processor_name[MPI_MAX_PROCESSOR_NAME];
        int name_len;
        MPI_Get_processor_name(processor_name, &name_len);
        printf("Hello world from processor %s, rank %d out of %d processors\n", processor_name, world_rank, world_size);
        MPI_Finalize();
}
```

After compiling the code, you can test the executable locally using `mpiexec`:

    Apptainer> mpiexec -n 4 hello
    Hello world from processor ap40.uw.osg-htc.org, rank 0 out of 4 processors
    Hello world from processor ap40.uw.osg-htc.org, rank 1 out of 4 processors
    Hello world from processor ap40.uw.osg-htc.org, rank 2 out of 4 processors
    Hello world from processor ap40.uw.osg-htc.org, rank 3 out of 4 processors

When testing is done be sure to exit from the apptainer shell using `exit`. 

## Run a Job Using the MPI Container and Compiled Code

The next step is to run your code as a job on the Open Science Pool. For this, first create a `wrapper.sh`. Example:

    #!/bin/sh
    
    set -e
    
    mpiexec -n 4 hello


Then, a job submit file:


    container_image = osdf:///ospool/ap40/data/username/openmpi.sif

    executable = wrapper.sh
    transfer_input_files = hello

    +JobDurationCategory = "Medium"
    
    request_cpus = 4
    request_memory = 1 GB

    output = job.out.$(Cluster).$(Process)
    error = job.error.$(Cluster).$(Process)
    log = job.log.$(Cluster).$(Process)

    queue 1

Note how the executable is the `wrapper.sh` script, and that the real executable `hello` is
transferred using the `transfer_input_files` mechanism.

Please make sure that the number of cores specified in the submit file via
`request_cpus` match the `-n` argument in the `wrapper.sh` file. 
