# IP address to lat/long demo
# Test of ipdata.co geolocation API
#
# Note: you must sign up for a free API key here http://www.ipdata.co
# Replace "api_key" with your key
# Limitations: The free tier allows 1500 requests a day or 45,000 requests a month--> it is up to you to make sure you do not violate these restrictions.


import urllib.request

api_headers = {
  'Accept': 'application/json'
}
request = urllib.request.Request('https://api.ipdata.co/8.8.8.8?api-key=1e8ae39884bace5e2ecc2d4630d812d837e43a1768e542d446aceda2', headers=api_headers)
response_body = urllib.request.urlopen(request).read()
print(response_body)
print("\n")
import json
api_foo = json.loads(response_body)
print(api_foo["latitude"])
print(api_foo["longitude"])