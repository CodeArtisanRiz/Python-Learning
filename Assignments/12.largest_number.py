# def list of numbers
list_of_numbers = [1, 3,9,4,74,6,11]
# def first no as largest no
largest_no = list_of_numbers[0]
# loop over the list
for item in list_of_numbers:
    if item > largest_no:
        largest_no = item
print(largest_no)