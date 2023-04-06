---
ospool:
  path: overview/account_setup/registration-and-login.md
---

Getting Started: Overview of Requesting OSPool Access
====================================


The major steps to get started on the OSPool are: 

* apply for access to the OSPool
* meet with a facilitation team member for an short consultation and orientation. 
* register for a specific OSPool Access Point
* log in to your designated Access Point

Each of these is detailed in the guide below. 
Once you've gone through these steps, you should be able to begin running work! 

## Apply for OSPool Access

To start, fill out the interest form on this OSG Portal site: 

[OS Pool Account Request](https://portal.osg-htc.org/application)

This will send the Research Facilitation team an email. We will be in 
touch to set up an orientation meeting, and confirm if you are joining 
an existing project on the OSPool or starting a new one. 

## Orientation Meeting

The orientation meeting generally takes about 20-30 minutes and is a chance to 
talk about your work, how it will 
fit on the OSPool, and some practical next steps for getting started. 

## Register for an Access Point

Before or during the orientation meeting, you will be prompted to register 
for an account on a specific OSPool Access Point. The current default is the 
"OSG Manage" Access Points, with registration via https://registry.cilogon.org. 
You will be directed to follow instructions on [this page](../ap7-access) to register 
for an account here. 

## Log In

Once you've gone through the steps above, you should have an account on 
on OSPool Access Point. 

If your account is on the "OSG Manage" Access Points (registration via 
https://registry.cilogon.org, accounts on `ap40.uw.osg-htc.org`), follow instructions 
in this guide for logging in: [Registration and Log In to OSG Manage Access Points](../ap7-access.md)

If your account is on the "OSG Connect" Access Points (registration via 
https://www.osgconnect.net/, accounts on `login04.osgconnect.net`, `login05.osgconnect.net`), 
follow instructions 
in this guide for logging in: [Registration and Log In to OSG Connect Access Points](../connect-access.md)

## Overview of access procedure and accounting

For those interested in details, this section describes some of the background 
information behind projects. 

The OSG governs access to grid resources through an accounting
framework that assigns each user's *jobs* to an *accounting group* or *project*.
As a new user of the OSG, one of the first things to iron out is what
project or projects best describe your work.  This is more a matter of
accountability than of entitlement: it concerns how organizations report to
their sponsors and funding agencies on the utilization of resources placed under
their administration.

To assist in this, OSG Connect uses a group management tool that places users
into one or more groups with names such as *osg.RDCEP* or *osg.Extenci*. 
The *osg* portion of this name differentiates our groups from those of 
other organizations in the same group management facility. The latter portion 
identifies the specific project, each with a Principal Investigator or other 
administrator, that oversees access to resources. Within our web tools, these 
names are often in mixed case, though you may see them uppercased in some 
reporting/accounting software.

The first step in registration is to create a user account and *bind* it to
other identity information. After that you will enroll in a project group.

Once you've enrolled in a group, you'll have the requisite rights to log in to
the submit node for the OSG Connect job scheduler, or to transfer data in and
out of Stash. Submit node logins are typically via Secure Shell (SSH) using a
password or a public key. We'll discuss how to connect further on.

[ssh-key]: ../../../overview/account_setup/generate-add-sshkey/
