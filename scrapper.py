import requests
from bs4 import BeautifulSoup

url = "https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?locations=IN"

# get the html content
req = requests.get(url)
htmlContent = req.content


# parse the html
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify())
exit()
anchors = soup.find_all('a') #finds all the anchor tags
all_links = set()

#getting all the links on the page
for link in anchors:
    if(link.get('href') != '#'):
        linkTx = "https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?locations=IN" + link.get('href')
        all_links.add(linkTx)

for lin in all_links:
    print(lin)

