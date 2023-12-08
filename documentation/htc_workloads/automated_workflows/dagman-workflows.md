---
ospool:
  path: htc_workloads/automated_workflows/dagman-workflows.md
---

# Submit Workflows with HTCondor's DAGMan 

## Overview

In this guide:

* [Introduction](#introduction)
* [What is DAGMan?](#what-is-dagman)
* [The Basics of the DAG Input File](#the-basics-of-the-dag-input-file)
* [Running a DAG Workflow](#running-a-dag-workflow)
* [A Simple DAG Example](#a-simple-dag-example)
* [DAGMan Features](#dagman-features)

## Introduction

If your work requires jobs that run in a particular sequence, you may benefit 
from a workflow tool that submits and monitors jobs for you in the correct 
order. HTCondor has a built in utility called "DAGMan" that automates the
job submission of such a workflow.

This talk (originally presented at HTCondor Week 2020) gives a good introduction
to DAGMan and its most useful features: 

<a href="https://www.youtube.com/watch?v=1MvVHxRs7iU">
<img alt="DAGMan Talk" src="https://raw.githubusercontent.com/OSGConnect/connectbook/master/images/dagman-talk-screenshot.png" width="360" height="204">
</a>

DAGMan can be a powerful tool for creating large and complex HTCondor workflows, 
but it can also be difficult for new users to get started with. 
The goal of this guide is to introduce users to the basics of a DAG workflow and 
how to implement it using HTCondor's DAGMan.

For the full details on various DAGMan features, see the HTCondor manual pages: 

* [DAGMan Manual Page](https://htcondor.readthedocs.io/en/latest/automated-workflows/index.html)

## What is DAGMan?

DAGMan is short for "DAG Manager", and is a utility built into HTCondor for automatically running a workflow (DAG) of jobs, 
where the results of an earlier job are required for running a later job. 
DAG itself is an acronym for [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph), a concept from the mathematic field of graph theory.

1. Graph: a collection of points ("nodes" or "vertices") connected to each other by lines ("edges").
2. Directed: the edges between nodes have direction, that is, each edge begins on one node and ends on a different node.
3. Acyclic: the graph does not have a cycle - or loop - where the graph returns to a previous node.

By using a directed acyclic graph, we can guarantee that the workflow has a defined 'start' and 'end'. 
In DAGMan, each node in the workflow corresponds to a job submission (i.e., `condor_submit`).
Each edge in the workflow corresponds to a set of files that are the output of one job submission and 
For convenience, we refer to such a workflow and the files necessary to execute it as "the DAG".

## The Basics of the DAG Input File

The purpose of the DAG input file (typically `.dag`) is to instruct DAGMan on the structure of the workflow you want to run. 
Additional instructions can be included in the DAG input file about how to manage the job submissions, rerun jobs (nodes), 
or to run pre- or post-processing scripts.

In general, the structure of the `.dag` input file consists of one instruction per line, with each line starting with a keyword defining the type of instruction. 

### 1. Defining the DAG jobs

To define a DAG job, we begin a new line with `JOB` then provide the name, the submit file, and any additional options. The syntax is

```
JOB JobName JobSubmitFile [additional options]
```

where you need to replace `JobName` with the name you would like the DAG job to have, and `JobSubmitFile` with the name or path of the corresponding submit file. Both `JobName` and `JobSubmitFile` need to be specified.

**Every node in your workflow must have a `JOB` entry in the `.dag` input file.** While there are other instructions that can reference a particular node, they will only work if the node in question has a corresponding `JOB` entry. 

### 2. Defining the connections

To define the relationship between DAG jobs in a workflow, we begin a new line with `PARENT` then the name of the first DAG job, followed by `CHILD` and the name of the second DAG job. That is, the `PARENT` DAG job must complete successfully before DAGMan will submit the `CHILD` DAG job. In fact, you can define such relationship for many DAG jobs (nodes) at the same time. Thus, the syntax is

```
PARENT p1 [p2 ...] CHILD c1 [c2 ...]
```

where you replace `p#` with the `JobName` for each parent DAG job, and `c#` with the `JobName` for each child DAG job. The child DAG jobs will only be submitted if all of the parent DAG jobs are completed successfully. Each `JobName` you provide must have a corresponding `JOB` entry elsewhere in the `.dag` input file.

> Technically, DAGMan does not require that each DAG job in a workflow is connected to another DAG job.
> This allows you to submit many unrelated DAG jobs at one time using DAGMan.

Note that in defining the `PARENT`-`CHILD` relationship, there is no definition of *how* they are related. 
Effectively, DAGMan does not need to know *why* the `PARENT` DAG jobs must complete successfully in order to submit the `CHILD` DAG jobs. 
There can be many reasons why you might want to execute the DAG jobs in this order, although the most common reason
is that the `PARENT` DAG jobs create files that are required by the `CHILD` DAG jobs. 
In that case, it is up to you to organize the submit files of those DAG jobs in such a way that the output of the `PARENT` DAG jobs 
can be used as the input of the `CHILD` DAG jobs. 
In the [DAGMan Features](#dagman-features) section, we will discuss tools that can assist you with this endeavor.

## Running a DAG Workflow

### 1. Submitting the DAG



### 2. Monitoring the DAG



## A Simple DAG Example

Consider the case of two HTCondor jobs that use the submit files `A.sub` and `B.sub`.
Let's say that `A.sub` generates an output file that `B.sub` will analyze.
To run this workflow manually, we would

  1. Submit the first HTCondor job with `condor_submit A.sub`.
  2. Wait for the first HTCondor job to complete successfully.
  3. Submit the second HTCondor job with `condor_submit B.sub`.

If the first HTCondor job using `A.sub` is fairly short, then manually running this workflow is not a big deal. 
But if the first HTCondor job takes a long time to complete (maybe takes several hours to run, or has to wait for special resources), 
this can be very inconvenient.
Instead, we can use DAGMan to automatically submit `B.sub` once the first HTCondor job using `A.sub` has completed successfully.

In this scenario, our workflow could be described as a DAG consisting of two nodes (`A.sub` and `B.sub`) connected by a single edge (`output.csv`).
In order to use DAGMan to run this workflow, we need to define the nodes and how they are connected. Thus we need to construct a `.dag` input file as described [above](#the-basics-of-the-dag-input-file) that defines the `A.sub` -> `B.sub` workflow. Let's call it `simple.dag`. 

### 1. The minimal DAG input file

At minimum, the contents of the `simple.dag` input file are

```
# simple.dag

# Define the DAG jobs
JOB A A.sub
JOB B B.sub

# Define the connections
PARENT A CHILD B
```

First, we used the syntax for [defining a DAG job](#1-defining-the-dag-jobs) to tell DAGMan that it will need to run two DAG jobs. 
To submit the DAG job labeled `A`, DAGMan should use the submit file `A.sub`, while to submit the DAG job labeled `B`, 
DAGMan should use the submit file `B.sub`. 
(While there is no requirement that the submit file for DAG job `A` to be called `A.sub`, it is convenient to use a consistent naming scheme.)

Second, since `B.sub` requires an output file generated by `A.sub`, we tell DAGMan that `A` is the `PARENT` while `B` is the `CHILD`, using the syntax for [defining connections between DAG jobs](#2-defining-the-connections).

### 2. The submit files

Now let's define simple examples of the submit files `A.sub` and `B.sub`.

#### Job A

First, the submit file `A.sub` uses the executable `A.sh`, which will generate the file called `output.txt`.
We have explicitly told HTCondor to transfer back this file by using the `transfer_output_files` command.

```
# A.sub

executable = A.sh

log = A.log
output = A.out
error = A.err

transfer_output_files = output.txt

+JobDurationCategory = "Medium"

request_cpus = 1
request_memory = 1GB
request_disk = 1GB

queue
```

The executable file simply saves the hostname of the machine running the script:

```
#!/bin/bash

# A.sh
hostname > output.txt
```

#### Job B

Second, the submit file `B.sub` uses the executable `B.sh` to print a message using the contents of the `output.txt` file generated by `A.sh`.
We have explicitly told HTCondor to transfer `output.txt` as an *input* file for this job, using the `transfer_input_files` command. 
The message we want will be printed to `B.out`.

```
# B.sub

executable = B.sh

log = B.log
output = B.out
error = B.err

transfer_input_files = output.txt

+JobDurationCategory = "Medium"

request_cpus = 1
request_memory = 1GB
request_disk = 1GB

queue
```

The executable file contains the command for printing the desired message:

```
#!/bin/bash

# B.sh
echo "The previous job was executed on the following machine:"
cat output.txt
```

### 3. The file structure

Using the above input file, DAGMan is expecting that the submit files `A.sub` and `B.sub` are in the same directory as `simple.dag`.
The submit files in turn are expecting `A.sh` and `B.sh` be in the same directory as `A.sub` and `B.sub`.
Thus, we have the following structure:

```
simple_DAG/
|-- A.sh
|-- A.sub
|-- B.sh
|-- B.sub
|-- simple.dag
```

It is possible to organize each job into its own directory, but for now we will use this simple, flat organization.

### 4. Running the simple DAG

To run the DAG workflow described by `simple.dag`, we use the HTCondor command `condor_submit_dag`:

```
condor_submit_dag simple.dag
```

The DAGMan utility will then parse the input file and generate an assortment of related files that it will use for monitoring and managing your workflow.
Here is the output of running the above command:





## DAGMan Features

### 1. Pre- and post-processing for DAG jobs

### 2. Rescue DAGs

