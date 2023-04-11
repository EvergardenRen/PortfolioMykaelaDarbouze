#Test3Part2.py
#IT1113/SectionW04
#Mykaela Darbouze
#Test3Part2
#12/07/2022
#The purpose of this program is to
#get the distance in kiliometers
#and convert them into miles while using a main fucntion
#By Submitting this assignment, I am verifying that all program code
# was created by me only

#Create a Loop that controls the function.

keep_going = 'Yes'


#Create main fucntion
while keep_going == 'Yes' :
    def main():
        
        #Get Kilometer Distance 
        kilometer= float(input('Enter Kilometer Distance Data:           '))
        
        #Convert Kilometer to Miles
        miles= convert_kilometer (kilometer)

        #Display Information 

        print('The Original Kilometer:', kilometer, \
              '. The Conversion to Miles is:', format (miles,',.2f'), sep='')
    

    keep_going = input('Enter New Kilometer Distance? (Yes/No):     ')

        
 
   #Create conversion function
    def convert_kilometer(kilometer):

        get_miles= float(kilometer * 0.6214)

        return get_miles
    
    #Return main function 
    main()
    
    
