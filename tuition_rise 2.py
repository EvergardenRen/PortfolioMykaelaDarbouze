#tuition_rise.py
#IT1113/ Section W04
#09/11/2022
#This program finds out the new tuition of 
#a university for the next 7 years
#and displays it.
#By submitting this assignement, I am verifying that all program code
#was created by me only.

#Create a variable for the loop
Next_year='y'

#Assign value to raise rate
raise_rate= float(.035)

#Print and calculate the years and their tuition
while Next_year == 'y':
    current_tuition= float(input('What is the current tuition?:     '))
    current_year = int(input('What is the current year?:      '))
    new_tuition = (current_tuition * raise_rate) + current_tuition

    #Display the tuition and the year.
    print('The tuition per semester for', current_year,'is $',
          format(new_tuition,',.2f'),'.')

    #Ask for another year
    Next_year= input('Calculate the next year? (y/n):     ')      
          
    


                        
                        
    
    






