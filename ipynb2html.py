from urllib.request import urlopen
from bs4 import BeautifulSoup

import requests

def get(url):
    data = urlopen(url)
    return BeautifulSoup(data, 'html.parser')

url ='https://github.com/kplr-training/Fondamentaux-Python/blob/main/Days_03/06-List%20Comprehensions.ipynb'
soup = get(url)

result = soup.find('iframe')

ipynb = result['src']
data = requests.get(ipynb).content

print(ipynb)

with open("Output.html", "wb") as text_file:
    text_file.write(data)
