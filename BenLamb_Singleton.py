"""
ProgramName: BenLamb_singleton.py
Author: BenLamb
Description: Turns last-week's web API program into a Singleton class
so only one instance of FindActivity class can be initialized
"""

import urllib.request
import json


def main():
    while True:
        user = input("Feeling Bored? Press Enter to retrieve an activity suggestion you can do! (Enter Q to quit)")
        if user == 'Q':
            print("Don't forget to have fun!")
            break
        fa1 = FindActivity()
        fa1.find_activity()


class FindActivity:
    def find_activity(self):
        url = "http://www.boredapi.com/api/activity"
        res = urllib.request.urlopen(url)
        status_code = res.status
        if 200 <= status_code < 300:
            data = res.read().decode('utf-8')
        else:
            print("Sorry, service not available right now. Please try again later")
            return
        obj = json.loads(data)
        print("Here is an activity idea for you: ", obj["activity"])

    # makes FindActivity a Singleton class
    singleton = None

    def __new__(cls):
        if not cls.singleton:
            cls.singleton = super(FindActivity, cls).__new__(cls)
        return cls.singleton

main()
