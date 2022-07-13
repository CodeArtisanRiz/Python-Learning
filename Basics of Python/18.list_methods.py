# def list
numbers = [5, 6, 8, 11, 8, 4]
print(f'Numbers: {numbers}')
# insert number at the end
numbers.append(20)
print(f'Added 20 in last position: {numbers}')
# insert number at specific position
numbers.insert(2, 41)
print(f'Added 41 in pos 2: {numbers}')
# remove last no from list
numbers.pop()
print(f'Numbers: {numbers}')
# check index of a number
print(f'Index of 8: {numbers.index(8)}')
# index : returns boolean
print(f'Boolean: {64 in numbers}')
# count no of occurrence
print(f'Occurrence of Number 8: {numbers.count(8)}')
# sort
numbers.sort()
print(f'Sorted Numbers: {numbers}')
# reverse
numbers.reverse()
print(f'Reversed Numbers: {numbers}')
# Make a copy
copy_numbers = numbers.copy()
print(f'Copied Numbers: {copy_numbers}')
# clear all numbers
numbers.clear()
print(f'Empty list: {numbers}')