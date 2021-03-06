# working with HTML parser
import requests
from bs4 import BeautifulSoup
import re

r = requests.get('http://srbiau.ac.ir/fa/news/category/100/%DA%A9%D8%A7%D8%B1%DA%AF%D8%A7%D9%87-%D9%87%D8%A7')
# print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup)

val = soup.find('a')
# print(val)
val = soup.find_all('h3')
# print(val)
val1 = val[1]
# print(val1)
# print(val1.attrs)
result = soup.find_all('h3', attrs={'class': 'title'})
# print(result)
# print(result[2].text)
all_workshops = [x.text.strip() for x in result]
workshops = [workshop for workshop in all_workshops if workshop.__len__() > 15]
print(*workshops, sep="\n")
