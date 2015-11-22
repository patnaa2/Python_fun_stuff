#!/usr/bin/python
from sys import exit as sy_exit
import smtplib

#from python documentation this should work
#this is something weird on google's side of not allowing "secure" apps
#will look into making this work
#to make this work, need to make "mail" work through bash shell

def send_mail(g_user, g_pwd, recipient, message):

    #format message
    g_msg = """\From: %s
               \nTo: %s
               \nSubject: %s
               \n\n %s
            """%(g_user, recipient, message[subject], message[body])

    try:
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo()
        server_ssl.login(g_user, g_pwd)
        server_ssl.sendmail(g_user, recipient, g_msg)
        server_ssl.close()
    except:
        print "Unable to send mail..exiting"
        #not sure if we shoulde exit or handle error somehow
        sy_exit(1)

user = "test123@gmail.com"
password = "password"
rec = "testing123@gmail.com"
message["subject"] = "test1"
message["body"] = "Not sure how to get this to work"
#send_mail(user, password, rec, message)
