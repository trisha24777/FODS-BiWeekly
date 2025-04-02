''' Program to calculate simple interest '''
principle = float(input("Enter principle amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time period in years: "))
interest = (principle * rate * time) / 100
print("Simple Interest:", interest)