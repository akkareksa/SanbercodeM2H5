# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 19:36:01 2020

@author: Kevin
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string

#webscraping
alamat = "https://www.kompas.com/global/read/2020/11/13/103507770/ini-bukan-pertama-kalinya-perusahaan-korea-selatan-dituding-bakar-hutan"
html = urlopen(alamat)
data = BeautifulSoup(html, 'html.parser')
read_content = data.find_all("div", {"class":"read__content"})[0]
contents = read_content.find_all("p")
text_processing = []

#filter hanya kontent bacaan yang dianalisis
for content in contents:
    text = content.get_text()
    if "Baca juga:" in text:
        continue
    else:
        text_processing.append(text)

#case folding
#lowercase, remove numeric value, remove punctuation, whitespace
querywords = ""
for text in text_processing:
    text = text.lower()
    text = re.sub(r"\d+","",text)
    text = text.translate(str.maketrans("","",string.punctuation)).strip()
    querywords+= text+" "

#stopword 
#remove defined words
querywords = querywords.split()
stopwords = ["aku", "saya", "dan", "kamu", "yang", "itu"]
resultwords = [word for word in querywords if word not in stopwords]
result = ' '.join(resultwords)
print(result)

