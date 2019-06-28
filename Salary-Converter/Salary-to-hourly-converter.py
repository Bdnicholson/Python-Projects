yearly_salary = input('What is your yearly salary? ') # Get the yearly salary

monthly_salary = (float(yearly_salary) // 12 ) # Convert yearly to monthly

print('This is your monthly salary: ' , monthly_salary) # Print the conversion

weekly_salary = (monthly_salary / 4)

print('This is your weekly salary: ', weekly_salary)

hourly = (weekly_salary / 40)

print('This is your hourly rate: ', hourly)
