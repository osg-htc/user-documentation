---
ospool:
  path: overview/account_setup/starting-project.md
---

# Set and View Project Usage

## Background

The OSG team assigns individual user accounts to "projects". These projects 
are a way to track usage hours and capture information about the types of 
research using the OSPool. 

A project typically corresponds to a research group headed by a single PI, but can 
sometimes represent a long-term multi-institutional project or some other grouping. 

You must be a member of a project before you can use an OSPool Access Point to submit jobs. 
The next section of this guide describes the process for joining a project. 

## Default Behavior (one project)

By default, you are added to a project when your OSG account is created. This 
project will be automatically added to your job submissions for tracking usage. 

## Choose a Project (multiple projects)

If you are affiliated with multiple groups using the OSPool and are a member of 
multiple projects, you will want to set the project name in your submit file. 

Run the following command to see a list of projects you belong to:

<pre class="term"><code>grep $USER /etc/condor/UserToProjectMap.txt</code></pre>

You can manually set the project for a set of jobs by putting this option in
the submit file:

<pre class="sub"><code>+ProjectName="ProjectName"</code></pre>

## View Metrics For Your Project

The project's resource usage appears in the OSG accounting system, [GRACC](https://gracc.opensciencegrid.org/d/000000074/gracc-home?orgId=1), 
specifically, in this [OSPool Usage 
Dashboard](https://gracc.opensciencegrid.org/d/000000077/open-science-pool-all-usage)

At the top of that dashboard, there is a set of filters that you can use to examine 
the number of hours used by your project, or your institution. You can adjust the time 
range displayed on the top right corner. 
