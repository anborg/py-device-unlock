# Device Lock & Unlock


## Quick run:
```
sudo su imeiadmin.

```



## Pre-requisites:
```
sudo su imeiadmin.
```
The script is installed in the following directory: /apps/Unlock, and imeiadmin has rwx permissions to Inbound/ Outbound/ logs/ folders


Login to machine:
ssh to your user id to target machine. Eg : ssh myUserId@myhost
su to user imeiadmin. e.g sudo su imeiadmin

Execute:
To process all input files              : /apps/Unlock/run.sh
To process b2b input files              : /apps/Unlock/run_b2brma.sh
To process invtransactions input files  : /apps/Unlock/run_invtransactions.sh
To process rmacrt input files           : /apps/Unlock/run_rmacrt.sh

Note: The folder is named "Unlock", however the script will process lock and unlock.

Troubleshoot FAQ:

1. Userid imeiadmin changes:  Make sure the user has read/write permissions on Inbound/ Outbound/ logs/ directories, under the

2. Input folder change: Update the variable PROCESS_DIR in all *.sh as shown below
PROCESS_DIR=/<myFolderBaseDir> #Folder where Inbound/ Outbound/ logs will exist.

3. A specific file is not processed:
- Ensure that the file name has relevant string in its name. E.g: B2BRMAnotification, INV_TRANSACTION, I020_RMACRT.

4. Connection refused for un/lock sonic service: Contact sonic team. If the service url changed please update url in Source/app.conf

5. Unknown unknown : Please look at the log files in logs/<inputfileName>.log, it should have stack trace explaining the problem.

6. un/Lock did not happen: Check the Soap Request / Response in the log file. If there is no clue, contact sonic team.
