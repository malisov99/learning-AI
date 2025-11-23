#Задание 2. Веб-скрейпинг ИИ новостей

"""Используя пример веб-скрейпинга практической части урока, 
проведите скрейпинг сайта с новостями из сферы ИИ (https://2051.vision/category/ii/), 
выведите на экран заголовки новостей."""

from bs4 import BeautifulSoup
import requests

url = ("https://2051.vision/category/ii/")
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html5lib')

headlines = soup.find_all("h3")

for i, h in enumerate(headlines, 1):
    print(f"{i}. {h.get_text(strip=True)}")