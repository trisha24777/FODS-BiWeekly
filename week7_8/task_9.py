"""
Program: Perform multiple operations on employee DataFrame

"""

import pandas as pd

# Create a dictionary containing employee data
data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['John Smith', 'Alice Brown', 'Bob White', 'Emma Green', 'Charlie Red'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'Age': [30, 28, 35, 40, 25],
    'Salary': [70000, 60000, 80000, 90000, 55000],
    'JoinDate': pd.to_datetime(['2018-07-15', '2020-03-10', '2016-11-01', '2012-05-25', '2021-06-01']),
    'ExperienceYears': [5, 3, 7, 11, 2]
}

# Create DataFrame from the dictionary
df = pd.DataFrame(data)

# a. Display Name and Salary columns
print("a. Name and Salary Columns:\n", df[['Name', 'Salary']])

# b. Filter employees in IT department
print("\nb. IT Department:\n", df[df['Department'] == 'IT'])

# c. Find employees older than 30 and calculate average salary by department
older_than_30 = df[df['Age'] > 30]
print("\nc. Older than 30:\n", older_than_30)
print("Average salary by department:\n", df.groupby('Department')['Salary'].mean())

# d. Count employees in each department
print("\nd. Count per department:\n", df['Department'].value_counts())

# e. Calculate and add a 10% bonus column
df['Bonus'] = df['Salary'] * 0.10
print("\ne. With Bonus:\n", df[['Name', 'Bonus']])

# f. Replace 'HR' with 'Human Resources' in Department column
df['Department'] = df['Department'].replace('HR', 'Human Resources')
print("\nf. Replaced Department:\n", df['Department'])

# g. Find employee(s) with longest tenure (earliest join date)
longest_tenure = df[df['JoinDate'] == df['JoinDate'].min()]
print("\ng. Longest Tenure:\n", longest_tenure)

# h. Categorize salaries as High (>75000) or Low
df['SalaryCategory'] = df['Salary'].apply(lambda x: 'High' if x > 75000 else 'Low')
print("\nh. Salary Category:\n", df[['Name', 'SalaryCategory']])

# i. Remove any duplicate EmployeeID entries
df = df.drop_duplicates(subset='EmployeeID')
print("\ni. After Removing Duplicates:\n", df)

# j. Calculate the median age of employees
print("\nj. Median Age of Employees:", df['Age'].median())
