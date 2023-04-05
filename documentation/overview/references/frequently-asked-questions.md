---
ospool:
  path: overview/references/frequently-asked-questions.md
---

Frequently Asked Questions 
====================================

## Getting Started
   
<details>
<summary>Who is eligible to request an OSG account?</summary>
<br>
Any researcher affiliated with a U.S. institution (college, university, national laboratory or research foundation) is eligible to use OSG resources for their work. Researchers outside of the U.S. with affiliations to U.S. groups may be eligible for membership if they are sponsored by a collaborator within the U.S. 
</details>

<details>
<summary>How do I request an OSG account?</summary>
<br>
Please visit our website for the most up-to-date information on requesting an account. Once your account request has been received, a Research Computing Facilitator will contact you within one business day to arrange a meeting to learn about your computational goals and to create your account. 
</details>

<details>
<summary>How do I change the project my jobs are affiliated with?</summary>
<br>
The OSG team assigns individual user accounts to "projects" upon account creation. These projects are a way to track usage hours and capture information about the types of research running on OSG resources. A project typically corresponds to a research group headed by a single PI, but can sometimes represent a long-term multi-institutional project or some other grouping. If you only belong to a single project, that project will be charged automatically when you submit jobs. Run the following command to see a list of projects you belong to:

    $ grep $USER /etc/condor/UserToProjectMap.txt
  
If need to run jobs under a different project you are a member of, you can manually set the project for those jobs by putting this option in the submit file:

    +ProjectName="ProjectName"
</details>


## Workshops and Training
   
<details>
<summary>Do you offer training sessions and workshops?</summary>
<br>
We offer virtual trainings twice-a-month, as well as an annual, week-long summer school for OSG users. We also participate in additional external conferences and events throughout the year. Information about upcoming and past events, including workshop dates and locations, is available on our website. 
</details>
  
<details>
<summary>Who may attend OSG workshops?</summary>
<br>
Workshops are available to any researcher affiliated with a U.S. academic, non-profit, or government institution.
</details>

