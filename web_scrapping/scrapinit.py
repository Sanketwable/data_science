from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://pythonscraping.com/pages/page1.html")
#print(html.read())
obj=BeautifulSoup(html.read(),"lxml")
print(obj.h1)
print(obj.nonExistingTag.sometag)
