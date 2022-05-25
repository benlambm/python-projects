import io
import json
import requests
import urllib.request
from geopy.geocoders import Nominatim

# This fakes a browser header to get around MOD_SECURITY issues on Apache webservers
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/ 537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
api_headers = {'Accept': 'application/json'}

def main():
    url = "https://isc.sans.edu/block.txt"
    full_text = getPageRequests(url)
    foo = open('block.txt', 'w')
    foo.write(full_text)
    foo.close()
    fp = open("block.txt", "r")  # open for reading
    # Read existing file with plaintext passwords
    lines = [line.rstrip() for line in fp.readlines()]
    fp.close()

    blacklist = []
    for line in lines:
        if line[0].isdigit():
            blacklist.append(line.split()[0])

    fio = io.open("block.txt", "a", encoding="utf-8")
    fio.write("\n\nEstimated Geographic Coordinates: ")
    for ip in blacklist:
        request = urllib.request.Request(
            'https://api.ipdata.co/' +
            ip + '?api-key=1e8ae39884bace5e2ecc2d4630d812d837e43a1768e542d446aceda2',
            headers=api_headers)
        response_body = urllib.request.urlopen(request).read()
        api_foo = json.loads(response_body)
        print(ip)
        print("Latitude: " + str(api_foo["latitude"]))
        print("Longitude: " + str(api_foo["longitude"]))
        geolocator = Nominatim(user_agent='my_application')
        location = geolocator.reverse(str(api_foo["latitude"])+", "+str(api_foo["longitude"]))
        print("Geo-Location: " + location.address)
        fio.write("\n" + location.address)
        print("\n")

def getPageRequests(url):
    my_req = requests.get(url, headers=headers)
    return my_req.text

main()