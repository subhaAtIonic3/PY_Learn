import csv

data = open("example.csv", encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)
# print(data_lines)

# for line in data_lines[0:5]:
#     print(line)

all_names = []
for line in data_lines[1:10]:
    name = line[1] + " " + line[2]
    all_names.append(name)

print(all_names)

file_to_output = open("to_save_file.csv", mode="w", newline="")
csv_writer = csv.writer(file_to_output, delimiter=",")

csv_writer.writerows([["a", "b", "c"], [1, 2, 3], [4, 5, 6]])
file_to_output.close()


f = open("to_save_file.csv", mode="a", newline="")
csv_writer = csv.writer(f, delimiter=",")

csv_writer.writerow(["pp", "oo", "ii"])
f.close()