<details>
<summary>How to cite or acknowledge OSG?</summary>
<br>
Whenever you make use of OSG resources, services or tools, we request you acknowledge OSG in your presentations and publications using the informtion provided on the [Acknowledging the OSG Consortium](https://osg-htc.org/acknowledging.html) page. 
</details>

## Software
   
<details>
<summary>What software packages are available?</summary>
<br>
In general, we support most software that fits the distributed high throughput computing model (e.g., open source). Users are encouraged to download and install their own software on our Access Points. 
 
Additionally, users may install their software into a Docker container which can run on OSG as an Apptainer image or use one of our existing containers.  See [this guide](../../../htc_workloads/using_software/available-containers-list/) for more information. 
</details>

<details>
<summary>Are there any restrictions on installing commercial softwares?</summary>
<br>
We can only *directly* support software that is freely distributable. At present, we do not have or support most commercial software due to licensing issues. (One exception is running [MATLAB standalone executables](../../../software_examples/matlab_runtime/tutorial-matlab-HelloWorld/) which have been compiled with the MATLAB Compiler Runtime).  Software that is licensed to individual users (and not to be shared between users) can be staged within the user's `/home` directory with HTCondor transferring to jobs, but should not be staged in OSG's public data staging locations (see ../../../htc_workloads/managing_data/osgconnect-storage/-data-management-and-policies). Please get in touch with any questions about licensed software.
</details>
 
<details>
<summary>Can I request for system wide installation of the open source software useful for my research?</summary>
<br>
We recommend users use Docker or Apptainer containers if jobs require system wide installations of software. Visit the [OSPool Documentation](https://portal.osg-htc.org/documentation/) website to learn more about creating your own container. 
</details>
  
## Running Jobs
   
<details>
<summary>What type of computation is a good match or NOT a good match for the OSG's Open Science Pool?</summary>
<br>
The OSG provides computing resources through the Open Science Pool for high throughput computing workloads. You can get the most of out OSG resources by breaking up a single large computational task into many smaller tasks for the fastest overall turnaround. This approach can be 
invaluable in accelerating your computational work and thus your research. Please see our ["Is OSG for You?"](../../../overview/account_setup/is-it-for-you/) page for more details on how to determine if your work matches up well with OSG's high throughput computing model.
</details>
  
<details>
<summary>What job scheduler is being used on the Open Science Pool?</summary>
<br>
We use a task scheduling software called HTCondor to schedule and run jobs.
</details>

<details>
<summary>How do I submit a computing job?</summary>
<br>
Jobs are submitted via HTCondor scheduler. Please see our [Roadmap to HTC Workload Submission](https://portal.osg-htc.org/documentation/htc_workloads/workload_planning/roadmap/) guide for more details on submitting and managing jobs.
</details>
  
<details>
<summary>How many jobs can I have in the queue?</summary>
<br>
The number of jobs that are submitted to the queue by any one user cannot not exceed 10,000 without adding a special statement to the submit file. If you have more jobs than that, we ask that you include the following statement in your submit file: 

`max_idle = 2000`  

This is the maximum number of jobs that you will have in the "Idle" or "Held" state for the submitted batch of jobs at any given time.  Using a value of 2000 will ensure that your jobs continue to apply a constant pressure on the queue, but will not fill up the queue unnecessarily (which helps the scheduler to perform optimally).  
</details>

<details>
<summary>How do I view usage metrics for my project?</summary>
<br>
The project's resource usage appears in the OSG accounting system, [GRACC](https://gracc.opensciencegrid.org/d/000000033/osg-project-accounting?orgId=1). Additional dashboards are available to help filter information of interest. 

At the top of that dashboard, there is a set of filters that you can use to examine the number of hours used by your project, or your institution. 
</details>

  
## Data Storage and Transfer
   
<details>
<summary>What is the best way to process large volume of data?</summary>
<br>
There may be more than one solution that is available to researchers to process large amounts of data. Contact a Facilitator at <support@osg-htc.org> for a free, individual consulation to learn about your options. 
</details>
 
<details>
<summary>How do I transfer my data to and from OSG Access Points?</summary>
<br>
You can transfer data using scp, rsync, or other common Unix tools. See [Using scp To Transfer Files](../../../htc_workloads/managing_data/scp/) for more details.
</details>
  
<details>
<summary>How public is /public?</summary>
<br>
The data under your `/public` location is discoverable and readable by anyone in the world. Data in `/public` is made public over http/https (via `https://stash.osgconnect.net/public/`) and mirrored to `/cvmfs/stash.osgstorage.org/osgconnect/public/` (for use with `stashcp`) which is mounted on a large number of systems around the world.
  
Store data in `/protected` or `/home` if you do not want it to be publicly accessible. 
</details>
  
<details>
<summary>Is there any support for private data?</summary>
<br>
Data stored in `/protected` and in `/home` is not publically accessible. **Sensitive data, such as HIPPA data, is not allowed to be uploaded or analyzed using OSG resources.** 
</details>

<details>
<summary>Is data backed up on OSG resources?</summary> 
<br>
Our data storage locations are not backed up nor are they intended for long-term storage. If the data is not being used for active computing work, it should not be stored on OSG systems.
</details>
  
<details>
<summary>Can I get a quota increase?</summary>
<br>
Yes. Contact support@osg-htc.org if you think you'll need a quota increase for `/home`, `/public`, or `/protected` to accommodate a set of concurrently-running jobs. We can suppport very large amounts of data, the default quotas are just a starting point.
</details>
  
<details>
<summary>Will I get notified about hitting quota limits?</summary>
<br>
The best place to see your quota status is in the login message.
</details>
  
## Workflow Management

<details>
<summary>How do I run and manage complex workflows?</summary>
<br>
For workflows that have multiple steps and/or multiple files, we advise using a workflow management system. A workflow management system allows you to define different computational steps in your workflow and indicate how inputs and outputs should be transferred between these steps. Once you define a workflow, the workflow management system will then run your workflow, automatically retrying failed jobs and transferrring files between different steps.
</details>
  
<details>
<summary>What workflow management systems are recommended on OSG?</summary>
<br>
We support DAGMan and Pegasus for workflow management.
</details>
  
