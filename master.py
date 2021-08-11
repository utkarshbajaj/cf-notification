import requests
import smtplib
import time
import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from credentials import sender_email, passwd
from aws_access import sendUpdates

# class SendMail:
#     server = smtplib.SMTP('smtp.gmail.com', 587)

#     def __init__(self):
#         """Connect to the smtp server for gmail"""

#         try:
#             self.server.starttls()
#             self.server.login(sender_email, passwd)

#             print("Login success")

#         except:
#             print("Was already logged in")



#     def sendto(self, user_info, contestant_info):
#         '''Send mail to the participant'''
#         rec_email = user_info['useremail']
#         new_rating = contestant_info['newRating']
#         name = user_info['username']

#         message = 'Hello ' + name + '! your new rating is ' + str(new_rating);

#         # msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s"
#         # % ( from_addr, to_addr, subj, date, message_text )

#         print(message)
#         self.server.sendmail(sender_email, rec_email, message)

#     def logout(self):
#         """Quit the current server session"""

#         self.server.quit()
#         print("Server quit done")


class SendUpdates:

    def sendto(self, url):

        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred)

        db = firestore.client()
        result = db.collection('users').get()

        response = requests.get(url)
        data = response.json()

        # sendUpdates(result)

        for contestant in data['result']:
            for user in result:
                if user.to_dict()['userhandle'] == contestant['handle']:
                    # print(user.to_dict())
                    # mailclient.sendto(user.to_dict(), contestant)
                    sendUpdates(user.to_dict(), contestant)

        firebase_admin.delete_app(firebase_admin.get_app(name='[DEFAULT]'))

