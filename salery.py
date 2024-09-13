# data input statments
salary = float(input("Enter your salary: "))
numDependents = float(input("Number of dependents: "))

# tax calculation
stateTax = salary * 0.065  # 6.5% state tax
federalTax = salary * 0.28  # 28.0% federal tax
dependentDeduction = salary * 0.025 * numDependents  # 2.5% per dependent

# total withholding and take-home pay calculations
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

# output statements
print("Salary: $" + str(salary))
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependent Deduction for " + str(numDependents) + " dependents: $" + str(dependentDeduction))
print("Total Withholding: $" + str(totalWithholding))
print("Take Home Pay: $" + str(takeHomePay))
