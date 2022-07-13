numbers = [1, 1, 1, 1, 5]
for count in numbers:
    output = ""
    for p_count in str(count):
        output = int(p_count) * "*"
        print(output)