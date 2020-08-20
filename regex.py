import re

text = "this is a simple text"

find_txt = re.search("is a s", text)
print(find_txt)
print(find_txt.span())
print(find_txt.start())
print(find_txt.end())

phone_number = "this is a phone number: 222-522-9132"
print(re.search(r"\d{3}-\d{3}-\d{4}", phone_number))

phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
result = re.search(phone_pattern, phone_number)
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group(3))


text_two = "phone one, phone twice"
match_tx = re.findall("phone", text_two)
print(match_tx)

for match in re.finditer("phone", text_two):
    print(match.group())
    print(match.span())
    print(match.start())
    print(match.end())


print(re.search(r"cat|dog", "The dog is here"))

# wildcard check
print(re.findall(r".at", "the cat in the hat sat there"))

# starts with and ends with
print(re.findall(r"^\d$", "2 is the number"))  # starts with
print(re.findall(r"\d$", "the number 2"))  # ends with

# exclude digits
phrase = "this is a list of 2's"
pattern = r"[^\d]+"
print(re.findall(pattern, phrase))


punctuation_str = "This is a String! with punctuation. How can we remove that?"
str_pattern = r"[^!.? ]+"
print(" ".join(re.findall(str_pattern, punctuation_str)))


text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
new_pattern = r"[\w]+-[\w]+"
print(re.findall(new_pattern, text))


# Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

print(re.search(r"cat(fish|nap|claw)", text))
print(re.search(r"cat(fish|nap|claw)", texttwo))
print(re.search(r"cat(fish|nap|claw)", textthree))
