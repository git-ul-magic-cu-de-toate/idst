import requests
from bs4 import BeautifulSoup

url = "https://ro.wikipedia.org/wiki/Rom%C3%A2nia"
response = requests.get(url)
html_content = response.content  # HTML content of the page
soup = BeautifulSoup(html_content, "html.parser") #this is the first step in using BeautifulSoup

title = soup.find("h1")   # finds all primary titles (this can be any number from 1->6)
title2 = soup.title
print(title2.text)
print()

paragraph = soup.find("p") # the content of the first paragraph
print(paragraph)
print()

image = soup.find("img")  # Finds the first <img> and extracts the information about it as a dictionary
print(image['src']) #extract the URL of the image
print()

link = soup.find("a")  # Finds the first <a> (anchor) tag
print(link['href'])  # Prints the URL of the link
print()

list_item = soup.find("li") #The first list item\
print(list_item)
print()

# Extract all paragraph (<p>) elements
paragraphs = soup.find_all("p")  # Finds all <p> tags on the page
# paragraphs is a list!

# Iterate over each paragraph and print its text content
for paragraph in paragraphs:
    print(paragraph.text)
