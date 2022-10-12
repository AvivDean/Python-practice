income = int(input("Enter your income: "))
tax_payable = 0
print("Given income is: ", income)

if income <= 10000:
    tax_payable = 0
elif income <=20000:
    x = income-10000
    tax_payable = x * 10 / 100
else:
    tax_payable = 10000 * 10 / 100
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is: $", tax_payable)