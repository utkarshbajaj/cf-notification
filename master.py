import requests
import smtplib
import time
import json

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
        rec_email = user_info['email']
        new_rating = contestant_info['newRating']
        name = user_info['name']

        message = 'Hello ' + name + '! your new rating is ' + str(new_rating);

        print(message)
        self.server.sendmail(sender_email, rec_email, message)

def send_updates():

    while(True):

        contestId = contest_finder()
        # contestId = 1506

        print("The contest I got is " + str(contestId))
        url = 'https://codeforces.com/api/contest.ratingChanges?contestId=' + str(contestId)

        while True:
            response = requests.get(url)
            data = response.json()

            if(data['status'] == "FAILED"):
                print("Trying again!")
                time.sleep(5)
                continue
            elif(data['status'] == 'OK'):
                break

        mailclient = SendMail()

        userdata = json.loads(people_data)

        for contestant in data['result']:
            for user in userdata['users']:
                if(contestant['handle'] == user['name']):
                    # mailclient.sendto(user, contestant)
                    print("Username: ", contestant['handle'], " New Rating: ", contestant['newRating'])

        break

if __name__ == "__main__":
    send_updates()
