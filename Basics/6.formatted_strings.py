# define variables
first_name = "H M Rizwan"
last_name = "Mazumder"
# traditional concatenation
message = first_name + " [" + last_name + "] is a coder"
print(message)
# concatenation using formatted string : prefix your string with a 'f' & use '{}' to insert strings dynamically
formatted_string = f'{first_name} [{last_name}] is a coder'
print(formatted_string)