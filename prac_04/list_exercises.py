"""
List operations
"""

NUMBER_OF_REPETITIONS = 5

numbers = []
for i in range(NUMBER_OF_REPETITIONS):
    numbers.append(int(input('Enter a number: ')))

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average number is {sum(numbers) / NUMBER_OF_REPETITIONS}")
