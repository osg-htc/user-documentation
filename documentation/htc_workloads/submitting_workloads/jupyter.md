---
ospool:
  path: htc_workloads/submitting_workloads/jupyter.md
---

# Launch a JupyterLab Instance

[TOC]

## Objective

This guide describes how to request an account to access a JupyterLab interface, launch a JupyterLab instance, and how to queue HTCondor jobs using your JupyterLab interface.

We welcome feedback on this new service. 

## What is JupyterLab?

JupyterLab is a web-based interface for [Project Jupyter](https://jupyter.org). It is an interactive environment that supports a variety of computational activities and workflows through features such as notebooks, terminals, text editors, etc.

More information about the JupyterLab interface can be found in the [JupyterLab manual](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html).

JupyterLab can be a helpful resource for teaching and for running small batches of HTCondor jobs for testing and/or troubleshooting purposes. JupyterLab jobs also have the option of running post-processing or other analyses on the access point, as opposed to needing to run these steps on an execution point via an HTCondor job.

# How to launch a JupyterLab Instance

To launch a JupyterLab instance, go to https://notebook.ospool.osg-htc.org using an internet browser.

You will be prompted to "Sign in" using your institution credentials.

Once logged in, you will be automatically redirected to the "Server Options" page. Several server options are listed, supporting a variety of programming environment and scientific workflows. 

Select your desired server option and click "Start" to launch your instance. This process can take several minutes to complete. You will be redirected automatically when your instance is ready.

# Working with your JupyterLab Instance

<details>
<summary>For researchers with accounts on a uw.osg-htc.org access point</summary>
<br>
<b>Working in JupyterLab, your account will be tied to your account on your uw.osg-htc.org access point.</b> This means you will be able to interact with files in your <code>/home</code> directory, execute code, and save files, similar to like you would if you were logged into your access point via a terminal. If you submit jobs to HTCondor, by default, your jobs will run on the Open Science Pool. As of right now, these HTCondor jobs will not be able to access any data you have stored in `/protected`.
<br>
<br>
Unlike logging into your access point through a terminal, when you log in through a JupyterLab instance, you can run computionally intensive tasks in your <code>/home</code> directory. This is because each researcher has a total of 8 CPUs and 16 GB memory available to their JupyterLab instance's <code>/home</code> directory. 
<br>
<br>
If you would like your HTCondor jobs to run inside your Jupyter container and not on the OSPool, you can copy/paste these lines to your submit file:
<br>
<br>
<code>requirements = Machine == "CHTC-Jupyter-User-EP-$ENV(HOSTNAME)"
+FromJupyterLab = true</code> 
<br>
<br>
  The <code>requirements =</code> and <code>+FromJupyterLab</code> lines tell HTCondor to assign all jobs to run on the dedicated execute point server assigned to your instance upon launch.
<br>
</details>

<details>
<summary>For researchers with accounts on login0N.osgconnect.net access point</summary>
<br>
<b>Working in JupyterLab, your account will <b>not</b> be tied to your account on your login0N.osgconnect.net access point.</b> 
<br>
<br>
JupyterLab is run on only our <code>uw.osg-htc.org access points</code>. This means your OSPool account will not be recognized. Therefore, while you are welcome to upload data to your JupyterLab instance and to use the 8 CPUs and 16 GB memory available to your instance to submit HTCondor jobs and analyze data, <b>we recommend you request an account on a <code>uw.osg-htc.org access points</code> access point to be able to run full OSPool workflows and to avoid having data deleted upon logging out.</b>
<br>
</details>

<details>
<summary>For researchers with no account on an OSPool access point</summary>
<br>
<b>Our JupyterLab instance is a great way to see if you would like to request an account on an OSPool access point or to practice small High Throughput Computing workflows without needing an OSPool account. </b>  
<br>  
<br>
Your instance has HTCondor pre-installed, which allows you to practice the job submission process required to use OSG resources. Your instance will have 8 CPUs and 16 GB of memory available to your computations. We encourage you to also attend our twice-a-month trainings (where you can use your Jupyter instance to follow along). At any time, you are welcome to request a full account that will allow you to submit jobs to the OSPool using a JupyterLab interface.
<br>
</details>

<b>For all users, notebooks will time out after an hour an inactivity and may run for a maximum of four hours. Timing out will not impact jobs submitted to the OSPool.</b>

# Submitting jobs to HTCondor from JupyterLab

It is possible to use the OSPool's job scheduling software, HTCondor, to submit and manage jobs. We highly recommend all users submitting jobs with their Jupyter interface add `should_transfer_files = YES` to their submit files. 

An example HTCondor submit file for a JupyterLab job may look like:

```
# File Name: jupyter.sub

# Specify the executable, arguments, and any files that are needed as input for the job. 
executable = jupyter.sh
# arguments = 
# transfer_input_files = file1, /path/to/file2

# Require HTCondor to transfer the executable and other files for the job. 
should_transfer_files = YES

# Name the log, standard output, and standard error files. 
log = hello-world.log
output = hello-world.out
error = hello-world.err

# Resource requests
request_cpus = 1
request_memory = 1 GB
request_disk = 2 GB

# Tell HTCondor how many jobs to queue
queue 3
```

# Log Out of JupyterLab Session

To log out of your session, go to the top left corner of the JupyterLab interface and click the "File" tab. Under this tab, click "Log Out".
