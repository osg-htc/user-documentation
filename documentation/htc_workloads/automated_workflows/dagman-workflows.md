---
ospool:
  path: htc_workloads/automated_workflows/dagman-workflows.md
---

# Submit Workflows with HTCondor's DAGMan 

## Overview

If your work requires jobs that run in a particular sequence, you may benefit 
from a workflow tool that submits and monitors jobs for you in the correct 
order. HTCondor has a built in utility called "DAGMan" that automates the
job submission of such a workflow.

This talk (originally presented at HTCondor Week 2020) gives a good overview of 
when to use DAGMan and its most useful features: 

<a href="https://www.youtube.com/watch?v=1MvVHxRs7iU">
<img alt="DAGMan Talk" src="https://raw.githubusercontent.com/OSGConnect/connectbook/master/images/dagman-talk-screenshot.png" width="360" height="204">
</a>

For full details on various DAGMan features, see the HTCondor manual page: 

* [DAGMan Manual Page](https://htcondor.readthedocs.io/en/latest/users-manual/dagman-workflows.html)

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
(Technically, DAGMan does not require that each node in a workflow is connected to another node.)

## A Simple DAG

Consider the case of two HTCondor jobs called Job A and Job B with corresponding submit files `A.sub` and `B.sub`
and executables `A.sh` and `B.sh`.
Job A generates an output file (`output.csv`) that Job B needs to analyze.
To run this workflow manually, we would

  1. Submit Job A with `condor_submit A.sub`.
  2. Wait for Job A to complete successfully.
  3. Submit Job B with `condor_submit B.sub`.

If Job A is fairly short, then manually running this workflow is not a big deal. 
But if Job A takes a long time to complete (maybe requires a lot of resources, or just takes several hours to run), this can be very inconvenient.
Instead, we can use DAGMan to automatically submit Job B once Job A completes successfully.

In this scenario, our workflow could be described as a DAG consisting of two nodes (Job A and Job B) connected by a single edge (`output.csv`).
In order to use DAGMan to run this workflow, we need to explicitly tell it what jobs to run and how they are connected. 

