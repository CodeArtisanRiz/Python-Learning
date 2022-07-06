price_of_house = 1000000
is_buyer_has_good_credit = False
#
if is_buyer_has_good_credit:
    down_payment = 0.1 * price_of_house
else:
    down_payment = 0.2 * price_of_house
print(f"The Down Payment is : {down_payment}")