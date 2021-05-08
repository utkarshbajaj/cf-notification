import requests
import smtplib
import time
import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from contest_list import contest_finder
from credentials import sender_email, passwd

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

        # msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s"
        # % ( from_addr, to_addr, subj, date, message_text )

        print(message)
        self.server.sendmail(sender_email, rec_email, message)

    def logout(self):
        """Quit the current server session"""

        self.server.quit()
        print("Server quit done")

def send_updates():

    oneday = 86400

    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    mailclient = SendMail()

    while(True):

        contestId = contest_finder()
        # contestId = 1506

        print("The contest I got is " + str(contestId))
        url = 'https://codeforces.com/api/contest.ratingChanges?contestId=' + str(contestId)

        start = time.time()

        while True:
            response = requests.get(url)
            data = response.json()

            end = time.time()
            elapsed = end - start

            # print(elapsed)

            if elapsed > 3 * oneday:
                break

            if(data['status'] == "FAILED"):
                print("Trying again!")
                time.sleep(600)
                continue
            elif(data['status'] == 'OK'):
                break

        if elapsed > 3 * oneday:
            print("ERROR! Contest was faulty")
            continue

        db = firestore.client()

        result = db.collection('users').get()

        for contestant in data['result']:
            for user in result:
                if user.to_dict()['userhandle'] == contestant['handle']:
                    # print(user.to_dict())
                    mailclient.sendto(user.to_dict(), contestant)

        # break
        # uncomment above line to make it run for only for next contest

if __name__ == "__main__":
    send_updates()
