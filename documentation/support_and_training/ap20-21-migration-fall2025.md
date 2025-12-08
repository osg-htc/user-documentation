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

### [⏭️ Jump to the Current Timeframe in the Transition](#3-migration-process-dec-8-15)

## Migration timeline

* For ap20-21 users: [Go here](#timeline-for-ap20-21-users)
* For ap23 users who are migrating: [Go here](#timeline-for-ap23-users-who-are-migrating)

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
    * We will copy all user data from ap23 (`/home`, `/scratch`) to a temporary /migrated directory.
    * We will copy all shared data in `/ospool/uc-shared` to a new shared location, which will be accessible by the new access point.
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

### 3\. Migration process (Dec 8 - 15)

As of today, December 8th, the migration of OSPool Access Points ap20 and ap21 (and some groups on ap23) is officially underway. This message outlines what has changed today and what you can expect during the week-long migration period.

* **Job submission on ap20–21 has been disabled**<br>You can no longer submit new jobs through these Access Points.

* **Jobs still running will be held on Dec 11**<br>Any jobs still in the queue after Dec 11 will be removed.

* **You may now test\* login on your new Access Point**

  \*While full services on the new Access Points may not be available until **December 15**, you *can* log in today to ensure:

  * Your new credentials are working  
  * Your SSH keys are recognized  
  * Your account is active in the [CILogon Registry (COmanage)](https://registry.cilogon.org) system

Your username will remain the same; however, **your AP’s SSH address will change**. See below for your new address.

| Old AP Address | New AP Address |
| :---- | :---- |
| ap20.uc.osg-htc.org | ap41.uw.osg-htc.org |
| ap21.uc.osg-htc.org | ap41.uw.osg-htc.org |
| ap23.uc.osg-htc.org<br>*Only notified users will be migrated* | ap42.uw.osg-htc.org |

#### 📁 Data Migration Begins This Week

Between **Dec 11–15**, we will copy all user data from ap20–21 to the temporary `/migrated` directory on the new Access Points.

During this period:

* You will **not** be able to modify your data on ap20–21.
* No jobs will run.
* Data transfer is handled entirely by OSG staff.

You will begin moving your own data from `/migrated` into your new `/home` and `/ospool` locations starting **Dec 15**. We will send you a ***Welcome to Your New OSPool Account*** email on Dec 15th with additional information.

##### New Data Paths

Your `/ospool` directories have changed. 

* Your new `/home` $HOME path will be in the same path (`/home/<user.name>/`)  
* Your `/ospool/` $DATA path is now `/ospool/ap41/data/<user.name>/`

#### Test-Driving Your New AP41 Account

We encourage you to take your new AP41 account for a spin during the migration period! This is a great time to confirm that your workflows submit and run as expected in the new environment.

Please keep these early submissions limited to small, lightweight test jobs, since services and data paths are still coming online. Data availability may be intermittent through December 15th, so hold off on production-scale work until everything is fully stabilized.

Your testing now helps us ensure a smoother experience once the migration is complete. Thank you for trying it out!

#### Login to Your New OSPool Account Portal (registry.cilogon.org)

As part of the migration to the AP41 access points, you have access to a new identity/account management portal within the OSPool ecosystem. You can review and manage your identity/account through the OSPool Account Portal at [registry.cilogon.org](https://registry.cilogon.org).

When you log in with your campus credentials, you’ll be able to:

* **Verify your new AP41 account** and confirm that it has been successfully created.
* **Check your group and project memberships**, including your PI-affiliated groups.
* **Ensure your institutional identity is linked correctly**, which is required for job submission under AP41.
* **Upload new SSH keys** to your profile to expedite the login process on AP41.
  * Previously uploaded SSH keys to OSGConnect have also been migrated your new [registry.cilogon.org](https://registry.cilogon.org) account and are ready for use on AP41! 

Visiting this portal during the migration provides a quick way to make sure everything is aligned with the new infrastructure before you begin submitting jobs. If something looks incorrect or incomplete, you can let us know early so we can correct any issues to your access ahead of the full transition.

## Get Ready and Excited for the Hard Launch of AP41

The AP41 access points are almost ready to take over as your primary gateway to the OSPool—and this upgrade brings improved stability, performance, and a cleaner, modernized identity system. Now is the perfect time to explore the new environment and make sure your workflows are ready for launch day.

Here’s how you can prepare:

- **Verify your new account** in the [OSPool Account Portal](registry.cilogon.org) to ensure your identity and group memberships are set up correctly.
- **Try out AP41 with small test jobs** to confirm that your scripts, containers, and input/output paths behave as expected in the upgraded environment.
- **Update any automation or hard-coded references** to AP20/21, as these will be retired after the transition.

Your early testing helps ensure a smooth, confident shift into AP41. We’re excited for you to experience the improvements coming with this next-generation access point—thank you for helping us prepare for a successful launch!

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

- December 16th \- 3:00pm \- 4:30pm (Central Time) \- Use our normal office hours link

- December 18th \- 10:30am \- 12pm (Central Time) \- Use our normal office hours link

- January 6th \- 3:00pm \- 4:30pm (Central Time) \- Use our normal office hours link

## Contact us

If you have any questions or concerns during this migration period, please contact the OSG support team:  
📧 [support@osg-htc.org](mailto:support@osg-htc.org)

We appreciate your patience and cooperation as we complete this important transition.

---

*Last updated: November 11th 2025*  
