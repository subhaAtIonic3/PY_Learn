import shutil
import os
import re

shutil.unpack_archive("unzip_me_for_instructions.zip", "puzzle-dir", "zip")

with open("puzzle-dir/extracted_content/Instructions.txt") as f:
    content = f.read()
    print(content)

phone_number_list = []


def search(text, pattern=r"\d{3}-\d{3}-\d{4}"):
    # print(text)
    if re.search(pattern, text):
        match_str = re.search(pattern, text)
        phone_number = match_str.group()
        phone_number_list.append(phone_number)


for folder, sub_folders, files in os.walk("puzzle-dir"):
    print(f"currently looking at {folder}")
    for f in files:
        with open(os.getcwd()+"/"+folder+"/"+f, "r+") as text_file:
            search(text_file.read())

print(phone_number_list and phone_number_list[0])
