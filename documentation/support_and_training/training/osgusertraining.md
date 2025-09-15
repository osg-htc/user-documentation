---
ospool:
  path: support_and_training/training/osgusertraining.md
---

OSG User Training (regular/monthly) 
====================================

All User Training sessions are offered on **Tuesdays from 2:30-4pm ET (11:30am - 1pm PT)**, on the third Tuesday of the month. The training's are designed as stand alone subjects. You do not need to bring/have your dataset prepared before the training. The only prerequisites are some familiarities with using command line inteface or [shell](https://swcarpentry.github.io/shell-novice/). Having some familiarities with [HTCondor job submissions](https://portal.osg-htc.org/documentation/htc_workloads/workload_planning/htcondor_job_submission/) are useful but not required.  

**Registration opens a month before the training date, and closes 24 hours before the event.**

<!-- <font size="15">[Register Here](https://osgfacilitation.setmore.com/#classes)</font> -->
<!--[Register Here](https://osgfacilitation.setmore.com/#classes){.md-button .md-button--primary}-->
[See our training events](osg-htc.org/services/facilitation/monthly-training){.md-button .md-button--primary}

## Spring 2025 Training Schedule

<!-- Template for adding training row to the following table

  <tr>
      <td> Tuesday, __DATE_OF_TRAINING__</td>
      <td><b>__TITLE_OF_TRAINING__</b>
        <p><i>Learning Objectives:</i> Topics covered in this workshop include:</p>
        <ul>
            <li>__TOPIC_1__
            <li>__TOPIC_2__
            <li>__TOPIC_3__
        </ul>
        <p>__TRAINING_DESCRIPTION__</b></p>
        <p><i>Prerequisites/Audience:</i> __PREREQUISITES__</p>
      </td>
  </tr>

-->

<!-- Commenting out. We plan to only update the front-facing training page on the main osg-htc site.

<table>
  <tr>
      <td>Tuesday, January 21</td>
      <td><b>Troubleshooting on the OSPool</b>
        <p><i>Learning Objectives:</i> Topics covered in this workshop include:</p>
        <ul>
            <li>Categories of job problems
            <li>How to get more information about a job problem
            <li>Strategies and considerations for troubleshooting
        </ul>
        <p>This session will focus on learning the concepts of debugging and troubleshooting on the OSPool. It will cover some strategies, tips, and tricks that you can use to answer questions such as "Why are my jobs on hold?" and "Why are my jobs stuck on idle?". At the end of the session is an optional hands-on portion.</b></p>
        <p><i>Prerequisites/Audience:</i> Intended for OSPool users who are familiar with logging in and submitting HTCondor jobs to the OSPool. Some familiarity with shell commands (such as how to edit files, copy/paste in the terminal) and HTCondor commands (such as condor_submit, condor_q) is recommended.</p>
        <a class="md-button md-button--primary" href="https://www.youtube.com/watch?v=azA7-4cPYEY">Video Recording</a>
      </td>
  </tr>
  <tr>
      <td>Tuesday, February 18</td>
      <td><b>Building and Using Containers on the OSPool</b>
        <p><i>Learning Objectives:</i> Topics covered in this workshop include:</p>
        <ul>
            <li>Introduction to containers
            <li>How to install software in a container
            <li>How to use a container to deploy your software in an OSPool job
        </ul>
        <p>Getting your computational program to run on someone else's computer can be a difficult process, especially on the OSPool, where there are many different operating systems with a variety of programs (and versions) installed and you don't have admin permissions. But what if there was a way to make sure your job always ran using your desired operating system, programs, and versions that you chose? In this training, we'll show you how you can achieve this very thing through the use of "container" technology.</b></p>
        <p><i>Prerequisites/Audience:</i> Intended for OSPool users who are familiar with logging in and submitting HTCondor jobs to the OSPool. Participants should have some familiarity with shell commands (such as how to edit files, copy/paste in the terminal).</p>
        <a class="md-button md-button--primary" href="https://www.youtube.com/watch?v=awSLTflAIJ8">Video Recording</a>
      </td>
  </tr>
  <tr>
      <td>Tuesday, March 18</td>
      <td><b>GPUs and Machine Learning in the OSPool</b>
        <p><i>Learning Objectives:</i> Topics covered in this workshop include:</p>
        <ul>
            <li>How to think about a machine learning workflow
            <li>How to run OSPool jobs that use GPUs
        </ul>
        <p> The training will include a step by step demonstration showing how to build up a machine learning workflow (scripting, containerization, data) and then how to run that workflow with HTCondor, using GPUs.</p>
        <p><i>Prerequisites/Audience:</i> Intended for OSPool users who are familiar with logging in and submitting HTCondor jobs to the OSPool. Participants should have some familiarity with shell commands (such as how to edit files, copy/paste in the terminal). Some familiarity with containers is also recommended.</p>
        <a class="md-button md-button--primary" href="https://www.youtube.com/watch?v=igU0RQFkR20">Video Recording</a>
      </td>
  </tr>
  <tr>
      <td>Tuesday, April 15</td>
      <td><b>Use Your Data Anywhere</b>
        <p><i>Learning Objectives:</i> Topics covered in this workshop include:</p>
        <ul>
            <li>Overview of data movement on the OSPool
            <li>How to stage data using the OSDF
            <li>Using the OSDF in you OSPool jobs
        </ul>
        <p>In this training, we will introduce attendees to the Open Science Data Federation (OSDF), a data platform that allows you to stage data for both distributed computing (such as on the OSPool) and sharing your data with others. It's even possible to connect your own storage to the OSDF directly, to both share and use yourself. Join us for an overview of the OSDF and hands-on examples of using it. </b></p>
        <p><i>Prerequisites/Audience:</i> Intended for OSPool users who are familiar with logging in and submitting HTCondor jobs to the OSPool. Participants should have some familiarity with shell commands (such as how to edit files, copy/paste in the terminal).</p>
        <a class="md-button md-button--primary" href="https://www.youtube.com/watch?v=x155qX6NClw">Video Recording</a>
        <a class="md-button md-button--primary" href="https://docs.google.com/presentation/d/1uh1SI1LgSOvPaMESPMwAbdrK8Dep4xunoE08JRrWWv4/edit?usp=sharing">Slides</a>
      </td>
  </tr>
  <tr>
      <td>Tuesday, May 20</td>
      <td><b>Adapting Workflows for High Throughput Bioinformatics</b>
        <p><i>Learning Objectives:</i> Topics covered in this workshop include:</p>
        <ul>
            <li>Setting up software for the OSPool
            <li>Organizing your work environment
            <li>Useful HTCondor submit options
        </ul>
        <p>In this training, we will create and scale up a BWA bioinformations workflow using HTCondor on the OSPool. In doing so, participants will learn how to set up and use software on the OSPool, how to keep their work environment organized, and strategies for HTCondor job submission. Though the training covers a bioinformatic example, the lessons are applicable to anyone interested in scaling up their OSPool computing.</b></p>
        <p><i>Prerequisites/Audience:</i> Intended for OSPool users who are familiar with logging in and submitting HTCondor jobs to the OSPool. Participants should have some familiarity with shell commands (such as how to edit files, copy/paste in the terminal).</p>
      </td>
  </tr>
</table> -->

For a calendar version of these events see:

* [Google Calendar](https://calendar.google.com/calendar/embed?src=c_f786e9455a56e4b1ea7aca0d15c88178fd0e309e92c3cf4767c268ea3e2fc884%40group.calendar.google.com&ctz=America%2FChicago)
* [Download and add to your calendar app](https://calendar.google.com/calendar/ical/c_f786e9455a56e4b1ea7aca0d15c88178fd0e309e92c3cf4767c268ea3e2fc884%40group.calendar.google.com/public/basic.ics)

## Materials

All of our training materials are public and provided under the [Past Training Materials](../materials/)

