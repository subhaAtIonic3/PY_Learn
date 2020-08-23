import requests
import bs4
import lxml

base_url = "http://quotes.toscrape.com/page/{}/"

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, "lxml")

authors = soup.select(".author")

quotes = soup.select(".text")

tag_box = soup.select(".col-md-4.tags-box")[0]
tags = tag_box.select(".tag")

unique_authors = set()
quotes_list = []

for author in authors:
    unique_authors.add(author.text)

for quote in quotes:
    quotes_list.append(quote.text)

for tag in tags:
    print(tag.text)

print(unique_authors)
print(quotes_list)

is_empty = False
page_count = 1
author_set = set()
while not is_empty:
    c_res = requests.get(base_url.format(page_count))
    c_soup = bs4.BeautifulSoup(c_res.text, "lxml")

    print(base_url.format(page_count))

    if "No quotes found!" in str(c_soup):
        print("condition false")
        is_empty = True
    else:
        c_authors = c_soup.select(".author")
        page_count += 1
        for c_author in c_authors:
            author_set.add(c_author.text)

print(author_set)
