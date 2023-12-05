---
ospool:
  path: software_examples/ai/scikit-learn.md
---

# scikit-learn

scikit-learn is a machine learning toolkit for Python.

Below you will find an example on how to use an OSG provided
scikit-learn image. However, it is good to keep in mind that
you have two options when it comes to integrating your own
code:

  1. If the code is simple, send it with the job (this is what the
     example uses)
  2. For more complex codes, consider extending the provided
     containers and integrate the code into the new custom
     container

Containers are detailed in our general documentation:

  * [Containers - Apptainer/Singularity](../../../htc_workloads/using_software/containers-singularity/)

## Python Code

    #!/usr/bin/env python3
    
    # example adopted from https://scikit-learn.org/stable/tutorial/basic/tutorial.html
    
    from sklearn import datasets
    from sklearn import svm
    
    iris = datasets.load_iris()
    digits = datasets.load_digits()
    
    # learning
    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(digits.data[:-1], digits.target[:-1])
    
    # predicting
    print(clf.predict(digits.data[-1:]))

## Submit File

    universe = container
    container_image = /cvmfs/singularity.opensciencegrid.org/htc/scikit-learn:1.3

    log = job_$(Cluster)_$(Process).log
    error = job_$(Cluster)_$(Process).err
    output = job_$(Cluster)_$(Process).out
    
    executable = run-scikit-learn.py
    #arguments = 
   
    # specify both general requirements and gpu requirements 
    requirements = True
    
    request_gpus = 0
    request_cpus = 1
    request_memory = 4GB
    request_disk = 4GB
    
    queue 1


