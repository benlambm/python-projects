import requests
from bs4 import BeautifulSoup

# This fakes a browser header to get around MOD_SECURITY issues on Apache webservers
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/ 537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}

def main():
    myres = requests.get("https://www.orionscache.com/books", headers=headers)
    soup = BeautifulSoup(myres.text, "html.parser")
    links = soup.findAll("a")
    for i in range(10):
        print(links[i])

main()