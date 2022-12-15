---
path:
   path: overview/references/workload-overview.md
---

# PATh Workload Overview

To get the most of your PATh Credit Allocation your computational workload will need to be updated to a High 
Throughput Computing (HTC) model. The result of adopting the HTC model is a workload that can be run and managed on 
distributed resources in parallel. 

## HTC Workload Composition

### Ensemble

An Ensemble is the largest component of an HTC workload, containing a set of [tasks](#task), and a set of 
[shared files](#shared-files).

#### Ensemble Attributes

###### Runs

The number of times you would like to run this ensemble, where running an ensemble entails running 
the entire set of tasks. 

###### Tasks

A set of tasks working towards a common goal. All tasks in this set have access to this
Ensembles [Shared Files](#shared-files).

###### Shared Files

A set of files that can be accessed the [tasks](#task) in this ensemble.

### Task

Tasks are the smallest component of the HTC workload and are grouped by function.
All tasks of the same function are expected to use similar resource requirements,
with their differences laying in input variables or randomness in the function itself.

#### Task Attributes

##### Unique Inputs/Simulations
 
Either the number of unique inputs into a task, or in the case of simulation, the number of simulations to run

##### CPU Cores

The number of cores needed to run one task

##### GPUs

The number of A100 GPUs needed to run one task

##### Memory ( in GB )

The amount of memory in gigabytes needed to run one task

##### Disk  ( in GB )

The amount of disk in gigabytes needed to run one task

##### Walltime ( in hours )

The amount of time in hours required to run one task

### Shared Files

Shared files are the files within an [Ensemble](#ensemble) that can be accessed by [tasks](#tasks).

Example: Data, Analysis Models, etc.

#### Shared File Attributes

##### Size ( in GB )

The size of the file in gigabytes

## Examples

To help provide an idea of how you might update your existing workload to the HTC model we have provided an example below. 

!!! tip

      The PATh team has alot of experience updating workloads to fit the HTC environment. Please contact support if you
      have any questions with the process!

      Contact PATh Support at [support@path-cc.io](mailto:support@path-cc.io)

## Example - Machine Learning

A researcher would like to clean their data, then train and test 3 different prediction models. Following the HTC workload
model they have set up the following composition.

![](../../assets/PATh/workload-overview/Ensemble-Overview.png)

### Ensemble - Remove Outliers

The goal of this Ensemble is to remove outliers from a dataset.
Since this involves context from the entire dataset, this ensemble we will run our task only once using the entire dataset as input. 

#### Shared File - Starting Data

Since our Task will be using the entire dataset we can consider it a Shared File. 

#### Shared File - Code

Since our Task will be using a Code file we will include that as a Shared File. 

#### Task - Remove Outliers

![](../../assets/PATh/workload-overview/Ensemble-Remove.png)

Each Task will use the code and data shared files, and run only once per Ensemble. 

### Ensemble - Standardize Data

The goal of this ensemble is to standardize our dataset. This includes updating the units, converting to a common language, and standardizing empty values. 

Since this can be done one row at time, we have organized the task in this ensemble to be run many times, using a segment
of the dataset as input to each run. 

#### Shared File - Code

Our only Shared File will be Code for this Ensemble as each task will only require a small segment of the data for each run.

#### Task - Standardize Data

![](../../assets/PATh/workload-overview/Ensemble-Standardize.png)

Using the HTC model we run this task many times with each run of the task using a small segment of data and the Shared Code
file. 

### Ensemble - Train/Select Model

The goal of this ensemble is to train a prediction model using a set of different hyper-parameters and select the best one. To 
achieve this goal we will use k-fold Cross-Validation as a method to select the best performing parameters. 

Additionally, since the researcher is looking to try out 3 different types of prediction model, we will be running
this ensemble 3 times, once for each type of model.

#### Shared File - Code

Since our Task will be using a Code file we will include that as a Shared File. 

#### Shared File - Data 

The dataset provided from our previous ensembles work. Since each task will be using this entire dataset we have included
it as a Shared File. 

#### Task - Train Model

![](../../assets/PATh/workload-overview/Ensemble-Train.png)

Each Task will use the code and data shared files, as well as one set of the hyper-parameters we wish to test. Each Task 
with a unique set of hyper-parameters will then be run k times to Cross-Validate.

The resulting number of runs will be *Number of Hyper-Parameter Sets* x *Cross-Validation Iterations (k)*.

### Ensemble - Test Model

The goal of this ensemble is to test our best performing models from the previous ensemble.

Since we ran the previous ensemble once for each of the 3 types of model we will run this ensemble 3 times as well. 

#### Shared File - Code

Since our Task will be using a Code file we will include that as a Shared File. 

#### Shared File - Data 

The dataset provided from our Standardize Data Ensemble. Since each task will be using this entire dataset we have included
it as a Shared File. 

#### Task - Test Model

![](../../assets/PATh/workload-overview/Ensemble-Test.png)

Each Task will use the code and data shared files, and run only once per Ensemble. 
