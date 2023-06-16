---
ospool:
  path: overview/account_setup/ap20-ap21-migration.md
---

**This guide is for users who are migrating from login04.osgconnect.net / login05.osgconnect.net
to the new access points ap20.uc.osg-htc.org / ap21.uc.osg-htc.org**

We are replacing the login04/login05.osgconnect.net access points with
new improved access points.  

**All users with accounts on login04/login05
must migrate to the new servers by Tuesday, August 1.**

Our dedicated infrastructure team has put in considerable effort to
improve the user experience. The new access points have larger and
faster file systems as well as improved network connectivity (100Gb
links), which will improve data handling capabilities. We are also
moving to a newer version of Linux.

To encourage a speedy migration, jobs on the new access points will have
higher priority than jobs on the old access points.

# Migration Steps

## Step 1: Determine Your Assigned Access Point

Your new access point assignment will be based on your current access point:

 * If your current assigment is `login04.osgconnect.net`, your new access point
   will be `ap20.uc.osg-htc.org`
 * If your current assigment is `login05.osgconnect.net`, your new access point
   will be `ap21.uc.osg-htc.org`

## Step 2: Set Up Multi Factor Authentication

An important change is that the new access points will require multi factor authentication.
As part of the migration process, you will connect to your account to a time-based one-time password (TOTP) client. 
When connecting to an access point via ssh, you will be asked to provide the
generated 6 digit verification code when logging in. Please see detailed instructions
[here](../connect-access/#add-multi-factor-authentication-to-your-web-profile).

## Step 3: Migrate Data

**You are responsible for migrating your own data from login04/login05 to the 
new Access Points.** The filesystems from `login04.osgconnect.net` and `login05.osgconnect.net` 
will be mounted **temporarily** on the new access points for ease of data transfer. 
Please ensure that you have copied all data you need
by the August 1st deadline.

**Once logged in to the new access points**, you will find your files from login04/login05 at the following locations:

  * Your old home directory under `/mnt/login04/home/[USERNAME]` or `/mnt/login05/home/[USERNAME]`
  * Your old /public directory under `/mnt/public/[USERNAME]`
  * Your old /protected directory under `/mnt/protected/[USERNAME]`

We recommend you use `cp` or `rsync` to duplicate the data to the new locations. Your `$HOME`
directory is still the primary location for jobs, so data you had in your old `$HOME`
directory should likely just be copied to the new `$HOME`. 

**After the migration deadline, all data will be deleted from login04 / login05 under `$HOME`, `/public`, and `/protected`**

## Step 4 (If Needed): Modify Workflows to Use New Data Paths

[OSDF](../../../htc_workloads/managing_data/overview/) locations have changed. We recommend
that most data from the old `/public/` or `/protected/` folders move into the new access point-
specific user-only areas (`/ospool/ap20/data/` or `/ospool/ap21/data` based on which access
point you are assigned to). This will offer the the best performance. You will also 
need to upload submit files and scripts to use these new data locations.  Consult the 
updated [Data Overview](../../../htc_workloads/managing_data/overview/) and 
[OSDF](../../../htc_workloads/managing_data/osdf/) guides for more information, and contact the 
Facilitation team with any questions. 

# Get Help

We understand transitions may raise questions or difficulties. Should you require 
any assistance, please feel free to reach out to us via email, or join one of 
our [office hours sessions](../../../support_and_training/support/getting-help-from-RCFs/#virtual-office-hours )
).  We are happy to walk through the migration steps online so that you have minimal
 interruptions to your work. 
