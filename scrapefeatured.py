import requests
from bs4 import BeautifulSoup
from mechanize import Browser
import time


def featured_movies():
    br = Browser()
    br.set_handle_robots( False )

    url = "https://tubitv.com/category/featured"
    headers = {
                'accept': '*/*',
            # 'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,hi;q=0.7,la;q=0.6',
            'cache-control': 'no-cache',
            'dnt': '1',
            'pragma': 'no-cache',
            'referer': 'https',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
            }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml') 
    #print(soup.prettify())

    el = soup.find_all(class_='web-content-tile__title', href=True)
    for e in el:
        print(e['href'])
    el = soup.find_all(class_='web-content-tile__title', href=True)
    mov = []
    for e in el:
        mov.append(e['href'])
    if len(mov)>0:
        return mov
    else:
        print("No result, trying again :/")
        time.sleep(30)
        featured_movies()

