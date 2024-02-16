---
ospool:
  path: htc_workloads/submitting_workloads/jupyter.md
---

# OSPool Notebooks: Access the OSPool via Jupyter Lab

[TOC]

The OSG team supports an OSPool Notebooks service, a Jupyter Lab interface that 
connects with an OSPool Access Point. An OSPool Notebook instance 
can be used to manage files, submit jobs, summarize results and run tutorials. 

## Quick Start

Go to this link to start an OSPool Notebooks instance: 

[Launch an OSPool Notebook](https://notebook.ospool.osg-htc.org){ .md-button }

- You will be prompted to "Sign in" using your institution credentials.
- Once logged in, you will be automatically redirected to the "Server Options" page. Several server options are listed, supporting a variety of programming environment and scientific workflows. 
- Select your desired server option and click "Start" to launch your instance. This process can take several minutes to complete. You will be redirected automatically when your instance is ready.

If you have an existing account on the `ap40.uw.osg-htc.org` Access Point, the 
started Jupyter instance will connect to your account on that Access Point. If you don't have 
an existing OSPool account, your Jupyter instance will be running on a temporary 
Access Point as the "joyvan" user.  For more details on the differences between 
these instances, see [Working with your OSPool Notebooks Instance](#working-with-your-ospool-notebooks-instance)

To log out of your session, go to the top left corner of the JupyterLab interface and click the "File" tab. Under this tab, click "Log Out".

## Why use OSPool Notebooks? 

There are many benefits to using this service: 

**Ease of access**: All you need to access OSPool Notebooks is an internet connection 
and web browser! You don't need an account, ssh keys, or anything else installed 
on your computer. 

**User-friendly environment**: The JupyterLab environment provides access to notebooks, terminals, and text editors in a visual environment, making it easier to use for researchers with newer command line skills. 

**Learn yourself, train others**: We have self-serve tutorials that 
anyone can use by starting up an OSPool Notebook and then going through the materials. 
This can be used by individuals (with or without an OSPool account!) or by anyone who 
wants to run a training on using the OSPool. 

**Integration with Access Point**: If you have an existing OSPool account, 
on `ap40.uw.osg-htc.org`, the OSPool Notebook service allows you to have the 
above benefits as part of your full OSPool account. If you start with a guest account, 
and then apply for a full account, you can keep 
using the same interface to work with the full OSPool. 

## Working with your OSPool Notebooks Instance

### Needed Submit File Options

When submitting jobs from the terminal in the OSPool Notebooks interface, make sure 
to always include this option in your submit file: 

	should_transfer_input = YES

This option is needed for jobs to start and run successfully. 

### OSPool Notebook Experience

There will be slight differences in your OSPool Notebook instance, depending 
on whether you have an existing OSPool account and what Access Point it is on. Click on 
the section below that applies to you to learn more. 

<b>For all users, notebooks will time out after an hour an inactivity and may run for a maximum of four hours. Timing out will not impact jobs submitted to the OSPool.</b>

<details>
<summary>For researchers with accounts on a uw.osg-htc.org access point</summary>
<br>
<b>Working in OSPool Notebooks, your account will be tied to your account on your uw.osg-htc.org access point.</b> This means you will be able to interact with files in your <code>/home</code> directory, execute code, and save files, similar to like you would if you were logged into your access point via a terminal. If you submit jobs to HTCondor, by default, your jobs will run on the Open Science Pool. As of right now, these HTCondor jobs will not be able to access any data you have stored in `/protected`.
<br>
<br>
Unlike logging into your access point through a terminal, when you log in through an OSPool Notebooks instance, you can run computionally intensive tasks in your <code>/home</code> directory. This is because each researcher has a total of 8 CPUs and 16 GB memory available to their OSPool Notebook instance's <code>/home</code> directory. 
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
<b>Working in OSPool Notebooks, your account will <b>not</b> be tied to your account on your login0N.osgconnect.net access point.</b> 
<br>
<br>
OSPool Notebooks are run on only our <code>uw.osg-htc.org access points</code>. This means your OSPool account will not be recognized. Therefore, while you are welcome to upload data to your OSPool Notebooks instance and to use the 8 CPUs and 16 GB memory available to your instance to submit HTCondor jobs and analyze data, <b>we recommend you request an account on a <code>uw.osg-htc.org access points</code> access point to be able to run full OSPool workflows and to avoid having data deleted upon logging out.</b>
<br>
</details>

<details>
<summary>For researchers with guest access on an OSPool access point</summary>
<br>
<b>Our OSPool Notebooks instance is a great way to see if you would like to request an account on an OSPool access point or to practice small High Throughput Computing workflows without needing an OSPool account. </b>  
<br>  
<br>
Your instance has HTCondor pre-installed, which allows you to practice the job submission process required to use OSG resources. Your instance will have 8 CPUs and 16 GB of memory available to your computations. We encourage you to also attend our twice-a-month trainings (where you can use your OSPool Notebooks instance to follow along). At any time, you are welcome to request a full account that will allow you to submit jobs to the OSPool using a Jupyter-based interface.
<br>
</details>

## Read More

For more information about the JupyterLab interface in general, see the [JupyterLab manual](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html).