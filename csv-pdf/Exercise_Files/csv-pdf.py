import csv
import PyPDF2
import requests
import re

file_data = open("find_the_link.csv", encoding="utf-8")
csv_reader = csv.reader(file_data)
data_lines = list(csv_reader)

col_len = len(data_lines[0])

link_url = ""
counter = 0

for row in data_lines:
    link_url += row[col_len - col_len + counter]
    counter += 1

print(link_url)
file_data.close()

# pdf downloaded but not opening
# res = requests.get(link_url)
# print(res)

# with open("dwnld.pdf", "wb") as f:
#     f.write(res.content)

pdf_file = open("Find_the_Phone_Number.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
print(pdf_reader.numPages)

all_text = ""
for page in range(pdf_reader.numPages):
    page_data = pdf_reader.getPage(page)
    text = page_data.extractText()
    all_text += "\n" + text

match = re.search(r"\d{3}\W\d{3}\W\d{4}", all_text)

if match:
    phone_number = match.group()
    print(phone_number)
else:
    print("Phone number not found")

pdf_file.close()
