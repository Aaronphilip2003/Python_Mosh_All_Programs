# if applicant has a high income and/or a good credit then eligible
# if applicant has a high income and no criminal record then eligible
high_income= False
good_credit = True
criminal_record=False
if high_income or good_credit and not criminal_record:
    print("Eligible")
else:
    print("Not Eligible")

