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

* For ap20-21 users: Go here
* For ap23 users who are migrating: Go here

### Timeline for ap20-21 users

* **November 30, 2025:** We recommend submitting jobs to ap20-21 no later than this date.  
* **December 8, 2025:** You may test login to the new Access Points. You will not be able to submit jobs.  
* **December 8-15, 2025:** ap20-21 will be shut down during these dates.   
    * **December 8, 2025:** Job submission is disabled on ap20-21.  
    * **December 11, 2025:** Logins to ap20–21 are disabled; all remaining jobs are put on hold.   
    * **December 11-15, 2025:** All ap20-21 data will be synced to a temporary location (`/migrated`).  
* **December 15, 2025:** You can submit jobs from the new Access Points.  
    * You should copy your data (`/migrated`) to new `/home` and `/ospool/data` locations.  
* **December 15 \- January 22, 2026:** We will have dedicated office hours for helping users with the migration.   
* **May 2026:** Access to `/migrated` data will be turned off. 

### Timeline for ap23 users who are migrating

* **November 30, 2025:** We recommend submitting jobs to ap23 no later than this date.  
* **December 8, 2025:** You may test login to the new Access Points. You will not be able to submit jobs.  
* **December 8-15, 2025:** Migration window   
    * **December 8, 2025:** Job submission is disabled for migrating users on ap23. 
    * **December 11, 2025:** ap23 users who are migrating to the new infrastructure will have their logins disabled.
    * **December 11-15, 2025:** All ap23 `/home` and `/scratch` data from users moving to the new infrastructure will be synced to a temporary location: `/migrated`.  
* **December 15, 2025:** You can submit jobs from the new Access Points.  
    * You should copy your data from `/migrated` to your new `/home`, including data that used to be on `/scratch.`
    * Collaboration shared data in `/ospool/uc-shared/projects/<project>` and `/ospool/uc-shared/public/<project>` will be migrated to a set of new Pelican origins on behalf of the collaboration 
* **December 15 \- January 22, 2026:** We will have dedicated office hours for helping users with the migration.   
* **May 2026:** Access to `/migrated` data will be turned off. 

## What to expect

* You will be **unable to submit and run jobs** on the OSPool between Dec. 8-15.   
* You may log into your new Access Point **after Dec. 8**.  
* You may submit jobs on the new Access Points **after Dec. 15**.  
* What happens to your data:  
    * We will copy all user data from ap20, 21 (`/home`, `/ospool`) to a temporary **`/migrated`** directory.  
    * We will copy all user data from ap23 (/home, /scratch) to a temporary /migrated directory.
    * We will copy all shared data in /ospool/uc-shared to a new shared location, which will be accessible by the new access point.
    * After Dec 15, **you are responsible for copying any data you want to keep** from `/migrated` into your new `/home` or `/ospool` directories.  
    * Your data in `/migrated` will remain available **until May 2026**.

## What you should do

### 1\. General preparation (November)

* **If you are concerned about interrupted work** during the downtime period (Dec 8-15), please contact OSG staff (support@osg-htc.org) **immediately** to make alternative arrangements.   
* ap20-21 users: Go through both your `/home` and `/ospool/ap2*/data` spaces and **remove files that are no longer needed for your current work.** 
* ap23 users who are moving: Go through your `/home` `/scratch`, `/ospool/uc-shared/public/<project>`, and `/ospool/u-shared/project/<project>` and **remove files that are no longer needed for your current work**.

### 2\. Pre-migration window (Dec 1 \- 8\)

* **Download or back up** any critical data you may need access to during the downtime (Dec. 8-15).  
* **Avoid submitting new jobs and remove idle jobs** that are unlikely to complete by Dec 8. This will allow for cleaner data migration. 

### 3\. Migration process (Dec 8 onward)

More instructions will be added once we are closer to the migration dates. 

## Why are we doing the migration? 

* **Unified management:** Closer integration between different components of the OSPool/OSDF services ecosystem.  
* **Long-term sustainability:** As PATh (https://path-cc.io/) enters its 6th year, we are trying to simplify how we administer OSPool/OSDF services to make them more sustainable. 

## Stay informed

We will post migration updates, downtime notifications, and access instructions in the following places: 

* **This migration page**  
  ➡️ [OSPool service migration for ap20-21](/documentation/support_and_training/ap20-21-migration-fall2025/)   
* On the **OSPool Status Page:**  
  ➡️ [https://status.opensciencegrid.org](https://status.opensciencegrid.org)  
    * Subscribe for email updates to receive the latest information.  
* Via emails and updates to the log in "Message of the Day"

### Get Help in Office Hours

We will be hosting a series of office hours following the initial migration window. We **highly recommend** you attend one of these office hour sessions to learn more about these changes.

- December 16th \- 3:00pm \- 4:30pm (Central Time) \- Use our normal office hours link

- December 18th \- 10:30am \- 12pm (Central Time) \- Use our normal office hours link

- January 6th \- 3:00pm \- 4:30pm (Central Time) \- Use our normal office hours link

## Contact us

If you have any questions or concerns during this migration period, please contact the OSG support team:  
📧 [support@osg-htc.org](mailto:support@osg-htc.org)

We appreciate your patience and cooperation as we complete this important transition.

---

*Last updated: November 6th 2025*  
