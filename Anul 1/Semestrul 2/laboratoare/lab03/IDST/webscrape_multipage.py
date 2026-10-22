import requests
from bs4 import BeautifulSoup

# Base URL for pagination, with a placeholder for the page number
base = "https://htmlburger.com/sitemap"
base_url = "https://htmlburger.com"

response = requests.get(base)
html_content = response.text  # HTML content of the page
soup = BeautifulSoup(html_content, "html.parser") #this is the first step in using BeautifulSoup

links = soup.find_all("a")

for link in links:
	try:
		url = f'{base_url}{link['href']}'
		response_2 = requests.get(url)
		html_content_2 = response_2.text
		soup_2 = BeautifulSoup(html_content_2, "html.parser")
		title = soup_2.title
		print(title.text)
		print()
	except:
		print("error")
		print()
