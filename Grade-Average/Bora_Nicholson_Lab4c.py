#Define Everything
I = 0
Grade = 0
Total = 0
#Grade Loop
while Grade != -1:
    Grade = int (input("Type a Grade: "))
    if Grade >= 90:
        print ("Your grade is an A")
    elif Grade < 90 and Grade >= 80:
        print ("Your grade is a B")
    elif Grade < 80 and Grade >=70:
        print ("Your grade is a C")
    elif Grade < 70 and Grade >= 60:
        print ("Your grade is a D")
    else:
        print ("Your grade is an F")
#Define and print
    I=I+1
    Total = Total + Grade
    print ("Number of entries: " ,I-1)
    print ('The total is: ' ,Total+1)
    Average = (Total / I)+1
    print ('The average grade is: ' , Average)
