# Need to close the file after opening
my_file = open("test.txt")
print(my_file.read())

# reset the cursor
my_file.seek(0)
print(my_file.read())

my_file.seek(0)
print(my_file.readlines())
#  close the file
my_file.close()

# No need to close the file now.
with open("test.txt") as my_file_two:
    content = my_file_two.read()

print(content)

#  file open modes
#  r for read
#  w for write if file not created it will create a new one
#  a for append

with open("test_2.txt", mode="r") as f:
    print(f.read())

with open("test_2.txt", mode="a") as f:
    f.write("\n LINE FOUR")

with open("test_2.txt", mode="r") as f:
    print(f.read())

# with open("test_3.txt", mode="w") as target:
#     f.write("Newly created file")
    # lines = ["LINE ONE \n", "LINE TWO \n"]
    # f.writelines(lines)
