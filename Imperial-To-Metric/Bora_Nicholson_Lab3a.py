print('Hello, Please input the Imperial values!')
#Miles
Miles = float(input('Miles to Kilometers: '))
totalKilometers = (1.6 * Miles)
if Miles < 0:
     print('Please no negative numbers')
else:
    if Miles > 0:
        print("The metric conversion is ", totalKilometers)
#Fahrenheit
Fahrenheit = float(input('Fahrenheit to Celsius: '))
totalCelcius = ((Fahrenheit - 32) * 5/9 )
if Fahrenheit < 0 or Fahrenheit > 1000:
    print('Please check your Fahrenheit number, It must be greater than 0 and less than 1000')
else:
    if Fahrenheit > 0 or Fahrenheit < 1000:
       print("The metric conversion is ", totalCelcius)
#Gallons
Gallons = float(input('Gallons to Liters: '))
totalLiters = (3.9 * Gallons)
if Gallons < 0:
    print('Please no negative numbers')
else:
    if Gallons > 0:
        print("The metric conversion is ", totalLiters)
#Pounds
Pounds = float(input('Pounds to Kilograms: '))
totalKilograms = (.45 * Pounds)
if Pounds < 0:
    print('Please no negative numbers')
else:
    if Pounds > 0:
      print("The metric conversion is ", totalKilograms)
#Inches
Inches = float(input('Inches to Cenitmeters: '))
totalCentimeters = (2.54 * Inches)
if Inches < 0:
    print('Please no negative numbers')
else:
    if Inches > 0:
        print("The metric conversion is ", totalCentimeters)
        
