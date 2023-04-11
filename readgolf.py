#Readgolf.py
#IT1113/SectionW04
#Mykaela Darbouze
#Lab 5
#10/09/2022
#This program gathers player information
#and places them in a text file.
#The program then displays the text information
#and determines if they were under, over, or equal to the Par number
##By submitting this assignement, I am verifying that all program code
#was created by me only.

#Open the golf.txt data for reading

def main():
    player_file= open ('golf.txt', 'r')

    #Read the first line of the line
    Last_name= player_file.readline()

    #Create a Loop to Continue and end the file.
    while Last_name != '':
        #Read player data
        First_name= player_file.readline()
        Handi_cap= player_file.readline()
        Par_score= int(player_file.readline())
        

        #Strip the newsline from the item data
        Last_name= Last_name.rstrip('\n')
        First_name=First_name.rstrip('\n')
        Handi_cap = Handi_cap.rstrip('\n')

        #Display the records
        print('Player Data:')
        print()
        print('Last Name:', Last_name)
        print('First Name:', First_name)
        print('Handicap:',Handi_cap)
        print('Par Score for Course', Par_score)
        if Par_score == 80:
            print('Made Par')
        else:
            if Par_score < 80:
                print('Under Par')
            else:
                if Par_score > 80 :
                    print('Over Par')
        print()

        #Read the next line
        Last_name= player_file.readline()

    #Close the file
    player_file.close()
#Call back to function

main()

                    
            
