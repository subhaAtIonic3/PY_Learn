class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")


b = Book(title="ReactJS", author="Facebook", pages=300)

print(b)
print(len(b))

# Delete variables from computer memory

del b

# print(b)  # cause an error because b has already been deleted
