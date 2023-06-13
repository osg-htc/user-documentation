---
ospool:
  path: overview/account_setup/ap20-ap21-migration.md
---

**This guide is for users who are migrating from login04.osgconnect.net / login05.osgconnect.net
to the new access points ap20.uc.osg-htc.org / ap21.uc.osg-htc.org**

We are pleased to announce an important update planned for our system
during the summer of 2023. To continue delivering reliable and efficient
service, we will be implementing an essential hardware refresh and
access point migration.

Our new access points are set to elevate your experience, with a focus
on capacity and speed. These enhanced systems will boast larger and
faster file systems, paving the way for improved data handling and
operations. Moreover, we are taking our connectivity a step further by
integrating 100 Gb internet links. This enhancement will ensure a robust
and swift connection, reducing latency and facilitating smoother data
transfers.

Users will have to complete the following steps before August 1st.

## Step 1: Determine Your Assigned Access Point

Your new access point assignment will be based on your current access point:

 * If your current assigment is `login04.osgconnect.net`, your new access point
   will be `ap20.uc.osg-htc.org`
 * If your current assigment is `login05.osgconnect.net`, your new access point
   will be `ap21.uc.osg-htc.org`

## Step 2: Set Up Multi Factor Authentication

An important change is that the new access points will require multi factor authentication.
As part of the migration process, ensure that you install a TOTP client and configure
your OSG Connect account to use it. Please see detailed instructions 
[here](../connect-access/#add-multi-factor-authentication-to-your-web-profile).

## Step 3: Migrate Data

**You are responsible for migrating your own data.** The filesystems from 
login04.osgconnect.net and login05.osgconnect.net will be mounted **temporarily**
on the new access points. Please ensure that you have copied all data you need
by the August 1st deadline.

Once logged in to the new access points, you will find your files from login04/login05 at the following locations:

  * Your old home directory under `/mnt/login04/home/[USERNAME]` or `/mnt/login05/home/[USERNAME]`
  * Your old /public directory under `/mnt/public/[USERNAME]`
  * Your old /protected directory under `/mnt/protected/[USERNAME]`

We recommend you use `cp` or `rsync` to duplicate the data to the new locations. Your `$HOME`
directory is still the primary location for jobs, so data you had in your old `$HOME`
directory should likely just be copied to the new `$HOME`. 

[OSDF](../../../htc_workloads/managing_data/overview/) locations have changed. We recommend
that most data from the old `/public/` or `/protected/` move into the new access point
specific "protected" areas (`/ospool/ap20/data/` or `/ospool/ap21/data` based on which access
point you are assigned to). This will offer the the best performance.

For project data you want to make available without authentication, you can use the new
`/ospool/uc-shared/public/[PROJECT]` location.







