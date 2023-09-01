#Multiply results to 100; for example if it's 0.75 then your Loan to Value is 75%

print('''
Loan to Value Calculator
========================
''')
restart = "y"
def ltv_calc():
    loan_amount = input("Enter Loan Amount: ")
    loan_amount = float(loan_amount)
    appraised_property_value = input("Enter Appraised Property Value: ")
    appraised_property_value = float(appraised_property_value)
    
    print('''
    Here is your loan to value percentage:
    ''')
    print(loan_amount/appraised_property_value)
while restart == "y":
    ltv_calc()
    continue_question = input('''
    Do you want to continue? Y/N: ''').lower()
    restart = continue_question
    if restart == "y":
     continue
else:
    print('''
        Goodbye!''')