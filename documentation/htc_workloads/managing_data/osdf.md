---
ospool:
  path: htc_workloads/managing_data/osdf.md
---

Transfer Larger Job Files and Containers Using OSDF
===========================================

For input files >1GB and output files >1GB in size, the default HTCondor
file transfer mechanisms run the risk of over-taxing the Access Point and
their network capacity. And this is exactly why the OSDF
([Open Science Data Federation](https://osg-htc.org/services/osdf.html))
exists for researchers with larger per-job data! The OSDF is a network of 
data **origins** and **caches** for data distribution. 

If you have an account on an OSG Access Point, you have access to an OSDF data 
origin, specifically a directory that can be used to stage input and output data for 
jobs, accessible via the OSDF. This guide describes general tips for using the OSDF, 
where to stage your files, and how to access files from jobs. 

## Important Considerations and Best Practices

1. **Use OSDF locations for larger files and containers**: We recommend using 
   the OSDF for files larger than 1GB (input or output) and all container files. 

1. **OSDF files are cached across the Open Science Pool,
   any changes or modifications that you make might not be propagated.**
   This means that if you add a new version of a file the OSDF
   directory, it must first be given a unique name (or directory path) to
   distinguish it from previous versions of that file. Adding a date or
   version number to directories or file names is strongly encouraged to
   manage your files uniqness. This is especially important when using the 
   OSDF for software and containers. 

1. **Never submit jobs from the OSDF locations;** always submit jobs from 
   within the `/home` directory. All `log`, `error`, `output`
   files and any other files smaller than the above values should ONLY ever
   exist within the user's `/home` directory.
   
1. **Files placed within a *public* OSDF directory are publicly accessible**,
   discoverable and readable by anyone, via the web. At the moment, most default 
   OSDF locations are **not** public. 

## Where to Put Your Files

Data origins and local mount points varies between the different
access points. See the list below for the "Local Path" to use, based on your access point. 

<table>
<tr>
  <th>Access Point</th>
  <th>OSDF Origin</th>
</tr>
<tr>
  <td>ap40.uw.osg-htc.org</td>
  <td>Accessible to user only:
      <ul>
        <li><nobr>Local Path: <code>/mnt/stash/ospool/PROTECTED/[USERNAME]</code></nobr></li>
        <li><nobr>Base OSDF URL: <code>osdf:///ospool/PROTECTED/[USERNAME]</code></nobr></li>
      </ul>
  <td>
</tr>
<tr>
  <td>ap20.uc.osg-htc.org</td>
  <td>Accessible to user only:
      <ul>
        <li><nobr>Local Path: <code>/ospool/ap20/data/[USERNAME]</code></nobr></li>
        <li><nobr>Base OSDF URL: <code>osdf:///ospool/ap20/data/[USERNAME]</code></nobr></li>
      </ul>
      Accessible to project group only:
      <ul>
        <li><nobr>Local Path: <code>/ospool/uc-shared/projects/[PROJECT]</code></nobr></li>
        <li><nobr>Base OSDF URL: <code>osdf:///ospool/uc-shared/projects/[PROJECT]</code></nobr></li>
      </ul>
      Public space for projects:
      <ul>
        <li><nobr>Local Path: <code>/ospool/uc-shared/public/[PROJECT]</code></nobr></li>
        <li><nobr>Base OSDF URL: <code>osdf:///ospool/uc-shared/public/[PROJECT]</code></nobr></li>
      </ul>
  <td>
</tr>
<tr>
  <td>ap21.uc.osg-htc.org</td>
  <td>Accessible to user only:
      <ul>
        <li><nobr>Local Path: <code>/ospool/ap21/data/[USERNAME]</code></nobr></li>
        <li><nobr>Base OSDF URL: <code>osdf:///ospool/ap21/data/[USERNAME]</code></nobr></li>
      </ul>
      Accessible to project group only:
      <ul>
        <li><nobr>Local Path: <code>/ospool/uc-shared/project/[PROJECT]</code></nobr></li>
        <li><nobr>Base OSDF URL: <code>osdf:///ospool/uc-shared/project/[PROJECT]</code></nobr></li>
      </ul>
      Public space for projects:
      <ul>
        <li><nobr>Local Path: <code>/ospool/uc-shared/public/[PROJECT]</code></nobr></li>
        <li><nobr>Base OSDF URL: <code>osdf:///ospool/uc-shared/public/[PROJECT]</code></nobr></li>
      </ul>
  <td>
</tr>
</table>

## Transfer Files To/From Jobs Using the OSDF

### Use an 'osdf://' URL to Transfer Large Input Files and Containers

Jobs will transfer data from the OSDF directory when files are indicated
with an appropriate `osdf://` URL (or the older `stash://`) in the
`transfer_input_files` line of the submit file. Make sure to customize the 
base URL based on your Access Point, as described in the [table above](#where-to-put-your-files). 

Some examples: 

* Transferring one file from `/ospool/apXX/data/`

		transfer_input_files = osdf:///ospool/apXX/data/<username>/InFile.txt
		

* When using multiple files from `/ospool/apXX/data/`, it can be useful to use 
	HTCondor submit file variables to make your list of files more readable: 

		# Define a variable (example: OSDF_LOCATION) equal to the 
		# path you would like files transferred to, and call this 
		# variable using $(variable)
		OSDF_LOCATION = osdf:///ospool/apXX/data/<username>
		transfer_input_files = $(OSDF_LOCATION)/InputFile.txt, $(OSDF_LOCATION)/database.sql

### Use `transfer_output_remaps` and 'osdf://' URL for Large Output Files

To move output files into an OSDF directory, users should 
use the **`transfer_output_remaps`** option
within their job's submit file, which will transfer the user's
specified file to the specific location in the data origin.

By using `transfer_output_remaps`, it is possible to specify what path
to save a file to and what name to save it under. Using this approach,
it is possible to save files back to specific locations in your OSDF 
directory (as well as your `/home` directory, if desired).

The general syntax for `transfer_output_remaps` is: 

    transfer_output_remaps = "Output1.txt = path/to/save/file/under/output.txt; Output2.txt = path/to/save/file/under/RenamedOutput.txt"

When saving large output files back to `/ospool/apXX/data/`, the path provided will look like: 

    transfer_output_remaps = "Output.txt = osdf:///ospool/apXX/data/<username>/Output.txt"
    
Some examples: 
	
* Transferring one output file (`OutFile.txt`) back to `/ospool/apXX/data/`: 

		transfer_output_remaps = "OutFile.txt=osdf:///ospool/apXX/data/<username>/OutFile.txt"

* When using multiple files from `/ospool/apXX/data/`, it can be useful to use 
	HTCondor submit file variables to make your list of files more readable. Also note 
	the semi-colon separator in the list of output files. 

		# Define a variable (example: OSDF_LOCATION) equal to the 
		# path you would like files transferred to, and call this 
		# variable using $(variable)
		OSDF_LOCATION = osdf:///ospool/apXX/data/<username>
		transfer_output_remaps = "file1.txt = $(OSDF_LOCATION)/file1.txt; file2.txt = $(OSDF_LOCATION)/file2.txt; file3.txt = $(OSDF_LOCATION)/file3.txt"


## Phase out of stash:/// and stashcp command

Historically, output files could be transferred from a job to an'
OSDF location using the `stashcp` command within the job's
executable. However, this mechanism is no longer encouraged for OSPool
users. Instead, jobs should use `transfer_output_remaps` (an HTCondor
feature) to transfer output files to your assigned OSDF origin. By using
`transfer_output_remaps`, HTCondor will manage the output data transfer
for your jobs. Data transferred via HTCondor is more likely to be
transferred successfully and errors with transfer are more likely to be
reported to the user.

`osdf://` is the new format for these kind of transfers, and is 
equivalent of the old `stash://` format (which will keep on being
supported for the short term).

