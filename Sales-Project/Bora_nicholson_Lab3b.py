#Get Name
Name = input('What is your name: ')
#Sales
Sales = float(input('What are your Sales? '))
if Sales < 10000:
    Commission = 0
    Bonus = 0
elif 10000 <= Sales < 100000:
    Commission = Sales * 0.02
    Bonus = 0
elif 100001 <= Sales < 500000:
    Commission = Sales * 0.15
    Bonus = 1000
elif 500001 <= Sales < 1000000:
    Commission = Sales * 0.28
    Bonus = 5000
else:
    Commission = Sales * 0.35
    Bonus = 100000
#Longevity
Longevity = int(input('How long have you been with the company?(in months): '))
if Longevity >60 and Sales > 100000:
    Newbonus = Bonus + 1000
else:
    Newbonus = Bonus
#Vacation
Vacation = int(input('How many vacation days did you take: '))
Base_Salary = 2000
if Vacation >3:
    Base_Salary = Base_Salary -200
#Paycheck
Paycheck = Base_Salary + Commission + Newbonus
#Print Results
print('Name: ',Name)
print('commission: $', Commission)
print('bonus: $', Newbonus)
print('The employee took', Vacation, 'days vacation')
print('total gross paycheck: $', Paycheck)
