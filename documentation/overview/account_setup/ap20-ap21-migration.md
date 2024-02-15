---
ospool:
  path: overview/account_setup/ap20-ap21-migration.md
---

# Migrating to New Access Points From `login04`, `login05`

The `login04`/`login05.osgconnect.net` access points were replaced with
new improved access points during July and August of 2023. If you did not 
migrate your account or data during this time, you can likely still access 
the new access points, following these steps. Please contact the facilitation 
team with any questions. 

## Migration Steps

## Step 1: Determine Your Assigned Access Point

Your new access point assignment will be based on your former access point:

 * If your current assigment is `login04.osgconnect.net`, your new access point
   will be `ap20.uc.osg-htc.org`
 * If your current assigment is `login05.osgconnect.net`, your new access point
   will be `ap21.uc.osg-htc.org`

You can also see this information on your profile page on [osgconnect.net](https://www.osgconnect.net)

## Step 2: Set Up Multi Factor Authentication

An important change is that the new access points will require multi factor authentication.
As part of the migration process, you will connect to your account to a time-based one-time password (TOTP) client. 
When connecting to an access point via ssh, you will be asked to provide the
generated 6 digit verification code when logging in. Please see detailed instructions
[here](../connect-access/#add-multi-factor-authentication-to-your-web-profile).

## Step 3 (If Needed): Modify Workflows to Use New Data Paths

[OSDF](../../../htc_workloads/managing_data/overview/) locations have changed. We recommend
that most data from the old `/public/` or `/protected/` folders transition to the new access point-
specific user-only areas (`/ospool/ap20/data/` or `/ospool/ap21/data` based on which access
point you are assigned to). This will offer the the best performance. You will also 
need to upload submit files and scripts to use these new data locations.  Consult the 
updated [Data Overview](../../../htc_workloads/managing_data/overview/) and 
[OSDF](../../../htc_workloads/managing_data/osdf/) guides for more information, and contact the 
Facilitation team with any questions. 

## Get Help

We understand transitions may raise questions or difficulties. Should you require 
any assistance, please feel free to reach out to us via email, or join one of 
our [office hours sessions](../../../support_and_training/support/getting-help-from-RCFs/#virtual-office-hours ).