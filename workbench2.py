def total_values(l):
    total = 0
    for value in l:
        total += value
    return total

numbers = [10, 20, 30, 40, 50]
print("List: ", numbers)

print("Total nilai dalam list: ", total_values(numbers))