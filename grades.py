
#Annias Scott
#Lab 4


def main():

    print("")
    print("> The program reads the grades.txt file. The Programe records in each line from grades.txt.")
    print("Next the grade entry from each line of grades.txt is set in grades.py.")
    print("The average of all students combined is calculated by grades.py. <")
    print("")
    #Reads grades.txt
    #writes text entries into a list:
    with open("grades.txt") as f:
        data = f.readlines()
        print ("")
       

    #Splitting strings into proper variables.
    Mick = data[0]
    #print(Mick)
    Jane = data[1]
    #print(Jane)
    Minnie = data[2]
    #print(Minnie)
    Donald = data[3]
    #print(Donald)
    Daffy = data[4]
    #print(Daffy)


    print ("Name                   Grade")
    print("")
    print("__ __ __ __ __ __ __ __ __ __ __ __ __")
    print("")

    #Mickey split and converstion to integer
    MickGradeVar = Mick.split(",")
    MickeyRaw = int(MickGradeVar[2])
    print("Mickey's Grade is: ", MickeyRaw)
    print("")


    #Jane split and converstion to integer
    JaneGradeVar = Jane.split(",")
    JaneRaw = int(JaneGradeVar[2])
    print("Jane's Grade is: ",JaneRaw)
    print("")


    #Minnie split and converstion to integer
    MinnieGradeVar = Minnie.split(",")
    MinnieRaw = int(MinnieGradeVar[2])
    print("Minnie's Grade is: ",MinnieRaw)
    print("")


    #Donald split and converstion to integer
    DonaldGradeVar = Donald.split(",")
    DonaldRaw = int(DonaldGradeVar[2])
    print("Donald's Grade is: ", DonaldRaw)
    print("")


    #Daffy split and converstion to integer
    DaffyGradeVar = Daffy.split(",")
    DaffyRaw = int(DaffyGradeVar[2])
    print("Daffy's Grade is: ",DaffyRaw)
    print("")



    #Caclulating the average grade of the 5 students
    CourseAverage = (MickeyRaw + JaneRaw + MinnieRaw + DonaldRaw + DaffyRaw)/5
    print("")
    print("")
    print ("The course average grade is: ", CourseAverage)
    print("")


main()
