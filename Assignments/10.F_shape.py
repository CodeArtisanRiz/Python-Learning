# without list of numbers
for x5 in range(2):
    print("x" * 5)
    for x2 in range(1):
        print("x" * 2)
print("x" * 2)
# space
print("")
# with list of numbers
numbers = [5, 2, 5, 2, 2]
for x in numbers:
    print("x" * int(x))
print("")
# nested loops with list of numbers
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)


