---
ospool:
  path: support_and_training/ap20-21-migration-fall2025.md
---

# OSPool service migration for ap20-21-23

The Open Science Pool (OSPool) is migrating certain OSPool and OSDF services to new physical / institutional locations. This transition is part of a larger service migration that will streamline and simplify how we run our services, positioning ourselves for long-term sustainability. 

**If your account is on Access Points ap20 or ap21** **(with the suffix `uc.osg-htc.org`) you will be moving to a new Access Point in early December.** 

**Some projects on Access Point ap23.uc.osg-htc.org, the OSG Collab AP, will also be moving to a new Access Point in early December. The users for those projects will be individually notified.**

Please read below for the migration timeline, downtime dates, and post-transition steps. 

➡️ [Timeline](#migration-timeline)

➡️ [What to expect](#what-to-expect)

➡️ [What you should do](#what-you-should-do)

> **If your account is NOT on ap20-21-23** (for example, `ap40.uw.osg-htc.org` or `ap1.facility.path-cc.io`), there will be **no changes** to your account. 


> **If you have accounts on one of ap20-21-23 AND another Access Point like ap40.uw.osg-htc.org** there will be no changes to your `ap40` account; contact [support@osg-htc.org](mailto:support@osg-htc.org) to coordinate consolidating your account information. 

## Migration timeline

* For ap20-21 users: [Go here](#timeline-for-ap20-21-users)
* For ap23 users who are migrating: [Go here](#timeline-for-ap23-users-who-are-migrating)

### Timeline for ap20-21 users

* **December 8-15, 2025:** ap20-21 will be shut down during these dates.   
    * **December 8, 2025:** Job submission is disabled on ap20-21.  
    * **December 11, 2025:** Logins to ap20–21 are disabled; all remaining jobs are put on hold.   
    * **December 11-22, 2025:** All ap20-21 data will be synced to a temporary location (`/migration`).  
* **December 22, 2025:** You can submit jobs from the new Access Points.  
    * You should copy your data (`/migration`) to new `/home` and `/ospool` locations.  
* **December 15 \- January 22, 2026:** We will have dedicated office hours for helping users with the migration.   
* **May 2026:** Access to `/migration` data will be turned off. 

### Timeline for ap23 users who are migrating

* **December 8-15, 2025:** Migration window   
    * **December 8, 2025:** Job submission is disabled for migrating users on ap23. 
    * **December 11, 2025:** ap23 users who are migrating to the new infrastructure will have their logins disabled.
    * **December 11-22, 2025:** All ap23 `/home` and `/scratch` data from users moving to the new infrastructure will be synced to a temporary location: `/migration`.  
* **December 22, 2025:** You can submit jobs from the new Access Points.  
    * You should copy your data from `/migration` to your new `/home`, including data that used to be on `/scratch.`
    * Collaboration shared data in `/ospool/uc-shared/projects/<project>` and `/ospool/uc-shared/public/<project>` will be migrated to a set of new Pelican origins on behalf of the collaboration 
* **December 15 \- January 22, 2026:** We will have dedicated office hours for helping users with the migration.   
* **May 2026:** Access to `/migration` data will be turned off. 

## What to expect

* You will be **unable to submit and run jobs** on the OSPool between Dec. 8-15.   
* You may log into your new Access Point **after Dec. 8**.  
* You may submit jobs on the new Access Points **after Dec. 15**.  
* What happens to your data:  
    * We will copy all user data from ap20, 21 (`/home`, `/ospool`) to a temporary **`/migration`** directory.  
    * We will copy all user data from ap23 (`/home`, `/scratch`) to a temporary `/migration` directory.
    * We will copy all shared data in `/ospool/uc-shared` to a new shared location, which will be accessible by the new access point.
    * After Dec 15, **you are responsible for copying any data you want to keep** from `/migration` into your new `/home` or `/ospool` directories.  
    * Your data in `/migration` will remain available **until May 2026**.

## What you should do

### Log in to your new access point

Your username will remain the same; however, **your AP’s SSH address will change**. See below for your new address.

| Old AP Address | New AP Address |
| :---- | :---- |
| ap20.uc.osg-htc.org | ap41.uw.osg-htc.org |
| ap21.uc.osg-htc.org | ap41.uw.osg-htc.org |
| ap23.uc.osg-htc.org<br>*Only notified users will be migrated* | ap43.uw.osg-htc.org |

### Update data paths

Your `/ospool` directories have changed. Update your scripts or submit files accordingly. 

* Your new `/home` $HOME path will be in the same path (`/home/<user.name>/`)  
* Your `/ospool/` $DATA path is now `/ospool/ap41/data/<user.name>/`

### Copy your data from `/migration`

Your data from ap20-21 has been copied into the temporary **`/migration`** directory on your new Access Point, and should be copied into your new `/home` and `/ospool` directories. 

📅 Data in `/migration` will remain available **until May 2026**, but we recommend moving important data as soon as possible.

#### Copying your migrated /home data

Your `/home` directory has been migrated to your new UW-Madison AP (ap4x). Your home directory was tarred to expedite migration to the new AP and you will need to untar the migrated directory into a subdirectory of your new `/home` path. You can do this by running the following commands:

1. **Make a new subdirectory** under `/home`
    
        mkdir -p ~/migration_temp/

2. **Untar** your `/home` directory:   
    
        tar -xzf /migration/ap2x/home/<username>.tar.gz -C ~/migration_temp/

3. **Review** data in `~/migration_temp/` and **move** files you’d like to keep  
    
        ls ~/migration_temp/
        mv ~/migration_temp/kept_file.txt ~/
    
    ⚠️ **Warning: Be wary of moving hidden files**, as this may overwrite hidden files important account services (such as Git and OSDF). 

#### Copying your migrated /ospool data

Your `/ospool` directory has been migrated to your new UW-Madison AP (ap4x). You’ll need to move the contents of your migrated data to your new directory: `/ospool/ap41/data/<username>/`. 

1. **Navigate** to your migrated `/ospool` directory (changing `ap2x` to the right value):  
    
        cd /migration/ap2x/data/<username>/

2. **Review and Move** and review data and move files you’d like to keep  
    
        ls /migration/ap2x/data/<username>/
        mv /migration/ap2x/data/<username>/kept_file.txt /ospool/ap41/data/<username>/

> ### Checking for completed data transfer
> 
> As of December 19, 2025, we are still completing the transfer of `/ospool` files for 
> a subset of users. These users have been emailed directly, but you can also 
> check if you data has been transferred successfully by checking the ownership of the folder using the following commands:
> 
>     ls -lh /migration/ap2x/data/<username>
> 
> If the output shows:
> 
>     ls: cannot access '/migration/ap2x/data/<username>/': Permission denied
> 
> This indicates that your transfer/verification is still in progress. If you are able to list the directory content, then your data have been fully migrated and ready for copying to your new `/ospool` directory as above. 

#### For ap23→43 users ONLY: copy your /scratch directory

Your migrated `/scratch` directory has been compressed into a `.tar.gz` file at the following path (changing `<username>` to your username):  

    /migration/ap23/scratch/<username>.tar.gz

1. **Make a temporary directory** in your new `/home/` directory and untar the contents of your home directory tarball (`<username>.tar.gz`) using the following commands:
    
        mkdir -p ~/migration_scratch

2. **Untar** your `/home` directory: Your home directory was tarred to expedite migration to the new AP. You should untar it using the following command: 
    
        tar -xzvf /migration/ap23/scratch/<username>.tar.gz -C ~/migration_scratch/

3. **Review data** in `~/migration_scratch/` and **move** files you’d like to keep  
    
        ls ~/migration_scratch/
        mv ~/migration_scratch/kept_file.txt ~/

We **highly recommend taking this time to clean-up the migrated scratch directory** and copy only the files you need to keep to your main home directory. 

### Log in to your new OSPool account portal (registry.cilogon.org)

As part of the migration to the AP41 and AP43 access points, you have access to a new identity/account management portal within the OSPool ecosystem. You can review and manage your identity/account through the OSPool Account Portal at [registry.cilogon.org](https://registry.cilogon.org/registry/co_dashboards/dashboard/co:7).

When you log in with your campus credentials, you’ll be able to:

* **Verify your new AP41 account** and confirm that it has been successfully created.
* **Check your group and project memberships**, including your PI-affiliated groups.
* **Ensure your institutional identity is linked correctly**, which is required for job submission under AP41.
* **Upload new SSH keys** to your profile to expedite the login process on AP41.
  * Previously uploaded SSH keys to OSGConnect have also been migrated your new [registry.cilogon.org](https://registry.cilogon.org) account and are ready for use on AP41! 

## Why are we doing the migration? 

* **Unified management:** Closer integration between different components of the OSPool/OSDF services ecosystem.  
* **Long-term sustainability:** As PATh (https://path-cc.io/) enters its 6th year, we are trying to simplify how we administer OSPool/OSDF services to make them more sustainable. 

## Stay informed

We will post migration updates, downtime notifications, and access instructions in the following places: 

* **This migration page**  
  ➡️ [OSPool service migration for ap20-21-23](/documentation/support_and_training/ap20-21-migration-fall2025/)   
* On the **OSPool Status Page:**  
  ➡️ [https://status.opensciencegrid.org](https://status.opensciencegrid.org)  
    * Subscribe for email updates to receive the latest information.  
* Via emails and updates to the log in "Message of the Day"

### Get Help in Office Hours

We will be hosting a series of office hours following the initial migration window. We **highly recommend** you attend one of these office hour sessions to learn more about these changes.

- January 13th \- 3:00pm \- 4:30pm (Central Time) \- Use our normal office hours link

## Contact us

If you have any questions or concerns during this migration period, please contact the OSG support team:  
📧 [support@osg-htc.org](mailto:support@osg-htc.org)

We appreciate your patience and cooperation as we complete this important transition.

---

*Last updated: December 19, 2025*  
