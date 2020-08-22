import bs4
import requests
import lxml

result = requests.get("https://en.wikipedia.org/wiki/MacBook_Air")
print(type(result))

soup = bs4.BeautifulSoup(result.text, "lxml")
title = soup.select("title")[0].getText()
css_class_name = soup.select(".toctext")[0].getText()
mac_img = soup.select(".thumbimage")[0]
print(title)
print(css_class_name)
print(mac_img["src"])
image_link = requests.get(f"https:{mac_img['src']}")

# write binary so use mode=wb
with open("mac_image.jpg", "wb") as f:
    f.write(image_link.content)

print(type(soup.select("title")[0]))
