---
ospool:
  path: overview/account_setup/comanage-access.md
---

# Log In to `uw.osg-htc.org` Access Points

**This guide is for users who were notified by a member of the OSG team that they 
will be using the `uw.osg-htc.org` Access Points.**

> To use the `uw.osg-htc.org` Access Points (`ap40.uw.osg-htc.org`), 
> you must have first registered and have your account approved
> as described [here](../registration-and-login).

## Log in

To log in, you can authenticate using one of two methods:

1. [Browser-based web authentication](#option-1-log-in-via-web-authentication) (requires access to web browser)

2. [SSH key pair authentication](#option-2-log-in-via-ssh-key-pair-authentication) (requires uploading an SSH key)

### Option 1: Log in via Web Authentication

Logging in via web authentication requires no preparatory steps beyond having access to an internet browser. 

To authenticate using this approach: 

1. Open a terminal and enter the following command, 
   being sure to replace `username` with your `uw.osg-htc.org` username:
   
   ```
   ssh username@ap40.uw.osg-htc.org
   ```
   
   Upon hitting enter, the following text should appear with a unique URL, similar to the one in the example below: 
   
   ```
   Authenticate at
   -----------------
   https://cilogon.org/device/?user_code=FF4-ZX6-9LK
   -----------------
   Type 'Enter' when you authenticate.
   ```

2. Open your unique `https://` link in your web browser. 
   With some terminals, you may be able to click on the link to open it.
   Otherwise, copy the link and paste it into a web browser, and hit enter.  

3. You will be redirected to a new page where you will be prompted to login using your institutional credentials. 
   Once you have done so, a new page will appear with the following text: `"You have successfully approved the user code. Please return to your device for further instructions."`

4. Return to your terminal, and press the 'Enter' key to complete the login process. 


### Option 2: Log in via SSH Key Pair Authentication

It is also possible to authenticate using an SSH key pair, if you prefer. 
Logging in using SSH keys does not require access to an internet browser.. 

The process below describes how to upload a public key to the registration website. 
It assumes that a private/public key pair has already been generated. 
If you need to generate a key pair, see this [guide](../generate-add-sshkey). 

1. Return to the [Registration Page](https://registry.cilogon.org/registry/) and login using your institutional credentials, if prompted.

2. Click your name at the top right. In the dropdown box, click "My Profile (OSG)" button.

      <img src="../../../assets/ap7-images/ssh-homepage-dropdown.png" class= "img-fluid"/>

3. On the right hand side of your profile, click "Authenticators" link.

      <img src="../../../assets/ap7-images/ssh-edit-profile.png" class= "img-fluid"/>

4. On the authenticators page, click the "Manage" button.

      <img src="../../../assets/ap7-images/ssh-authenticator-select.png" class= "img-fluid"/>

5. On the new SSH Keys page, click "Add SSH Key" and browse your computer to upload your public SSH key.

      <img src="../../../assets/ap7-images/ssh-key-list.png" class= "img-fluid"/>

You can now log in to `ap40.uw.osg-htc.org` from the terminal using the following command, 
being sure to replace `username` with your `uw.osg-htc.org` username:
   
```
ssh username@ap40.uw.osg-htc.org
```

When you run this command, you may be asked for your SSH key passphrase.
Enter your corresponding passphrase and you should be logged in to `ap40.uw.osg-htc.org`.

## Known Issues

* Existing Account
	* Error message: `SORID "http://cilogon.org/serverA/users/20186" is already associated with EnvSource`
	* Try logging into [COmanage](https://registry.cilogon.org/). If you can log in, 
	email us with your name and we will add you to the appropriate group. 

* Privacy enhancing plugins
	* Error message: `Identifier (SORID) variable "REDIRECT_OIDC CLAIM sub" not set`
	* We have seen this happen when a user has various "privacy enhancing" plugins installed in the browser and it blocks the necessary flow from fully happening. Try a different web browser without any plugins installed. 

## Get Help

For questions regarding logging in or creating an account, contact us at [support@osg-htc.org](mailto:support@osg-htc.org).
