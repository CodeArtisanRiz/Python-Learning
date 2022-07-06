# assign input variable
name = input("Enter your name: ")
# logic starts here
if len(name) < 3:
    print("Name must be atleast 3 characters")
elif len(name) > 50:
    print("Name can be maximum of 50 characters")
else:
    print("Name looks good")