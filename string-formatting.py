print("This is a string {}".format("Test"))

print("The {2} {1} {0}".format("fox", "brown", "quick"))

print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))

result = 102 / 444
print("The result is {r}".format(r=result))
# formatting follows {value:width.precission f}
print("The result is {r:1.3f}".format(r=result))
print("The result is {r:10.3f}".format(r=result))
# formatted string literals
name = "Subha"
print(f"My name is {name}")
