#Grades.py
#IT1113/ Section W04
#Lab04
#09/18/2022
#This program gets students name and
#calculates their average grade.
#By submitting this assignemnt, I am verifyinh that all
#all program code was creadted by me only.

#Give Value to variable
a_grade= 90.00
b_grade=80.00
c_grade=70.00
d_grade=60.00
f_grade=60.00

next_student='y'


while next_student=='y':
    def main():
        # Ask students name
        names=enter_names()
        #Calculate their average
        test_score=calc_average()
        #Find Grade Letter
        letters=determine_grade ()
        #Display name, average, and grade letter
        print(names,test_score)
        #Ask for another student
    next_student= input('Next Student? (y/n):     ')  
          
    
    
    def enter_names():
        #Input the names of the students 
        first_name= input('Enter First Name:          ')
        last_name= input('Enter Last name:           ')
        print()
        #Return the name
        return last_name,first_name
   
    #Caluclate the average of a student
    def calc_average():
        max = 8 # This is th max number of grades inputed.
        sum=0 #Initilaize Accumlator variable
        for grades_score in range(max):
            number= int(input('Enter Test Score:     '))
            sum= sum + number
            average=sum/8.0
        print('The total average is', average)
        #return the average
        return average 
    
        
    #Determine the grade letter
    def determine_grade():
        student_average= float(input('Enter Student\'s average:          '))
        format(student_average,',.2f')
        if student_average >= a_grade:
            print('Grade Letter is: A')
        else:
            if student_average >= b_grade:
                print( 'Grade Letter is: B')
            else:
                if student_average >= c_grade:
                    print( ' Grade Letter is: C')
                else:
                    if student_average >= d_grade:
                        print('Grade Letter is: D')
                    else:
                        if student_average < f_grade:
                            print('Grade Letter is: F')
                            return print('')
    


    #Return to Main
    main ()
        
    


    
    

    
