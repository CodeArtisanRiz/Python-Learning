# Get weight type
weight_type = input("(L)bs or (K)g: ")
# Get input weight
weight = input("Weight: ")
# logic
if type(weight) != int or float:
    print("Enter a valid number.")
else:
    if weight_type.upper() == "L":
        converted_weight = float(weight) * 0.5 # converted_weight is converted from str to float
    elif weight_type.upper() == "K":
        converted_weight = float(weight) / 0.5  # converted_weight is converted from str to float
    else:
        converted_weight = "Error.."
    print(converted_weight)