# def both variables
has_high_income = True
has_good_credit = False
has_criminal_record = True
# and: if both true
if has_high_income and has_good_credit:
    print("Eligible for loan.")
# or: if atleast one true
if has_high_income or has_good_credit:
    print("Eligible for loan.")
# not: inverse boolean value
if has_good_credit or not has_criminal_record:
    print("Eligible for loan.")