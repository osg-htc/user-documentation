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
Effectively, DAGMan does not need to know the reason *why* the `PARENT` DAG jobs must complete successfully in order to submit the `CHILD` DAG jobs. 
There can be many reasons why you might want to execute the DAG jobs in this order, although the most common reason
is that the `PARENT` DAG jobs create files that are required by the `CHILD` DAG jobs. 
In that case, it is up to you to organize the submit files of those DAG jobs in such a way that the output of the `PARENT` DAG jobs 
can be used as the input of the `CHILD` DAG jobs. 
In the [DAGMan Features](#dagman-features) section, we will discuss tools that can assist you with this endeavor.

## Running a DAG Workflow

### 1. Submitting the DAG

Because the DAG workflow represents a special type of job, a special command is used to submit it. To submit the DAG workflow, use 

```
condor_submit_dag input.dag
```

where `input.dag` is the name of your DAG input file containing the `JOB` and `PARENT`-`CHILD` definitions for your workflow.
This will create and submit a "DAGMan job" that will in turn be responsible for submitting and monitoring the job nodes described in your DAG input file.

A set of files is created for every DAG submission, and the output of the `condor_submit_dag` lists the files with a brief description.
For the above submit command, the output will look like:

```
-----------------------------------------------------------------------
File for submitting this DAG to HTCondor           : input.dag.condor.sub
Log of DAGMan debugging messages                 : input.dag.dagman.out
Log of HTCondor library output                     : input.dag.lib.out
Log of HTCondor library error messages             : input.dag.lib.err
Log of the life of condor_dagman itself          : input.dag.dagman.log

Submitting job(s).
1 job(s) submitted to cluster ######.
-----------------------------------------------------------------------
```

### 2. Monitoring the DAG

The DAGMan job is actually a "scheduler" job (described by `input.dag.condor.sub`) and the status and progress of the DAGMan job is saved to `input.dag.dagman.out`.
Using `condor_q` or `condor_watch_q`, the DAGMan job will be under the name `input.dag+######`, where `######` is the Cluster ID of the DAGMan scheduler job. 
Each job submitted by DAGMan, however, will be assigned a separate Cluster ID.

For a more detailed status display, you can use

```
condor_q -dag -nobatch
```

For even more details about the execution of the DAG workflow, you can examine the contents of the `input.dag.dagman.out` file. 
The file contains timestamped log information of the execution and status of nodes in the DAG, along with statistics.
As the DAG progresses, it will also create the files `input.dag.metrics` and `input.dag.nodes.log`, where the metrics file contains the current statistics of the DAG and the log file is an aggregate of the individual nodes' user log files.

### 3. Removing the DAG

To remove the DAG, you need to `condor_rm` the Cluster ID corresponding to the DAGMan scheduler job. 
This will also remove the jobs that the DAGMan scheduler job submitted as part of executing the DAG workflow.
A removed DAG is almost always marked as a failed DAG, and as such will generate a rescue DAG (see below).


## DAGMan Features

### 1. Pre- and post-processing for DAG jobs



### 2. Rescue DAGs

