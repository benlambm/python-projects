import requests

# This fakes a browser header to get around MOD_SECURITY issues on Apache webservers
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/ 537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}


def main():
    url = input("Please enter the URL here: ")
    full_text = getPageRequests(url)
    foo = open('requested.txt', 'w')
    foo.write(full_text)
    foo.close()


def getPageRequests(url):
    my_req = requests.get(url, headers=headers)
    return my_req.text


main()