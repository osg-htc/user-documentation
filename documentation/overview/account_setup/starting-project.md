---
ospool:
  path: overview/account_setup/starting-project.md
---

Joining and Setting your Project
====================================



## Background

The OSG Connect team assigns individual user accounts to "projects". These projects 
are a way to track usage hours and capture information about the types of 
research using OSG Connect. 

A project typically corresponds to a research group headed by a single PI, but can 
sometimes represent a long-term multi-institutional project or some other grouping. 

You must be a member of a project before you can use OSG Connect to submit jobs. 
The next section of this guide describes the process for joining an OSG Connect project. 

## Joining a Project

### Project Membership via Account Creation Process (Default)

You will be added to a project when going through the typical 
OSG Connect account setup process. After applying for an OSG Connect account, 
you will receive an email to set up a consultation meeting and confirm which 
'OSG Project' your usage should be associated with. You will be prompted to provide information 
based on the following two scenarios: 

- **If you are the first member of your research group / team to use the OSG through 
OSG Connect**, a new project will be created for you. You will need to provide the following information to do so: 
	-    Project Name
	-    PI Name
	-    PI Email
	-    PI Organization
	-    PI Department
	-    Field of Science: (out of https://osp.unm.edu/pi-resources/nsf-research-classifications.html)
	-    Project Description
- **If you know that other members of your research group have used OSG Connect** in the past, 
you can likely join a pre-existing group. Provide the name of your institution and PI 
to the OSG Connect team (if you haven't already) and we can confirm. 

Based on this information, OSG Connect support staff will either create a project and 
add you to it, or add you to an existing project when your account is approved. 

### Join a Project

If you need to join an existing project (you can be a member of more than one), please email the 
OSG team (support@osg-htc.org) with your name and the project 
you wish to join, with PI in CC to confirm.

## Charging usage to your OSG Connect project

Job submission on OSG Connect requires that the job usage will be charged
to a project. If you only belong to a single project, that project will
be charged automatically. Run the following command to see a list of
projects you belong to:

    $ grep $USER /etc/condor/UserToProjectMap.txt

If need to run jobs under a different project you are a member of, you
can manually set the project for those jobs by putting this option in
the submit file:

    +ProjectName="ProjectName"

## View Metrics For Your Project

The project's resource usage appears in the OSG accounting system, [GRACC](https://gracc.opensciencegrid.org/d/000000033/osg-project-accounting?orgId=1). 
You can see the main OSG Connect dashboard here: [Link to OSG Connect Dashboard](https://gracc.opensciencegrid.org/d/000000099/osg-connect-summary-osgconnect-net-submit-hosts-only?orgId=1)

At the top of that dashboard, there is a set of filters that you can use to examine 
the number of hours used by your project, specific users, or your institution.
