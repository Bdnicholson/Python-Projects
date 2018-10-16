Student = 12
NameList = []
NameList_Tuple = []
def main():
#NameList
    Get_Name()
    print (NameList)
#SortList
    Sort_List ()
    print("Alphabetical NameList: ", NameList)
#ReverseList
    Reverse_Sort_List ()
    print("Reversed NameList: ", NameList)
#Ask for instructor's name
    Instr_Name()
    print (NameList)
#Insert my name
    My_Name()
    print("The list after insert: ", NameList)
#Open a file for writing
    write_file ()
#Convert list to tuple
    Convert_Tuple ()
#Get name
def Get_Name():
    for Name in range (Student):
        Name = Name +1
        Name = input("Enter the students name: ")
        NameList.append(Name)
#Sort
def Sort_List():
    NameList.sort()
#Reverse sort
def Reverse_Sort_List():
    NameList.reverse()
#Get instructor's name
def Instr_Name():
    Instr_Name = input("Enter the instructor's name: ")
    NameList.append(Instr_Name)
#Get my name
def My_Name():
    My_Name = input("Enter your name: ")
    NameList.insert(0, My_Name )
#Write file
def write_file():
    Outfile = open("names.txt",'w')
    for Name in NameList:
        Outfile.writelines(Name +'\n')
    Outfile.close()
#Convert tuple
def Convert_Tuple ():
    NameList_Tuple = tuple(NameList)
    print ("Converted to tuple: ", NameList_Tuple)
main()
