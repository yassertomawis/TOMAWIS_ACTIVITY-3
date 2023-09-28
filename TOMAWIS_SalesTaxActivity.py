# Prompt the user to enter purchase value
Value = eval(input("Enter purchase value: "))

# Compute Sales Tax
Tax = (0.06 * Value)

# Display results
print("Sales tax is " + str(round(Tax, 2)))
