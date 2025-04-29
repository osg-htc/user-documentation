---
ospool:
  path: overview/references/policy.md
---

Policies for Using OSG Services and the OSPool 
====================================

Access to OSG services and the Open Science Pool (OSPool) is contingent on compliance with the below and with any requests from OSG staff to change practices that cause issues for OSG services and/or users. **Please contact us if you have any questions! We can often help with exceptions to default policies and/or identify available alternative approaches to help you with a perceived barrier.**

As the below do not cover every possible scenario of potentially disruptive practices, OSG staff reserve the right to take any necessary corrective actions to ensure performance and resource availability for all users from OSG-managed Access Points. This may include the hold or removal of jobs, deletion of user data, deactivation of accounts, etc. In some cases, these actions may need to be taken without notifying the user.

1. **By using the OSG resources, users are expected to follow the OSPool [acceptable use policy](https://github.com/opensciencegrid/osgconnect-portal-markdowns/blob/master/signup_content/signup_modal.md)**, which includes appropriate scope of use and common user security practices. OSG-operated Access Points are only available to individuals affiliated with a US-based academic, government, or non-profit organization, or with a research project led by an affiliated sponsor.

2. **Do not run computationally-intensive or persistent processes on the Access Points (login nodes).** Exceptions include single-threaded software compilation and data management tasks (transfer to/from the Access Point, directory creation, file moving/renaming, untar-ing, etc.). Software testing should be executed from within submitted jobs. OSG staff reserve the right to kill any tasks running on the login nodes, in order to ensure performance for all users. **Please contact us to discuss appropriate features and options, rather than running scripts (including `cron`) to automate job submission**, throttling, resubmission, or ordered execution (e.g. workflows), even if these are executed remotely to coordinate work on OSG-managed Access Points. These almost always end up causing significant issues and/or wasted computing capacity, and we are happy to help you to use automation tools that integrate with HTCondor.

3. **Data Policies**: *OSG-managed filesystems are not backed up and should be treated as temporary (“scratch”-like) space for active work, only*. Some OSG-managed storage spaces are truly ‘open’ with data available to be downloaded publicly. Of note:
	 - Users should keep copies of essential data and software in non-OSG-managed locations, as OSG staff reserve the right to remove data at any time in order to ensure and/or restore system availability, and without prior notice to users.
	 - Proprietary data, HIPAA, and data with any other privacy concerns should not be stored on any OSG-managed filesystems or computed on using OSG-managed resources. Similarly, users should follow all licensing requirements when storing and executing software via OSG-managed Access Points.
	 - Users should keep their /home directory privileges restricted to their user or group, and should not add ‘global’ permissions, which will allow other users to potentially make your data public.
	 - User-created ‘open’ network ports are [disallowed](https://github.com/opensciencegrid/security/blob/master/docs/policy/OSG_Connect_Login_Server_Open_Port_Policy.md), unless explicitly permitted following an accepted justification to support@osg-htc.org. (If you’re not sure whether something you want to do will open a port, just get in touch!)

4. **Contact the Research Facilitation Team if your workload is scaling beyond several thousand jobs.** You can submit any number of jobs to the OSPool. When submitting less than 10,000 jobs at once, no additional submit file options are needed; for larger workflows, contact the research facilitation team for the needed option(s) to submit more than 10,000 jobs at once. It is strongly recommended to always submit large batches of jobs from a single submit file or DAG. 

5. The following scenarios are a few examples of why jobs may be held or removed, either automatically or by OSG staff. Any time your jobs go on hold or are removed (for any reason!), please contact us so we can help you understand the problem and avoid it in the future.
	 - **Jobs using more memory or disk than requested** (see [Scaling Up after Test Jobs](../../../htc_workloads/workload_planning/preparing-to-scale-up/) for tips on requesting the ‘right’ amount of job resources in your submit file).
	 - **Jobs running longer than their JobDurationCategory allows for** (see [Indicate the Job Duration Category of Your Jobs](../../../htc_workloads/workload_planning/roadmap/)).
	 - **Jobs that have executed more than 30 times without completing**  (likely because [they’re too long](../../../overview/account_setup/is-it-for-you/) for the OSPool).
	 - **Jobs otherwise causing known problems** 
	 - **Held jobs may also be edited to prevent automated release/retry**
	 - NOTE: in order to respect user email clients, job holds and removals do not come with specific notification to the user, unless configured by the user at the time of submission using HTCondor’s ‘notification’ feature.
