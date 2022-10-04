---
path:
   path: overview/account_setup/registration.md
---

# Registration and Login for the PATh Facility

The major steps to getting started using compute resources at the PATh Facility are:

* applying for <a href="http://example.com/" target="_blank">example</a> and being approved by the NSF
* applying for an account 
* meeting with a PATh staff member for a short consultation and orientation
* uploading your SSH key

This guide will discuss how to apply for an account and login to the PATh Facility once you have been granted credits by the NSF.

## Get a PATh Facility Account
To register with the PATh facility, submit an application using the following steps:

1. Go to the account [registration page](https://registry.cilogon.org/registry/co_petitions/start/coef:263). You will be redirected to the CILogon sign in page. Select your institution and use your institutional credentials to login.

      ![CILOGIN](../files/cilogon.png)
   
      If you have issues signing in using your institutional credentials, contact us at [support@opensciencegrid.org](mailto:support@opensciencegrid.org).


1. Once you sign in, you will be redirected to the "PATh Facility User Enrollment for New Users" page. Click "Begin" and enter your name, and email address in the following page. In many cases, this information will be automatically populated. If desired, it is possible to manually edit any information automatically filled in. Once you have entered your information, click "SUBMIT".

   
      ![](../files/comanage-enrollment-form.png)


1. After submitting your application, you will receive an email from [registry@cilogon.org](mailto:registry@cilogon.org) to verify your email address. Click the link listed in the email to be redirected to a page confirm your invitation details. Click the "ACCEPT" button to complete this step.

   
      ![](../files/comanage-email-verification-form.png)

## Meet with a Research Computing Facilitator

Once PATh staff receive your email verification, a Research Computing Facilitator will contact you within one business day to arrange a short consultation and introduction to PATh resources. During this meeting, our staff will provide personalized start-up guidance per your specific computational research goals and activate your account.

Following the meeting, the Facilitator will approve your account, add your profile to any relevant PATh 'project' names, and ensure that you have access to the PATh Facility. (You will receive automated emails for some of these actions, which you can otherwise ignore.)


## Login

Once your account has been added to a PATh access point, you will be able to log in using a terminal or SSH program. Logging in requires authenticating your credientials using one of two options: __web authentication__ or __SSH key pair authentication__. Additional information on this process will be provided during and/or following your meeting with a Research Computing Facilitator.


### Option 1: Login via Web Authentication

Logging in via web authentication requires no preparatory steps beyond having access to an internet browser. 

To authenticate using this approach: 

1. Open a terminal and type `ssh username@ap1.facility.path-cc.io`, being sure to replace `username` with your PATh access point username. Upon hitting enter, the following text should appear with a unique, but similar, URL: 


         Authenticate at
         -----------------
         https://cilogon.org/device/?user_code=FF4-ZX6-9LK
         -----------------
         Type 'Enter' when you authenticate.


2. Copy the `https://` link, paste it into a web browser, and hit enter.  

3. You will be redirected to a new page where you will be prompted to login using your institutional credentials. Once you have done so, a new page will appear with the following text: "You have successfully approved the user code. Please return to your device for further instructions."

4. Return to your terminal, and type 'Enter' to complete the login process. 


### Option 2: Login via SSH Key Pair Authentication

It is also possible to authenticate using an SSH key pair, if you prefer. Logging in using SSH keys does not require access to an internet browser to login into the PATh access point, `ap1.facility.path-cc.io`. 

The process below describes how to upload a public key to the registration website. It assumes that a private/public key pair has already been generated. If you need to generate a key pair, see the "Step 1: Generate SSH Keys" section of this [OSG guide](https://support.opensciencegrid.org/support/solutions/articles/12000027675-generate-ssh-keys-and-activate-your-osg-login). 

1. Return to the [Registration Page](https://registry.cilogon.org/registry/co_petitions/start/coef:263) and login using CILogon if prompted.

1. Click your name at the top right. In the dropdown box, click "My Profile (OSG)" button.

      ![](../files/ssh-homepage-dropdown.png)

1. On the right hand side of your profile, click "Authenticators" link.

      ![](../files/ssh-edit-profile.png)

1. On the authenticators page, click the "Manage" button.

      ![](../files/ssh-authenticator-select.png)

1. On the new SSH Keys page, click "Add SSH Key" and browse your computer to upload your public SSH key.

      ![](../files/sh-key-list.png)


## Get Help

For questions regarding logging in or creating an account, contact us at  [support@opensciencegrid.org](mailto:support@opensciencegrid.org).
