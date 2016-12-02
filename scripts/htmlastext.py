#!/usr/bin/env python3.5
from bs4 import BeautifulSoup
import html2text
import urllib

url = 'http://www.apixio.com/technical-post/four-key-updates-from-the-chrome-dev-summit'
req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
response = urllib.request.urlopen(req)

html = response.read()

data = BeautifulSoup(html, 'html.parser')

h = html2text.HTML2Text()
test = str(data)
markdown = h.handle(test)

print(markdown)
