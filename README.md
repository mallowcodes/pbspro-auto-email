# pbspro-auto-email
Python and Bash scripts to automate sending output files, errors and usage by email

This code was written for the Artemis supercomputer at USYD. May require modification for use elsewhere.

SET UP:

1. Go into eemail_new.py and change the password to your email password and youremail to your email address
2. Edit the genericchain.bsh file to run the pbs job you want and edit the name of the job to match your pbs jobname

DEFAULT:
eemail_new.pbs is currently set to python eemail_new.py 'Artemis output '"${jobname}"' '"$id" -b "$outid" -b "$outid"'_usage'

with this setting it sets the subject of the email to artemis output jobname jobid and the -b option means it attaches the job output (of the form jobname.ojobid) and the usage file (of the form jobname.ojobid_usage) to the email body. 

if you need to attach the files instead of copying the text to the body you can do so with the -f option. 

you can see help by running python eemail_new.py -h

RUN:
run by entering bash genericchain.bsh
you can edit the name of the genericchain.bsh file to your job name if you want
