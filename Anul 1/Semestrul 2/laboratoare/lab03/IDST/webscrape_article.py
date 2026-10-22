import requests
from bs4 import BeautifulSoup

url = "https://medium.com/analytics-vidhya/web-scraping-with-python-beginner-to-advanced-10daaca021f3"
response = requests.get(url)
html_content = response.content  # HTML content of the page
soup = BeautifulSoup(html_content, "html.parser") #this is the first step in using BeautifulSoup

titles = soup.find_all("h1")
print(len(titles))
print()

for title in titles:
    print(title.text)
    print()
