---
ospool:
  path: htc_workloads/workload_planning/roadmap.md
---

Roadmap to HTC Workload Submission
====================================



## Overview

This guide lays out the steps needed to go from logging in to an OSG Access Point to running a full scale high throughput computing 
(HTC) workload on OSG's [Open Science Pool (OSPool)](https://opensciencegrid.org/about/open_science_pool/). 
The steps listed here apply to any new workload 
submission, whether you are a long-time OSG user or just getting 
started with your first workload, with helpful links to our documentation pages. 

This guide assumes that you have applied for an OSG Access Point account and 
have been approved after meeting with an OSG Research Computing Facilitator. 
If you don't yet have an account, you can apply for one [here](https://portal.osg-htc.org/application)
or [contact us](mailto:support@osg-htc.org) with any questions you have. 

Learning how to get started on the OSG does not need to end with this document or 
our guides! Learn about our training opportunities and personal facilitation support 
in the [Getting Help](#getting-help) section below. 

## 1. Introduction to the OSPool and OSG Resources

The OSG's Open Science Pool is best-suited for computing work that can be run as many, independent 
tasks, in an approach called "high throughput computing." For more information 
on what kind of work is a good fit for the OSG, 
see [Is the Open Science Pool for You?](../../../overview/account_setup/is-it-for-you/). 

Learn more about the services provided by the OSG in this video: 

<a href="https://www.youtube.com/watch?v=5FMAFxROGv0"><img alt="OSG Introduction" src="https://raw.githubusercontent.com/OSGConnect/connectbook/master/images/osg-intro-video-screenshot.png" width="360" height="204"></a>

<!-- Diagram/cartoon showing how jobs are distributed to multiple sites across the U.S.-->

## 2. Log on to an OSG Access Point

If you have not done so, apply for an account [here](https://portal.osg-htc.org/application). A Research Computing Facilitator will contact you within one business day to arrange a meeting to discuss your computational goals and to activate your account. 

Note that there are multiple classes of access points provided.
When your account was activated, you should have been told which 
access point your account belongs to:

<details>
<summary>Log In to "uw.osg-htc.org" Access Points (e.g., ap40.uw.osg-htc.org)</summary>
<br>
If your account is on the uw.osg-htc.org Access Points (e.g., accounts on ap40.uw.osg-htc.org), follow instructions in this guide for logging in:
<a href="https://portal.osg-htc.org/documentation/overview/account_setup/ap7-access/">Log In to uw.osg-htc.org Access Points</a>
</details>

<details>
<summary>Log In to "OSG Connect" Access Points (e.g., ap20.uc.osg-htc.org)</summary>
<br>
If your account is on the OSG Connect Access points (e.g., accounts on ap20.uc.osg-htc.org, ap21.uc.osg-htc.org), follow instructions in this guide for logging in:
<a href="https://portal.osg-htc.org/documentation/overview/account_setup/connect-access/">Log In to OSG Connect Access Points</a>
</details>


## 3. Learn to Submit HTCondor Jobs

Computational work is run on the OSPool by submitting it as “jobs” to the
HTCondor scheduler. Jobs submitted to HTCondor are then scheduled and
run on different resources that are part of the Open Science Pool.
Before submitting your own computational work, it is important to
understand how HTCondor job submission works. The following guides show
how to submit basic HTCondor jobs.

- [Overview: Submit OSPool Jobs using HTCondor](../../../htc_workloads/workload_planning/htcondor_job_submission/)

## 4. Test a First Job

After learning about the basics of HTCondor job submission, you will
need to generate your own HTCondor job -- including the software needed
by the job and the appropriate mechanism to handle the data. We
recommend doing this using a single test job. 

### Prepare your software

Software is an integral part of your HTC workflow.  Whether you’ve written it yourself, inherited it from your research group, or use common open-source packages, any required executables and libraries will need to be made available to your jobs if they are to run on the OSPool. 

Read through [this overview of Using Software](../../../htc_workloads/using_software/software-overview/) to help you determine the best way to provide your software.  We also have the following guides/tutorials for each major software portability approach:

- To **install your own software**, begin with the guide on [Compiling Software](../../../htc_workloads/using_software/compiling-applications/) and then complete the [Example Software Compilation tutorial](../../../htc_workloads/using_software/example-compilation/).
- To **use precompiled binaries**, try the example presented in the [AutoDock Vina tutorial](../../../software_examples/drug_discovery/tutorial-AutoDockVina/) and/or the [Julia tutorial](../../../software_examples/other_languages_tools/julia-on-osg/).
- To **use Apptainer/Singularity/Docker containers** for your jobs, see the [Create an Apptainer/Singularity Container Image](../../../htc_workloads/using_software/containers-singularity/)

Finally, here are some additional guides specific to some of the most common scripting languages and software tools used on OSG\*\*:

- [Python](../../../software_examples/python/manage-python-packages/)
- [R](../../../software_examples/r/tutorial-R/)
- [Machine Learning](../../../software_examples/machine_learning/tutorial-tensorflow-containers/)
- [BLAST](../../../software_examples/bioinformatics/tutorial-blast-split/)

\*\*This is not a complete list.  Feel free to search for your software in our [Knowledge base](https://support.opensciencegrid.org/support/solutions/). 

### Manage your data

The data for your jobs will need to be transferred to each job that runs in the OSPool, 
and HTCondor has built-in features for getting data to jobs. Our [Data Management](../../../htc_workloads/managing_data/overview/) guide
discussed the relevant approaches, when to use them, and where to stage data for each.
<!--
- Pick a tutorial?
-->

<!-- TODO: add guides
## Organize your files*
## Troubleshooting*
-->

### Assign the Appropriate Job Duration Category

Jobs running in the OSPool may be interrupted at any time, and will be re-run by HTCondor, unless a single execution of a job exceeds the allowed duration. Jobs expected to take longer than 10 hours will need to identify themselves as 'Long' according to our [Job Duration policies](../../../htc_workloads/workload_planning/jobdurationcategory/). Remember that jobs expected to take longer than 20 hours are not a good fit for the OSPool (see [Is the Open Science Pool for You?](../../../overview/account_setup/is-it-for-you/)) without implementing self-checkpointing (further below).

## 5. Scale Up

After you have a sample job running successfully, you’ll want to scale
up in one or two steps (first run several jobs, before running ALL of them). 
HTCondor has many useful features that make it easy to submit
multiple jobs with the same submit file.  

- [Easily submit multiple jobs](../../../htc_workloads/submitting_workloads/submit-multiple-jobs/)
- [Scaling up after success with test jobs](../../../htc_workloads/workload_planning/preparing-to-scale-up/) discusses how to test your jobs for duration, memory and disk usage, and the total amount of space you might need on the 

<!-- TODO: Making jobs resilient* -->

## 6. Special Use Cases

If you think any of the below applies to you, 
please [get in touch](mailto:support@osg-htc.org)
and our facilitation team will be happy to discuss your individual case. 

- Run sequential workflows of jobs: [Workflows with HTCondor's DAGMan](../../../htc_workloads/automated_workflows/dagman-workflows/)
- Implement self-checkpointing for long jobs: [HTCondor Checkpointing Guide](https://htcondor.readthedocs.io/en/latest/users-manual/self-checkpointing-applications.html)
- Build your own Apptainer container: [Create an Apptainer/Singularity Container Image](../../../htc_workloads/using_software/containers-singularity/)
- Submit more than 10,000 jobs at once: [FAQ, search for 'max_idle'](../../../overview/references/frequently-asked-questions/)
- Larger or speciality resource requests: 
	- GPUs: [GPU Jobs](../../../htc_workloads/specific_resource/gpu-jobs/)
	- Multiple CPUs: [Multicore Jobs](../../../htc_workloads/specific_resource/multicore-jobs/)
	- Large Memory: [Large Memory Jobs](../../../htc_workloads/specific_resource/large-memory-jobs/)

## Getting Help 

The OSG Facilitation team is here to help with questions and issues that come up as you work 
through these roadmap steps. We are available via email, office hours, appointments, and offer 
regular training opportunities. See our [Get Help page](../../../support_and_training/support/getting-help-from-RCFs/) and [OSG Training page](../../../support_and_training/training/osgusertraining/)
for all the different ways you can reach us. Our purpose 
is to assist you with achieving your computational goals, so we want to hear from you!
