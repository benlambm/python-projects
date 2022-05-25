
# https://docs.python.org/3/library/functions.html#enumerate

values = ["cat", "dog", "bird"]

for value in values:
    print(value)

# classic pattern
i = 0
for value in values:
    print(i, value)
    i = i + 1

# [(0,"cat")(1,"dog")(2,"bird")]
for i, value in enumerate(values):
    print(i, value)
    