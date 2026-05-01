---
ospool:
  path: support_and_training/copyfail26.md
---

# OSG/PATh Major Outage - April 29 - May 1

## What happened
On Wednesday evening, April 29, a serious Linux privilege-escalation exploit was widely published. This exploit allows a local user to obtain admin-level access and bypass standard security controls. 

## Our response 
We temporarily paused OSPool services yesterday morning to protect our users, infrastructure, and contributing sites while we assessed and mitigated the risk.

We have now applied patches across our infrastructure and are continuing to test and monitor systems to ensure the vulnerability does not compromise OSPool operations.

As the OSPool reopens for job processing, you may notice longer queue times over the next few days. This is expected as different sites rejoin the pool independently and begin accepting jobs again. Some jobs may also need to be released from hold or resubmitted as a result of the shutdown.

## Recommendations for you
We have seen no indicators of compromise. We recommend against storing private keys on OSPool Access Points. If you do store your **private** SSH keys on OSPool Access Points, consider replacing them. 

To generate new SSH key pairs on the AP, you can run the command:

`ssh-keygen -t rsa`

**You should set a strong, unique passphrase when prompted.**

Once you’ve generated your new SSH key, you’ll be able to share your public key (ending with `.pub`) with other computing resources you would like to access from the AP via SSH. You should delete the old public key from any server you may have uploaded it to. To do so, you’ll need to:

1. Log in to the remote server  
2. Open the authorized keys file in your choice of editor  
   `nano ~/.ssh/authorized_keys`  
3. Delete the line containing your old SSH key  
4. Upload your new SSH public (`.pub`) key to the server

*You may need to contact the administrator of your system to delete/update SSH keys on the remote server*. 

If you have API keys, tokens, passwords, or other secrets stored on an OSPool Access Point, we also recommend rotating those credentials. Please consult the documentation for the relevant service for instructions on revoking and reissuing those credentials.

## Reporting Security Incidents 
We would also like to remind users of our Security Incident Reporting guidance.

Our goal is to make OSPool resources convenient and effective for advancing research while also protecting users, contributing sites, and the broader research computing ecosystem. If you suspect a security issue, please report it promptly. Early reporting helps staff respond quickly and limit the impact of potential security threats.

Please **never attempt to test suspected vulnerabilities on OSPool systems**, even in good faith. Suspected vulnerabilities, exposures, or unusual system behavior should be reported directly to the OSPool team.

Learn more about our reporting process at: [https://portal.osg-htc.org/documentation/support\_and\_training/support/security](https://portal.osg-htc.org/documentation/support_and_training/support/security)   
