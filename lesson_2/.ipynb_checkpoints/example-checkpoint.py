numbers = [1, 2, 3, 4, 5]
i = 1
saved_n = numbers[i]

while i <= len(numbers):
    n = numbers[i]
    if n > saved_n:
        saved_n = n
    i += 1

print(saved_n)