#writegolf.py
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

#Get player information using input data

def main ():
    #Get the Number of players in the tournament
    player_num = int(input('Number of Tournamnet Players:          '))
    
    #Open a file for writing
    player_file= open('golf.txt', 'w')
    
    #Get Player Information
    for count in range(1, player_num + 1):
        print('Enter Player Data', count, ':', sep='')
        Last_name= input('Player\'s Last Name:             ')
        First_name =input('Player\'s First Name:          ')
        Handi_cap=input('Players\'s Handicap Score:         ')
        Par_score=int(input('Player\'s Par Score:         '))

        #Determine Par Score
        if Par_score == 80:
            print('Made Par')
        else:
            if Par_score < 80:
                print('Under Par')
            else:
                if Par_score > 80 :
                    print('Over Par')

        #Write Player Data on File

        player_file.write(Last_name +'\n')
        player_file.write(First_name +'\n')
        player_file.write(Handi_cap + '\n')
        player_file.write(str(Par_score) + '\n')

        player_info()
        

    #Close the file
    player_file.close()
    print('Player Data Has Been Saved in golf.txt.')

def player_info():
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
    
#Call the main function
main()
    
    
