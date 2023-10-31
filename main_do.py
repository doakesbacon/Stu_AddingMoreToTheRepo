# @TODO: Write a function that returns the arithmetic average for a list of numbers


def average(numbers):
    if len(numbers)  == 0:
        return 0
    total = sum(numbers)
    return total / len(numbers)

# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))

