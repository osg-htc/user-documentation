---
ospool:
  path: htc_workloads/submitting_workloads/tutorial-command.md
---

Workflow Tutorials 
====================================



OSPool workflow tutorials on Github
-------------------------------

All of the OSG provided tutorials are available as repositories on
[Github](<https://github.com/OSGConnect/>). These
tutorials are tested regularly and should work as is, but if 
you experience any issues please contact us. 

Available tutorials
-------------------

The following tutorials are available and are compatible with OSG-provided Access Points: 

	Currently available tutorials:
	R ...................... Estimate Pi using the R programming language
	R-addlibSNA ............ Shows how to add R external libraries for the R jobs
	ScalingUp-Python ....... Scaling up compute resources - Python example to optimize a function on grid points
	blast-split ............ How to run BLAST on the OSPool by splitting a large input file
 	fastqc ................. How to run FastQC on the OSPool
	dagman-wordfreq ........ DAGMan based wordfreq example
	error101 ............... Use condor_q -better-analyze to analyze stuck jobs
	matlab-HelloWorld ...... Creating standalone MATLAB application - Hello World 
	osg-locations .......... Tutorial based on OSPool location exercise from the User School
	pegasus ................ An introduction to the Pegasus job workflow manager
	quickstart ............. How to run your first OSPool job
	scaling ................ Learn to steer jobs to particular resources
	scaling-up-resources ... A simple multi-job demonstration
	software ............... Software access tutorial
	tensorflow-matmul ...... Tensorflow math operations as a singularity container job on the OSPool - matrix multiplication
  
Install and setup a tutorial
----------------------------

On an OSPool Access Point, type the following to download a tutorial's materials:

	$ git clone https://github.com/OSGConnect/<tutorial-name>
  
This command will clone the tutorial repository to your current working directory.
`cd` to the repository directory and follow the steps described in the `readme.md` file.
Alternatively, you can view the `readme.md` file at the tutorial's corresponding GitHub page.
