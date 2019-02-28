import urllib.request
from bs4 import BeautifulSoup
import re


html=urllib.request.urlopen('http://coinpan.com/free')
soup=BeautifulSoup(html,'html.parser')