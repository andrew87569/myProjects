# Use the BeautifulSoup and requests Python packages 
# to print out a list of all the article titles on the New York Times homepage.

from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

articles = []

for article in soup.find_all(class_="esl82me0"):
    article = article.string
    articles.append(article)

print(articles)