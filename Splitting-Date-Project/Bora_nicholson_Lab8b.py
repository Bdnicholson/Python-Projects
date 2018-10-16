def main():
    Date = input("Please enter a date MM/DD/YY: ")
    Date_Split = Date.split("/")
    print ("Month: ", Date_Split [0])
    print ("Day: ", Date_Split [1])
    print ("Year: ", Date_Split [2])
    Month = Date_Split[0]
    Day = Date_Split[1]
    Year = Date_Split[2]

    if Month > "12" or Month < "01":
        print ("Please enter a month between 1 and 12")
        return main()
    if Day > "31" or Day < "01":
        print ("Please enter a date betwween 1 and 31")
        return main()
    elif len(Year) > 2:
        print ("The year must be two digits")
        return main()
    elif Year != "13":
        print ("Year must be 2013!")
        return main()
    else:
        date_output(Month, Day, Year)

def date_output(Month, Day, Year):
    if Month == "01":
        Month = "January"
    if Month == "02":
        Month = "February"
    if Month == "03":
        Month = "March"
    if Month == "04":
        Month = "April"
    if Month =="05":
        Month = "May"
    if Month == "06":
        Month = "June"
    if Month == "07":
        Month = "July"
    if Month == "08":
        Month = "August"
    if Month == "09":
        Month = "September"
    if Month == "10":
        Month = "October"
    if Month == "11":
        Month = "November"
    if Month == "12":
        Month = "December"
    if Year == "13":
        Year = "2013"
    print ("The date is:", Month + " " + Day + ",", Year)
main()
