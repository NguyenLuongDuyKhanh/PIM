counter = 0
def count():
    for x in range(3):
        for y in range(4):
            counter += 1

count()
print(counter)