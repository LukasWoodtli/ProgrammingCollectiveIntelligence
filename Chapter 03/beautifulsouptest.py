'''
Created on 30.08.2011

@author: Luki
'''

import urllib2
from BeautifulSoup import BeautifulSoup

c=urllib2.urlopen('http://kiwitobes.com/wiki/Programming_language.html')
soup=BeautifulSoup(c.read())
links= soup('a')
print links[10]
print links[10]['href']