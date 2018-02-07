import smtplib
import os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("subjecttext", help="subject of the email in quotes, e.g. 'test subject'") 
parser.add_argument("-b", "--bodytextfile", action="append", help="body of the email as txt file, e.g. -b /test1.txt . Can attach multiple. Do not use for large files.")
parser.add_argument("-f", "--filelist", action="append", help="files to attach, using -f and quotes, e.g. -f '/images2017/f20.png' -f '/images2017/f30.png' -f '/images2017/f40.png'")
args = parser.parse_args()

import StringIO

if args.bodytextfile is None:
	textout=None
else:
        textout = StringIO.StringIO()       #use io.StringIO for python3
        for file_dir in args.bodytextfile:
            with open(file_dir, 'r') as file:
                textout.write(file.read())
                textout.write('\n')
                textout.write('\n')
        textout= textout.getvalue()
        
if args.filelist is None:
	filetuple=()
else:
	filetuple=tuple(args.filelist)

def send_mail(send_from, send_to, subject, text, files=None, server="smtp.office365.com", port=587, isTls=True): #server="outlook.office365.com"): #, server="127.0.0.1"):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        if os.path.isfile(f) == True:
            with open(f, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=os.path.basename(f)
                )
            # After the file is closed
            part['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(f)
            msg.attach(part)


    smtp = smtplib.SMTP(server,port)
    if isTls: smtp.starttls()
    smtp.login(send_from, "your_password_here")
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

send_mail(send_from = "youremail@office365domain", send_to= ["youremail@office365domain"], subject=args.subjecttext,text=textout, files=filetuple)
