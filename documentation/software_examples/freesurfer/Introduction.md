---
ospool:
  path: software_examples/freesurfer/Introduction.md
---

# Introduction to FreeSurfer

## Overview

[FreeSurfer](http://freesurfer.net/) is a software package to analyze MRI scans
of human brains. In the past, we had a service called
Fsurf, which is now discontinued. Instead, we currently utilize a community supported 
FreeSurfer container image and workflow. Please see:

* [https://github.com/pegasus-isi/freesurfer-osg-workflow](https://github.com/pegasus-isi/freesurfer-osg-workflow) - scroll down to see the documentaion on this page.
* Container image: `/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-freesurfer:latest` and defined at [https://github.com/opensciencegrid/osgvo-freesurfer](https://github.com/opensciencegrid/osgvo-freesurfer)

## Prerequisites

To use the FreeSurfer on the Open Science Pool (OSPool), you need:

* Your own FreeSurfer license file (see: [https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall#License](https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall#License))
* An account on an OSPool access point. 

## Privacy and Confidentiality of Subjects

In order to protect the privacy of your participants’ scans, we **require that you
submit only defaced and fully deidentified scans for processing**.
