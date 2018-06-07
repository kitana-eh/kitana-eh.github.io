# # exercise 1 from https://nbviewer.jupyter.org/github/humanitiesprogramming/humanitiesprogramming.github.io/blob/master/python/notebooks/intro-to-scraping.ipynb
# from bs4 import BeautifulSoup
# from urllib import request
#
# url = "http://www.casebook.org/press_reports/alderley_and_wilmslow_advertiser/881019.html"
# html = request.urlopen(url).read()
# soup = BeautifulSoup(html, 'lxml')
# body_text = soup.select('div#content')
# clean_text = body_text[0].text
#
# print(clean_text)

# exercise 2
# from bs4 import BeautifulSoup
# from urllib import request
#
# url = "http://www.casebook.org/press_reports/alderley_and_wilmslow_advertiser/"
# html = request.urlopen(url).read()
# soup = BeautifulSoup(html, 'lxml')
# raw_links = soup.select('div#content a')
# clean_links = [link['href'] for link in raw_links]
# final_links = ["http://www.casebook.org/" + link for link in clean_links]
# print(final_links)

# exercise 3
from bs4 import BeautifulSoup
from urllib import request

url = "http://www.casebook.org/press_reports/alderley_and_wilmslow_advertiser/"
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')
links_html = soup.select('div#content a')
urls = []
for link in links_html:
    url = link['href']
    urls.append("http://www.casebook.org/" + url)

corpus_texts = []
for url in urls:
    print(url)
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    text = soup.text.replace('\n', '')
    corpus_texts.append(text)
print(corpus_texts)
