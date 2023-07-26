---
ospool:
  path: overview/account_setup/ap7-access.md
---

# Log In to `uw.osg-htc.org` Access Points

**This guide is for users who were notified by a member of the OSG team that they 
will be using the `uw.osg-htc.org` Access Points.**

To join and use the `uw.osg-htc.org` Access Points (`ap40.uw.osg-htc.org`), you will go through the following steps: 

1. Apply for a `uw.osg-htc.org` Access Point account 
2. Have your account approved by an OSG Team member
3. Log in to `ap40.uw.osg-htc.org`

## Request Access to `uw.osg-htc.org` Access Points

To request access to `ap40.uw.osg-htc.org`, submit an application using the following steps:

1. General OSPool users not involved in the 2023 OSG School, please visit this account [registration page](https://registry.cilogon.org/registry/co_petitions/start/coef:297); Researchers accepted into the 2023 OSG User School should use this [User School Registration page](https://registry.cilogon.org/registry/co_petitions/start/coef:415). You will be redirected to the CILogon sign in page. Select your institution and use your institutional credentials to login. You will use these credentials later to login so it is important to remember the institution you use at this step. 
   
   
      <img src="../../../assets/ap7-images/cilogon.png" class= "img-fluid"/>
   
   
   If you have issues signing in using your institutional credentials, contact us at [support@osg-htc.org](mailto:support@osg-htc.org).


2. Once you sign in, you will be redirected to the User Enrollment page. Click "Begin" and enter your name and email address in the following page. In many cases, this information will be automatically populated. If desired, it is possible to manually edit any information automatically filled in. Once you have entered your information, click "SUBMIT".


      <img src="../../../assets/ap7-images/comanage-enrollment-form.png" class= "img-fluid"/>

3. After submitting your application, you will receive an email from [registry@cilogon.org](mailto:registry@cilogon.org) to verify your email address. Click the link listed in the email to be redirected to a page confirm your invitation details. Click the "ACCEPT" button to complete this step.


      <img src="../../../assets/ap7-images/comanage-email-verification-form.png" class= "img-fluid"/>
   

## Account Approval by a Research Computing Facilitator

If a meeting has not already been scheduled with a Research Computing Facilitator, one of the facilitation team will contact you about arranging a short consultation. 

Following the meeting, the Facilitator will approve your account and add your profile to any relevant OSG ‘project’ names. Once your account is ready, the Facilitator will email you with your account details including the 'username' you will use to log in to the `ap40.uw.osg-htc.org` access point. 

## Log in

Once your account has been added to the `ap40.uw.osg-htc.org` access point, you will be able to log in using a terminal or SSH program. Logging in requires authenticating your credientials using one of two options: __web authentication__ or __SSH key pair authentication__. Additional information on this process will be provided during and/or following your discussion with a Research Computing Facilitator.


### Option 1: Log in via Web Authentication

Logging in via web authentication requires no preparatory steps beyond having access to an internet browser. 

To authenticate using this approach: 

1. Open a terminal and type `ssh username@ap40.uw.osg-htc.org`, being sure to replace `username` with your `uw.osg-htc.org` username. Upon hitting enter, the following text should appear with a unique, but similar, URL: 


        Authenticate at
        -----------------
        https://cilogon.org/device/?user_code=FF4-ZX6-9LK
        -----------------
        Type 'Enter' when you authenticate.


2. Copy the `https://` link, paste it into a web browser, and hit enter.  

3. You will be redirected to a new page where you will be prompted to login using your institutional credentials. Once you have done so, a new page will appear with the following text: "You have successfully approved the user code. Please return to your device for further instructions."

4. Return to your terminal, and type 'Enter' to complete the login process. 


### Option 2: Log in via SSH Key Pair Authentication

It is also possible to authenticate using an SSH key pair, if you prefer. Logging in using SSH keys does not require access to an internet browser to log in into the OSG Access Point, `ap40.uw.osg-htc.org`. 

The process below describes how to upload a public key to the registration website. It assumes that a private/public key pair has already been generated. If you need to generate a key pair, see this [OSG guide](../generate-add-sshkey). 

1. Return to the [Registration Page](https://registry.cilogon.org/registry/co_petitions/start/coef:297) and login using your institutional credentials if prompted.

2. Click your name at the top right. In the dropdown box, click "My Profile (OSG)" button.

      <img src="../../../assets/ap7-images/ssh-homepage-dropdown.png" class= "img-fluid"/>

3. On the right hand side of your profile, click "Authenticators" link.

      <img src="../../../assets/ap7-images/ssh-edit-profile.png" class= "img-fluid"/>

4. On the authenticators page, click the "Manage" button.

      <img src="../../../assets/ap7-images/ssh-authenticator-select.png" class= "img-fluid"/>

5. On the new SSH Keys page, click "Add SSH Key" and browse your computer to upload your public SSH key.

      <img src="../../../assets/ap7-images/ssh-key-list.png" class= "img-fluid"/>

You can now log in to `ap40.uw.osg-htc.org` from the terminal, using `ssh username@ap40.uw.osg-htc.org`. When you log in, instead of being prompted with a web link, you should either authenticate automatically or be asked for your ssh key passphrase to complete logging in.


## Get Help

For questions regarding logging in or creating an account, contact us at  [support@osg-htc.org](mailto:support@osg-htc.org).
