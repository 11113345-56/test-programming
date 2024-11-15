def find_largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# numbers
numbers = [1, 2, 3, 4, 5, 6]

# finding  largest number
print(find_largest_number(numbers))  
