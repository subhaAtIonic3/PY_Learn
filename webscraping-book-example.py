import bs4
import requests
import lxml


base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# result = requests.get(base_url.format(1))
# soup = bs4.BeautifulSoup(result.text, "lxml")
# book = soup.select(".product_pod")[0]

# star = book.select(".star-rating.Three")[0]
# book_title = book.select("a")[1]["title"]


two_star_title = []

for n in range(1, 51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, "lxml")

    books = soup.select(".product_pod")
    for book in books:
        if len(book.select(".star-rating.Two")):
            two_star_title.append(book.select("a")[1]["title"])

print(len(two_star_title))
