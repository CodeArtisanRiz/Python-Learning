num_list = [2, 3, 8, 9, 8, 11]
numbers = num_list.copy()
print(f'Original Number List: {num_list}')

# reverse the list to remove duplicate no from the end
num_list.reverse()
# remove duplicate no
for item in num_list:
    if num_list.count(item) > 1:
        print(item)
        num_list.remove(item)
# reverse the list the already reversed list
num_list.reverse()
print(f'Number List after duplicate removed:{num_list}')

# alternate method using second variable
print("\nUsing second variable:\n")
uniques = []
for num in numbers:
    if num not in uniques:
        uniques.append(num)
print(f'Number List after duplicate removed:{uniques}')

