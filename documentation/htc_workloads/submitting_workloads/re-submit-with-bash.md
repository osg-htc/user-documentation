---
ospool:
  path: htc_workloads/submitting_workloads/re-submit-with-bash.md
---

Submit and Resubmit Multiple Jobs using Bash Scripting
====================================

This guide is based on the original scripts from Jarryd Ramborger at the George Lab at UC San Diego, presented at HTC'24 ([watch the presentation](https://youtu.be/YrCLBf6ATmE?si=Scu4TSt7VlRpzUVL)). You can reach Jarryd at [jkramborger@health.ucsd.edu](mailto:jkramborger@health.ucsd.edu)

## Overview

HTCondor allows for [submitting multiple jobs from a single submit file](../submit-multiple-jobs). Many users find the `queue <var> from <list>` option particularly helpful, as it allows users to submit multiple jobs with one or more distinct variables per job. However, creating this list for hundreds of jobs becomes inefficient to do manually. How can you automate creation of this list? Furthermore, what if you want to rerun only *some* runs and not all?

This guide will walk through the basics of submitting and rerunning jobs with multiple variables by leveraging bash scripting. To fully utilize this guide, users should be familiar with using [`queue <var> from <list>` in submitting multiple jobs](../submit-multiple-jobs/#2-submit-multiple-jobs-with-one-or-more-distinct-variables-per-job).

## Before you start: Consider your own workflow

Every user's workflow is different and has varying needs. You will need to evaluate your own workflow and come up with a strategy for writing scripts for submitting and resubmitting jobs. Here are some questions to consider when strategizing how to automate your workflow:

1. What are common elements within the list of jobs that I need to submit?
2. How do correctly loop through the list of input files and/or arguments in my submit file?
3. How can I uniquely name my outputs so that they don't overwrite each other?
4. If my some of my jobs fail, what parts of their output files (including standard error, output, and log files) distinguishes them from successful jobs?  How can I utilize this difference in rerunning my jobs?


!!! tip "General strategy"
    1. Write a bash script to create a list of variables. (e.g. `ls *.mp4 > input_list.txt`).
    2. Use `queue <var> from <list>` to submit multiple jobs based on the variables.
    3. To resubmit multiple jobs, write a bash script to update your list of variables.
    
In this guide, we will walk through one detailed example on how to leverage bash scripting and the `queue` statement to submit multiple jobs. However, your needs may differ from what's presented. We encourage you to consider how to integrate or modify these methods into your own workflow as you read this guide.

## Submit multiple jobs matching a filename or file extension

Consider a pipeline in which a researcher needs to analyze hundreds of .mp4 video files saved in multiple directories under different names. Below is a snippet of a tree diagram of what their file directory structure might look like. Their data is stored in subdirectories in `videos/`, and they have created separate directories for their standard error (`err/`), standard output (`out/`), and final analysis (`analysis/`).

```
/home/username/
|-- analysis/
|-- analyze_videos.sh
|-- err/
|-- log/
|-- out/
|-- videos/
|   |-- dataset1/
|   |   |-- 2024-09-18-mouse1.mp4
|   |   |-- 2024-09-18-mouse2.mp4
|   |   |-- 2024-09-18-mouse3.mp4
|   |   `-- notes.txt
|   |-- dataset2/
|   |   |-- 2024-10-31-mouse1.mp4
|   |   |-- 2024-10-31-mouse2.mp4
|   |   `-- notes.txt
|   ...
```

The researcher needs to run `analyze_videos.sh` on each .mp4 file. They plan to use the `queue <var> from <list>` syntax to submit all their jobs from a single submit file. To create their list, they can manually copy and paste the path of each .mp4 file into a text document, but this can soon becomes a tedious task. How can they automate this process?

### Create a list of files using Bash scripting
Instead of copy and pasting the path to each video manually, we can leverage Bash scripting to do this for us. There are multiple ways to achieve this: if all the files were in one directory, we could use simple `ls *.mp4 > job_list.txt` command, similar to the example in the [Easily Submit Multiple Jobs guide](../submit-multiple-jobs/#2-submit-multiple-jobs-with-one-or-more-distinct-variables-per-job).

However, the files are listed in multiple sub-directories, so in this case, we will use the `find` command to recursively find the .mp4 files. `find` can be a powerful tool - read more about the `find` command [here](https://help.ubuntu.com/community/find).

Our plan is to print the path for each file, as well as the basename of the file itself. These two elements will then be utilized as *variables* for our HTCondor submit file. Below is the script `create_list.sh`, which accomplishes these tasks:

```
#!/bin/bash

# Set name of the file containing the list of jobs
job_list=job_list.txt

# Specify directory with videos
videos_directory=videos

# Remove the job list file, if it exists, for a clean start
if [ -f "${job_list}" ] ; then
    rm "${job_list}"
fi

# Append list of videos with .mp4 extension to the job list file
for video in $(find ${videos_directory} -type f -name "*.mp4"); do
        echo "${video}, $(basename ${video} .mp4)" >> ${job_list}
        echo "${video} added to ${job_list}"
done
```

??? question "What the script doing in the `for` loop?"

    For users unfamiliar with Bash scripting, the above code can be daunting. Let's break it down step-by-step.

    Recall that the goal is to grab a list of paths to the .mp4 files, as well as the basenames for the files themselves. The .mp4 files are listed in multiple sub-directories. To find those .mp4 files, we can use the `find` command:
    
    ```
    find ${videos_directory} -type f -name "*.mp4"
    ```

    1. The first argument after the `find` command indicates which directory to search in. In this case, we pass the value assigned to `${videos_directory}`, which should be `videos`.
    2. Next, `-type f` indicates that we want to find a file (in contrast to finding a directory).
    3. Lastly, `-name "*.mp4"` indicates we want to find files that match a certain naming pattern. The wildcard `*.mp4` indicates a name with any length of characters as long as it ends with `.mp4`.

    The full `find` command above would generate a list of full paths to files:
    
    ```
    videos/dataset1/2024-09-18-mouse2.mp4
    ```<br>
    ```
    videos/dataset1/2024-09-18-mouse1.mp4
    ```<br>
    ```
    videos/dataset2/2024-10-31-mouse1.mp4
    ```<br>
    ```
    videos/dataset2/2024-10-31-mouse2.mp4
    ```
    
    We can then use `for` to loop through this list and assign each line to the variable `${video}`. The `$()` captures the output of the `find` command, which is then used in the `for` loop.

    > ```
    > for video in $(find ${videos_directory} -type f -name "*.mp4"); do
    > ```

    Each time the `for` loop runs, we want to collect information about the path and the basename in `job_list.txt`. The path is already assigned to the variable `${video}`. To get the basename, we use the `basename` command. When we pass the path into `basename` and use `.mp4` as the second argument, it returns the basename without the .mp4 extension.

    ```basename ${video} .mp4```

    We can then print both the path and the basename to our `${job_list}` file, separated by a comma.
    > ```
    > echo "${video}, $(basename ${video} .mp4)" >> ${job_list}
    > ```

    The next line prints a message to the terminal to let us know that the corresponding file is added to the rerun list. This line could be omitted.
    > ```
    > echo "${video} added to ${job_list}"
    > ```

Once the script is created, we change the script to be executable and run the script. When this is complete, `job_list.txt` now contains a list of absolute paths to the .mp4 files in the videos directory and the basenames of each .mp4 file.

```
[username@ap40 ~ ]$ chmod +x create_list.sh

[username@ap40 ~ ]$ ./create_list.sh
videos/dataset1/2024-09-18-mouse2.mp4 added to job_list.txt
videos/dataset1/2024-09-18-mouse1.mp4 added to job_list.txt
videos/dataset2/2024-10-31-mouse1.mp4 added to job_list.txt
videos/dataset2/2024-10-31-mouse2.mp4 added to job_list.txt

[username@ap40 ~ ]$ ls
analysis/          create_list.sh  job_list.txt  out/
analyze_videos.sh  err/            log/          videos/

[username@ap40 ~ ]$ cat job_list.txt
videos/dataset1/2024-09-18-mouse2.mp4, 2024-09-18-mouse2
videos/dataset1/2024-09-18-mouse1.mp4, 2024-09-18-mouse1
videos/dataset2/2024-10-31-mouse1.mp4, 2024-10-31-mouse1
videos/dataset2/2024-10-31-mouse2.mp4, 2024-10-31-mouse2
```

Notice that in our list, we have the name of the file without the .mp4 extension. In our script, we used the `basename` program within the loop to remove the `.mp4` file extension.

Why might we want to do this? We can use the basename of our file (e.g. `2024-09-18-mouse1`) in the filename of our outputs to keep our files organized. Leaving out the .mp4 extension in these names will make naming these outputs easier.

### Submit multiple jobs using `queue <var> from <list>`

Now, that we have a list, we can use `job_list.txt` in our HTCondor submit file using the `queue <var> from <list>` syntax. Below is our submit file, `job.sub`.

```
# job.sub

executable = analyze_videos.sh
arguments = $(video)

log = log/job_$(Cluster).log
error = err/$(video)_$(Cluster).err
output = out/$(video)_$(Cluster).out

transfer_input_files = $(path)
transfer_output_files = $(video).txt
transfer_output_remaps = "$(video).txt = analysis/$(video).txt"

+JobDurationCategory = "Medium"

request_cpus = 1
request_memory = 10GB
request_disk = 10GB

queue path, video from job_list.txt
```

Notice the `queue` statement on the last line. As HTCondor loops through each line in `job_list.txt`, the values of `$(path)` and `$(video)` will change correspondingly.

We set `transfer_input_files` to reference each .mp4 file using the `$(path)` value from the list. We also pass `$(video)` as an argument to our executable, so our executable knows the basename of the video file and can proceed with its analysis. Lastly, we remap the output file so that HTCondor transfers it to the `analysis` folder.

The researcher can now submit the job. When the job is finished, the output files of the analysis, log, and other files are in their respective folders, as seen in this tree diagram.

```
/home/username/
|-- analysis
|   |-- 2024-09-18-mouse1.txt
|   |-- 2024-10-31-mouse1.txt
|-- analyze_videos.sh
|-- create_list.sh
|-- err
|   |-- 2024-09-18-mouse1_800457.err
|   |-- 2024-09-18-mouse2_800457.err
|   |-- 2024-10-31-mouse1_800457.err
|   `-- 2024-10-31-mouse2_800457.err
|-- job_list.txt
|-- job.sub
|-- log
|   `-- job_800457.log
|-- out
|   |-- 2024-09-18-mouse1_800457.out
|   |-- 2024-09-18-mouse2_800457.out
|   |-- 2024-10-31-mouse1_800457.out
|   `-- 2024-10-31-mouse2_800457.out
...
```

Notice that `2024-09-18-mouse2.txt` and `2024-10-31-mouse2.txt` does not exist in the analysis folder. In our hypothetical scenario, these particular jobs failed, and our researcher needs to rerun the jobs after identifying what caused the failure. The researcher could manually create another `job_list.txt` file with the right information to resubmit the job, but if there are many failures, this could become a tedious task. In the next section, we will see how to automate resubmission of jobs from a batch submission.

## Resubmit selected jobs from a batch submission

Sometimes, one or more jobs in a batch of jobs will fail. Failure can be caused by various reasons: going over requested memory, inconsistent files — the potential reasons are too numerous to list! How can we resubmit a few jobs out of the entire batch of jobs in an automated fashion?

First, we need to *identify the differences between a failed job and a successful job*. In the previous example, if our researcher's calculation was successful, it would transfer the results of the analysis, a .txt file, to the `analysis` folder. If the analysis was unsuccessful, the corresponding .txt file would not exist.

After rectifying the point of failure (such as increasing requested memory), the researcher needs to resubmit the job for videos with the missing analyses. Because the missing analyses have no .txt files in the analysis folder, the researcher realized that they need a script that checks for which analyses are missing and create a new list of videos for submission.

### Create an updated list of files using Bash scripting

One strategy we can use in this scenario is to compare `job_list.txt` with the files currently in the `analysis` directory. If the basename of our .mp4 video matches with a .txt file in the `analysis` directory, we can skip the corresponding job. If the basename does *not* have a match, then we should add that line of the job list to the rerun list.

Below is the script `create_rerun_list.sh`:

```
#!/bin/bash

# Define input and output files for job list
input_list=job_list.txt
rerun_list=rerun_list.txt

# Define analysis directory
analysis_dir=analysis

# Remove the rerun list file, if it exists, for a clean start
rerun_list="rerun_list.txt"
if [ -f "${rerun_list}" ] ; then
    rm "${rerun_list}"
fi

# Loop through input_list and finds the basename: 
#    If there is no match, add it to rerun_list
#    If there is a match in the analysis folder, skip

while read line; do

    match=$( awk '{print $2}' <<< "${line}")

    if [ $(ls ${analysis_dir}/*.txt | grep -c ${match}) -eq 0 ];
    then
        echo "${line}" >> ${rerun_list}
        echo "${match} added to ${rerun_list}."
    else
        echo "${match} has already been run. Skipping."
    fi

done < ${input_list}

```

???+ question "What the script doing in the `while` loop?"

    For users unfamiliar with Bash scripting, the above code can be daunting. Let's break it down step-by-step.

    ??? note "The `while` block"

        The beginning of the `while` block reads a file and assigns each line to the variable `$line`:

        > ```
        > while read line; do
        > ```
        
        The end of the block uses `${input_list}` as the file to be read:

        > ```
        > done < ${input_list}
        > ```

    ??? note "Assigning the basename to `${match}`"

        The first line in the `while` block uses multiple bash commands.
        
        > ```
        > match=$( awk '{print $2}' <<< "${line}")
        > ```

        Recall the format of each line in `job_list.txt`:

        ```
        videos/dataset1/2024-09-18-mouse2.mp4, 2024-09-18-mouse2
        ```

        The basename (`2024-09-18-mouse2`) can be used to match to files in the `analysis` directory. The basename is the second item in the line, so we use `awk '{print2}'` to grab the second item.
        
        However, we still need to refer to the corresponding line in our list. To achieve that, `<<<` feeds `${line}` into the `awk` command.

        Lastly, the variable `${match}` is assigned to the value of the entire command, which is encased in `$()`.

    ??? note "The `if` conditional statement"

        Next, we use an `if` block to make decisions about which lines to add to our list.

        > ```
        > if [ $(ls ${analysis_dir}/*.txt | grep -c ${match}) -eq 0 ];
        > ```

        How did we come to writing this condition? Our goal is to match the basename (`2024-09-18-mouse2`) to a .txt file in the `analysis` directory.

        We can get a list of the .txt files in the `analysis` directory using the `ls` command with the wildcard `*`:

        ```
        ls ${analysis_dir}/*.txt
        ```

        We can then pipe (`|`) the output of the `ls` command to the `grep` command to see if the basename `${match}` exists in the output of the above `ls` command. Additionally, the `-c` flag for grep counts the number of matches.

        The combination of those pieces then becomes:

        ```
        ls ${analysis_dir}/*.txt | grep -c ${match}
        ```

        Lastly, we need to evaluate whether there is a match. If there is a match, the above command will return a number greater than 0. If there is no match, the command will return zero.

        Thus, we set the condition to see if the command (encased in `$()`) evaluates to zero with `-eq 0`.
    
    ??? note "The `then` and `else` blocks"

        Lastly, we print or skip lines depending on whether there is or isn't a match.

        The `then` block:

        If the conditional statement evaluates to 0, then that means there is *no* match, and we should add the line to the rerun list.
        > ```
        > echo "${line}" >> ${rerun_list}
        > ```

        The next line prints a message to the terminal to let us know that the corresponding file is added to the rerun list. This line could be omitted.
        > ```
        > echo "${match} added to ${rerun_list}."
        > ```

        <br>
        The `else` block:

        If the conditional statement returns a value other than 0, then that means there is a match, and the line should *not* be added to the rerun list. This line could be omitted.
        > ```
        > echo "${match} has already been run. Skipping."
        > ```


We can execute `create_rerun_list.sh` and observe which video files will be added to the rerun list, and which will be skipped.

```
[username@ap40 ~ ]$ ./create_rerun_list.sh
2024-09-18-mouse2 added to rerun_list.txt.
2024-09-18-mouse1 has already been run. Skipping.
2024-10-31-mouse1 has already been run. Skipping.
2024-10-31-mouse2 added to rerun_list.txt.
```

### Resubmit selected jobs
Our researcher is now ready to resubmit the selected jobs. Instead of editing the `job.sub` file, it will be useful to create separate submit file, `job_rerun.sub`, where the only difference is the `queue` statement.

```
queue path, video from rerun_list.txt
```

Our researcher can now submit the new jobs, and two jobs are submitted accordingly.
```
[username@ap40 ~ ]$ condor_submit job_rerun.sub
Submitting job(s)..
2 job(s) submitted to cluster 800458.
```

## Other tips and techniques
### Useful commands
Often your bash scripts will use commands like `find`, `grep`, `ls`, and `awk`. Exploring these commands will widen your toolkit for writing automated scripts.

### Arguments
You can generalize your scripts further by using arguments in your Bash scripts. For example, we could change the first few lines of `create_list.sh` to accept arguments:

```
#!/bin/bash

# Set name of the file containing the list of jobs
job_list=$1

# Specify directory with videos
videos_directory=$2
...
```

This allows us to specify the name of our job list file and directory containing our videos without having to constantly edit the script. When we run the new script, the arguments we put in are then assigned to the corresponding variables in the script.
```
[username@ap40 ~] ./create_list.sh new_list.txt updated_videos
updated_videos/dataset1/2024-09-18-mouse2.mp4 added to new_list.txt
updated_videos/dataset1/2024-09-18-mouse1.mp4 added to new_list.txt
updated_videos/dataset2/2024-10-31-mouse1.mp4 added to new_list.txt
updated_videos/dataset2/2024-10-31-mouse2.mp4 added to new_list.txt
```

### Using variables in the `condor_submit` command
In the above example, we copied `job.sub` to `job_rerun.sub` and needed to edit the queue statement to refer to `rerun_list.txt`. Instead of doing this, we can use a variable in the `queue` statement.

```
queue path, video from $(job_list)
```

We can assign the variable and submit the job in one step.

```
[username@ap40 ~] condor_submit job.sub job_list=rerun_list.txt
Submitting job(s)..
2 job(s) submitted to cluster 800469.
```

!!! warning
    Double-check your files and do a small-scale test before using variables in the `condor_submit` command. Any mistakes in a submitting a large number of jobs could potentially mean a large mess to clean up!

## Get Help

For assistance, questions, or discussing strategy, please email the OSG Research Facilitation team at [support@osg-htc.org](mailto:support@osg-htc.org) or attend our [Virtual Office Hours](../../../support_and_training/support/getting-help-from-RCFs/#virtual-office-hours).