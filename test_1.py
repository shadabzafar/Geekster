# -*- coding: utf-8 -*-
"""Test-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ePAaVgmyjtGT7k9v2fix44UE37tuGcHs
"""

pip install requests beautifulsoup4 pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time-in-python"

response=requests.get(url)

response.text

soup=BeautifulSoup(response.content,'html.parser')

soup.select('pre',class_='lang-py s-code-block')[1].text

answers=[]

for i in soup.select('pre',class_='lang-py s-code-block'):
  answers.append(i.text)

for i in answers:
  print(i)
  print()