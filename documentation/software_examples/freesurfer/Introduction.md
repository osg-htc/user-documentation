---
ospool:
  path: software_examples/freesurfer/Introduction.md
---

# FreeSurfer

## Overview

[FreeSurfer](http://freesurfer.net/) is a software package to analyze MRI scans
of human brains.

OSG used to have a hosted service, called Fsurf. This is no longer available. Instead,
OSG provides a container image, and one of our collaborators provides an optional
workflow using that container.

* Container image: `/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-freesurfer:latest` and defined at [https://github.com/opensciencegrid/osgvo-freesurfer](https://github.com/opensciencegrid/osgvo-freesurfer)
* [FreeSurfer Workflow](https://github.com/pegasus-isi/freesurfer-osg-workflow) 

The container can be used with simple jobs as described below.

## Prerequisites

To use the FreeSurfer on the Open Science Pool (OSPool), you need:

* Your own FreeSurfer license file (see: [https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall#License](https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall#License))
* An account on an OSPool access point. 


## Privacy and Confidentiality of Subjects

In order to protect the privacy of your participants’ scans, we **require that you
submit only defaced and fully deidentified scans for processing**.


## Single Job

The following example job has three files: `job.submit`, `freesurfer-wrapper.sh` and `license.txt`

`job.submit` contents:

    container_image = /cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-freesurfer:latest
    
    executable = freesurfer-wrapper.sh
    transfer_input_files = license.txt, sub-THP0001_ses-THP0001UCI1_run-01_T1w.nii.gz
    
    error = job.$(Cluster).$(Process).error
    output = job.$(Cluster).$(Process).output
    log = job.$(Cluster).$(Process).log
    
    request_cpus = 1
    request_memory = 1 GB
    request_disk = 4 GB
    
    queue 1


`freesurfer-wrapper.sh` contents:

    #!/bin/bash
    
    set -e
    
    # freesurfer environment
    . /opt/setup.sh
    
    # license file comes with the job
    export FS_LICENSE=`pwd`/license.txt
    
    export SUBJECTS_DIR=$PWD
    
    recon-all -subject THP0001 -i sub-THP0001_ses-THP0001UCI1_run-01_T1w.nii.gz -autorecon1 -cw256
    
    # tar up the subjects directory so it gets transferred back
    tar czf THP0001.tar.gz THP0001
    rm -rf THP0001

`license.txt` should have the license data obtained from the Freesurfer project.


