my_list = [1, 2, 3]
print(len(my_list))

my_list_two = ["One", "Two", "Three"]
print(my_list_two[1:])
another_list = ["Four", "Five"]
new_list = my_list_two + another_list
print(new_list)

new_list[0] = new_list[0].upper()
print(new_list)
new_list.append("Six")
print(new_list)

popped_item = new_list.pop()
print(popped_item)

new_list.pop(0)
print(new_list)

new_list_rev = new_list[::-1]
print("List reverse =>", new_list_rev)

list_alphabet = ['a', 'h', 'w', 'b', 'c']
list_alphabet.sort()
print(list_alphabet)

rev_string = ['s', 'u', 'b', 'h', 'a']
rev_string.reverse()
print(rev_string)

# Pallindrom check
pallindrom_string = "maddam"
pallindrom_List = list(pallindrom_string)

rev_pallindrom_list = pallindrom_List
rev_pallindrom_list.reverse()

new_string = "".join(rev_pallindrom_list)
print("new_string =>", new_string)

isPallindrom = (new_string == pallindrom_string)
print(isPallindrom)

# Nested list
nested_list = [1, 2, [3, 4]]
print(nested_list[2][1])
