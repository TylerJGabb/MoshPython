values = [*range(5), *"Hello"]
print(values)

first = [1, 2]
second = [3]
combined = [*first, *second]
print(combined)

d1 = {"x": 1}
d2 = {"x": 2, "y": 3}
combined = {**d1, **d2}
print(combined)
