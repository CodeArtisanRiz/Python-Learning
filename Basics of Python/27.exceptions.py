try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
# accepts error of type ValueError
except ValueError:
    print("Invalid value")
# accepts error of type ZeroDivisionError
except ZeroDivisionError:
    print("Age cannot be 0")
