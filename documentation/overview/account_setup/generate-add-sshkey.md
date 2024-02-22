---
ospool:
  path: overview/account_setup/generate-add-sshkey.md
---

Generate SSH Keys For Login
====================================

## Overview

One way to connect to an OSG-managed Access Point is an 
SSH key. This guide details how to create an SSH key. 
Once created, it needs to be added to your web profile 
in order to enable log in to an Access Point. 

## Generate SSH Keys

We will discuss how to generate a SSH key pair for two cases: 

* "Unix" systems (Linux, Mac) and certain, latest versions of Windows
* Older Windows systems

Please note: The key pair consist of a private key and a public key. You will upload the 
public key to OSG Connect, but you also need to keep a copy of the private key to log in!  
You should keep the private key on machines that you have 
direct access to, i.e. your local computer (your laptop or desktop).

### Unix-based operating system (Linux/Mac) or latest Windows 10 versions

We will create a key in the .ssh directory of your computer. Open a terminal on your local computer and run the following commands: 

     mkdir ~/.ssh
     chmod 700 ~/.ssh
     ssh-keygen -t rsa

For the newer OS versions the .ssh directory is already created and the first command is redundant. The last command will produce a prompt similar to

     Generating public/private rsa key pair.
     Enter file in which to save the key (/home/<local_user_name>/.ssh/id_rsa):

Unless you want to change the location of the key, continue by pressing enter.
Now you will be asked for a passphrase. Enter a passphrase that you will be 
able to remember and which is secure:

     Enter passphrase (empty for no passphrase):
     Enter same passphrase again:

When everything has successfully completed, the output should resemble the
following: 

     Your identification has been saved in /home/<local_user_name>/.ssh/id_rsa.
     Your public key has been saved in /home/<local_user_name>/.ssh/id_rsa.pub.
     The key fingerprint is:
     ...

The part you want to upload is the content of the `.pub` file (~/.ssh/id_rsa.pub)
The following video demonstrates the key generation process from the [terminal](https://www.youtube.com/watch?v=sKXqRjKm4bM&t=114s&ab_channel=OSG) 

### Windows, using Putty to log in

If you can connect using the `ssh` command within the Command Prompt (Windows 10 build version 1803 and later), please follow the Mac/Linux directions above. If not, 
continue with the directions below. 

1. Open the `PuTTYgen` program.  You can download `PuttyGen` 
here: [PuttyGen Download Page](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), 
scroll down until you see the `puttygen.exe` file. 

2. For Type of key to generate, select RSA or SSH-2 RSA. 

2. Click the "Generate" button.

3. **Move your mouse in the area below the progress bar.**
When the progress bar is full, PuTTYgen generates your key pair.

4. Type a passphrase in the "Key passphrase" field. Type the same passphrase in the "Confirm passphrase" field. You 
can use a key without a passphrase, but this is not recommended.

5. Click the "Save private key" button to save the private key. **You must save the private key.** You will need it to connect to your machine.

6. Right-click in the text field labeled "Public key for pasting into OpenSSH authorized_keys file" and choose Select All.

7. Right-click again in the same text field and choose Copy.

![alt text](/images/putty_ssh.png "PuttyGen Window")

## Next Steps

After generating the key, you will need to upload it to a web profile to use it 
for log in. 

* If you have an account on an `uw.osg-htc.org` Access Point (account created through https://registry.cilogon.org/registry/) follow the instructions here: [Log In to `uw.osg-htc.org` Access Points](../ap7-access#log-in)
* If you have an account on "OSG Connect" Access Points (account created through https://www.osgconnect.net/), follow the instructions here: [Log In to OSG Connect Access Points](../connect-access#log-in)


## Getting Help 

For assistance or questions, please email the OSG Research Facilitation team  at <mailto:support@osg-htc.org> or visit the [help desk and community forums](http://support.opensciencegrid.org).
