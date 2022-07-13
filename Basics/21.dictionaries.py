# def a dictionary
customer = {
    "name": "John Doe",
    "age": 30,
    "is_verified": True
}
# print key name:
name = customer["name"]
print(f'Name : {name}')
# wrong key will throw a error
#     print(customer["Name"])
#     KeyError: 'Name'

# prevent error
birth_day = customer.get("birthday")
print(f'Bithday: {birth_day}') # returns None
# assign default value to key if missing:
birth_day_with_default = customer.get("Birthday","Jan 1 1969")
print(f'Bithday with default: {birth_day_with_default}')

# add key value pair to existing dictionary:
customer["birthday"] = "Jan 1 1990"
birthdate = customer.get("birthday")
print(f'Birthday: {birthdate}')