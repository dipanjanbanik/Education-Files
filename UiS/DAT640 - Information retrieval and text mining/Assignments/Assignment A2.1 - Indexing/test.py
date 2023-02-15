from collections import Counter

a = Counter("missisipi")
b = Counter("bangladesh")
c = {"body": a, "title": b}

for key in c:
    for x, y in key.items():
        print(x)
