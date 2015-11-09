#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2
import html2text

response = urllib2.urlopen('http://alexkras.com/archive/')
html = response.read()

data = BeautifulSoup(html, 'html.parser')
archive = data.findAll('div', class_='clean-my-archives')[0]

h = html2text.HTML2Text()
test = unicode(str(archive), 'utf-8')
markdown = h.handle(test)

heading = """
**Backup for Content Posted on http://www.alexkras.com**

Please visit: http://www.alexkras.com if you are trying to find the context for some of the text in this repo.

# Table of Contents

"""

fo = open("README.md", "wb")
outData = heading + markdown
fo.write(outData.encode('utf-8'))
fo.close()


