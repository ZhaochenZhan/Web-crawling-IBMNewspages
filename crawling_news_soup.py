#get news-link from IBM NEWS webpage
from bs4 import BeautifulSoup
import urllib
import re

homepage = 'http://www-03.ibm.com/press/us/en/pressreleases/recent.wss'

IBMpage = urllib.urlopen(homepage).read()
soup = BeautifulSoup(IBMpage,'html.parser')
print'BS open'
body = soup.find_all('td')
print len(body)
n=-1
for i in body:
    n = n+2
    print body[n]
    
######################
#using beautifulsoup crawling news
######################
# open link get news 
# change link.txt to link.html format
from bs4 import BeautifulSoup
import urllib
import json

soup = BeautifulSoup(open('link.html'))

n=0
links = soup.find_all('a')
linklist=[]
for link in links:
    n=n+1
    fulllink = link.get('href')
    linklist.append(fulllink)
print 'get linklist'

n = 10
for i in linklist:
    n = n+1
    newslink = 'http://www-03.ibm.com'+str(i)
    IBMpage = urllib.urlopen(newslink).read()
    soup = BeautifulSoup(IBMpage,'html.parser')
    print'BS open' , n
    news = soup.find_all ('p')
    nn = str (news)
    print "crawling pages..." , n
    f = open( n+'.txt','a')
    f.write(nn)
    f.close()
    print 'finish' , n
    break
    
#open cleandata.py
# change txt to html format

########################
#option1:try to remove tags using beautifulsoup,fail!
#######################
# reason: cannot read all file because some[] break the html structure

# modify 4.txt to 4.html format
from bs4 import BeautifulSoup
import json
import re


soup = BeautifulSoup(open('5.html'),'lxml')
content = soup.get_text()

artical = '',join(content.split())
print 'clean the data'
f = open('9_clean.txt','w')
f.write(artical)
f.close
print 'all done'

##############
#option2: using regular expression to remove tags, succeed!
##############
import re

news = open('5.txt').read()
print 'read'
htmll = re.sub('<(.|\n)*?>','',news)
htmll = str(htmll)
htmll2 = htmll.replace('\t','')
html = htmll2.replace('\n','')
print 'regular expression'
f = open ('3.txt','a')
print 'write'
f.write(html)
f.close
print 'done'


