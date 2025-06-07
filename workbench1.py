import random

scores = [random.randint(0, 100) for _ in range(10)]
print("Original scores: ", scores)

scores.sort()
print("Sorted ascending: ", scores)

scores.reverse()
print("Sorted descending: ", scores)

print("Maximum score: ", scores[0])