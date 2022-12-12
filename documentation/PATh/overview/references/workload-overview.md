---
path:
   path: overview/references/workload-overview.md
---

# PATh Workload Overview

To get the most of your PATh Credit Allocation your computational workload will need to be updated to a High 
Throughput Computing (HTC) model. The goal of adopting the HTC model is to minimize the resource usage of each job you
run, and running 1000s of those jobs in parallel across all of our resources. 

## HTC Workload Composition

### Ensemble

An Ensemble is the largest component of an HTC workload, containing a set of [tasks](#task), and a set of 
[shared files](#shared-files).

#### Ensemble Attributes

###### Runs

The number of times you would like to run this ensemble, where running an ensemble entails running 
the entire set of tasks. 

###### Tasks

A set of tasks working towards a common goal. All tasks in this set have access to the 
Ensembles [Shared Files](#shared-files).

###### Shared Files

A set of files that can be accessed the [tasks](#task) in this ensemble.

### Task

Tasks are the smallest component of the HTC workload, representing a set of jobs with unique inputs, and similar
resource requirements. In the case of simulations, the unique inputs might involve randomness in the jobs themselves. 

#### Task Attributes

##### Unique Inputs/Simulations

The number of unique inputs, translates directly to number of tasks. Typically, will be the size of the input space or in the case of simulations the
number of simulations to run. 

##### CPU Cores

The number of cores needed to run one job

##### GPUs

The number of A100 GPUs needed to run one job

##### Memory ( in GB )

The amount of memory in gigabytes needed to run one job

##### Disk  ( in GB )

The amount of disk in gigabytes needed to run one job

##### Walltime ( in hours )

The amount of time in hours required to run one job

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

![](../../assets/PATh/workload-overview/Workload_Composition_Overview.png)

### Ensemble - Sanitize Data

Since the data only needs to be sanitized once it has been put in its own ensemble. To maximize its ability to 
be run in parallel the researcher has split the pipeline in two parts: Standardization, which can be run in parallel and 
Outlier Removal, which needs to be run with the entire dataset. 

#### Shared File - Un-sanitized Data

Un-standardized tabular data that has 10,000 rows

#### Task - Standardize Data

The researcher has decided to break up their dataset into 100 groups of 100 rows so that they can run 100 standardization
jobs in parallel.

![](../../assets/PATh/workload-overview/Workload_Composition_Standardize.png)

#### Task - Remove Outliers

There is no option to run outlier removal with independent inputs so this is run once with the entire dataset. 

### Ensemble - Run Model 

The researcher has 3 different prediction models they would like to run, so they have decided to create one general ensemble
of tasks and run it 3 times with each prediction model in parallel.

#### Shared File - Dataset 

The dataset sanitized in the previous ensemble

#### Task - Train Model

![](../../assets/PATh/workload-overview/Workload_Composition_Train_Model.png)

Step one for them is to decide what of the 16 sets of parameters is the best, which they will use 100-fold Cross-Validation
to decide. Since each of iteration of the cross validation can happen in parallel they have decided to split this into 
**1,600 jobs**, where each job is one iteration of Cross-Validation using one of the 16 sets of inputs. 

### Task - Test Model

Using the set of parameters that performed the best in training, the researcher will now test on their testing data.
