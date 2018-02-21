import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpkgraphics%20card'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
print(page_soup.h1)
print(page_soup.p)
