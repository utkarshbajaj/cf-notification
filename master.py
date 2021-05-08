import requests
import smtplib
import time
import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from contest_list import contest_finder

from credentials import sender_email, passwd
from data import people_data

class SendMail:
    server = smtplib.SMTP('smtp.gmail.com', 587)

    def __init__(self):
        """Connect to the smtp server for gmail"""
        self.server.starttls()
        self.server.login(sender_email, passwd)

        print("Login success")

    def sendto(self, user_info, contestant_info):
        '''Send mail to the participant'''
        rec_email = user_info['useremail']
        new_rating = contestant_info['newRating']
        name = user_info['username']

        message = 'Hello ' + name + '! your new rating is ' + str(new_rating);

        print(message)
        self.server.sendmail(sender_email, rec_email, message)

def send_updates():

    while(True):

        # contestId = contest_finder()
        contestId = 1506

        print("The contest I got is " + str(contestId))
        url = 'https://codeforces.com/api/contest.ratingChanges?contestId=' + str(contestId)

        while True:
            response = requests.get(url)
            data = response.json()

            if(data['status'] == "FAILED"):
                print("Trying again!")
                time.sleep(300)
                continue
            elif(data['status'] == 'OK'):
                break

        mailclient = SendMail()

        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
        db = firestore.client()

        result = db.collection('users').get()

        for contestant in data['result']:
            for user in result:
                if user.to_dict()['userhandle'] == contestant['handle']:
                    # print(user.to_dict())
                    mailclient.sendto(user.to_dict(), contestant)

        break

if __name__ == "__main__":
    send_updates()
