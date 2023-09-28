# Prompt the user to enter time in seconds
value = int(input("enter time in seconds: "))

# Assign hour, min, sec
sec = (value % 60)
min = (value//60)
value = value % 3600

# Display results
print("m:s")
print("%d:%d"%(min, sec))

