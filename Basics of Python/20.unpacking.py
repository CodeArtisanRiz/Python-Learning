# def a tuple
coordinates_tuple = (1, 2, 3)
# def a list
coordinates_list = [1, 2, 3]
# unpacking
a, b, c = coordinates_tuple
x, y, z = coordinates_list
# it will act just like:
#     x = coordinates[0]
#     y = coordinates[1]
#     z = coordinates[2]

print(f'a: {a} b: {b} c: {c}')
print(f'x: {x} y: {y} z: {z}')
