import zipfile
import shutil
import os

with open("fileone.txt", "w+") as f:
    f.write("Test one file")

with open("filetwo.txt", "w+") as f:
    f.write("Test two file")

comp_file = zipfile.ZipFile("comp_file.zip", "w")
comp_file.write("fileone.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.write("filetwo.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile("comp_file.zip", "r")
zip_obj.extractall("extracted_content")


dir_location = os.getcwd() + "/extracted_content"
shutil.make_archive("example", "zip", dir_location)

shutil.unpack_archive("example.zip", "final_unzip", "zip")
