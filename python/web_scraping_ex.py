# https://nbviewer.jupyter.org/github/humanitiesprogramming/humanitiesprogramming.github.io/blob/master/python/notebooks/intro-to-scraping.ipynb

from bs4 import BeautifulSoup
from urllib import request

url = "https://github.com/humanitiesprogramming/scraping-corpus"

#print (url)
# print(url)

# modify the URL
# print(url + "/subdomain")

# uses a python package named request, takes the link stored at the variable 'url', visits it, reads it back, and stores in a new variable named html
html = request.urlopen(url).read()
# print(html[0:2000])

# takes html pulled and turns into a beautiful soup object
soup = BeautifulSoup(html, 'lxml')

# # to get all the links
# print(soup.find_all('a')[0:10])

# # to get all the text
# print(soup.text[0:2000])
# # to strip out the '\n' characters
# print(soup.text.replace('\n', ' ')[0:1000])

# # Output: 'ResultSet' - not a beautiful soup object
# print(type(soup.find_all('a')).__name__)

# # Output: 'Tag'
# print(type(soup.find_all('a')[0]).__name__)

# # Output: 'Skip to content'
# print(soup.find_all('a')[0].text)

# to find out how many links are on this pages
# print(len(soup.find_all('a')))

# get text for each individual item, add formatting, and strip out whitespace
# for item in soup.find_all('a')[0:10]:
#     print('=======')
#     print(item.text.replace('\n', ''))

# pull down links ('a') within 'td' tags with the 'content' class selector
# for link in soup.select("td.content a"):
#     print(link.text)

# collect the above links and store in a list to scrape
# links_html = soup.select('td.content a')
# urls = []
# for link in links_html:
#     url = link['href']
#     urls.append(url)
# print(urls)

# to strip github formatting (modify url by taking out 'blob')
links_html = soup.select('td.content a')
urls = []
for link in links_html:
    url = link['href'].replace('blob/', '')
    urls.append("https://raw.githubusercontent.com" + url)
# print(urls)

corpus_texts = []
for url in urls:
    print(url)
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    text = soup.text.replace('\n', '')
    corpus_texts.append(text)

print(corpus_texts)
