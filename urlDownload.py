 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import urllib2,urllib
import re
from urlparse import urlparse
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4)'}
url = r"http://www.qiushibaike.com/imgrank/"
print 'reading the page...'
request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
html_cont = response.read()
soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
# print(soup.prettify())
images = set()
#淘宝 //g-search2.alicdn.com/bao/uploaded/i3/TB1tLZ1JXXXXXXlXpXXXXXXXXXX_!!0-item_pic.jpg_180x180.jpg_.webp
#糗百 <img src="http://pic.qiushibaike.com/system/pictures/11736/117362557/medium/app117362557.jpg" alt="我反正是笑了" />
print "finding the image urls.."
links = soup.find_all('img',src=re.compile(r"http://pic.qiushibaike.com"))
# print links
for link in links:
	# will get the value of attribute src
	new_url = link['src']
	images.add(new_url)
print "Done.."
count = 0
for img in images:
	path = str(count) + '.jpg'
	data = urllib.urlretrieve(img,path)
	count = count + 1 
	print img
