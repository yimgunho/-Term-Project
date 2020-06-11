import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

u = urllib.request.urlopen("https://openapi.gg.go.kr/EmgMedInfo?KEY=685efddff2354c78a02c17e9c9453169&Type=xml&pSize=1000")

soup = BeautifulSoup(u, 'html.parser')

print(soup)

# SUM_DEs = soup.findAll('sum_de')
# for SUM_DE in SUM_DEs:
#     SUM_DE = re.sub('<.*?>', '|', SUM_DE.text)
#     print(SUM_DE)