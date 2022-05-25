""""
Program: rest_api.py
Author: BenLamb
Description: This RESTful Python program finds a random activity for you to do
when you are feeling bored by using a web API. Hitting Enter will initiate the API
"""

import urllib.request
import json

def main():
    while True:
        user = input("Feeling Bored? Press Enter to retrieve an activity suggestion you can do! (Enter Q to quit)")
        if user == 'Q':
            print("Don't forget to have fun!")
            break
        findActivity()

def findActivity():
    url = "http://www.boredapi.com/api/activity"

    res = urllib.request.urlopen(url)

    status_code = res.status

    if status_code >= 200 and status_code < 300:
        data = res.read().decode('utf-8')
    else:
        print("Sorry, service not available right now. Please try again later")
        return
    obj = json.loads(data)
    print("Here is an activity idea for you: ", obj["activity"])

main()
