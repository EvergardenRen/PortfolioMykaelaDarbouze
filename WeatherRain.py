#WeatherRain.py
#IT1113/SectionW04
#Mykaela Darbouze
#Lab 6
#10/16/2022
#This program gathers monthly rainfall
#and puts them in a list 
#The program then  calculates the average rainfall in year from
#lowest to highest
#By submitting this assignement, I am verifying that all program code

#Create a List of Months
months =['January', 'Feburary', 'March', 'April', 'May', 'June',\
          'July', 'August', 'September', 'October', 'November', 'December']

#Create an Empty List for the Rainfall
rainfall_list=[]

#Get Rainfall Data
for new_month in months :
    monthly_rainfall=float(input('Enter the Rainfall Amount For the' + \
                                 ' New Month (In Order, Starting with January):         '))
    #Append the values to the list
    rainfall_list.append(monthly_rainfall)
    
#Create Function for total and average 
#Create an accumlator 
def calculation():
    total=0
    for value in rainfall_list:
        total += value
    print(' The total amount of rainfall for the year is', total,' inches.')
    #Calculate Average Monthly Rainfall
    average = sum(rainfall_list)/ len(rainfall_list)
    print('The total monthly average of rainfall is',format(average,'.2f'))
#Call back to the calculations function
calculation()

#Sort the list
def sorting_rainfall():
    rainfall_list.sort()
    print('This is the rainfall of the year from lowest to highest:', rainfall_list)
#Call back to the sorting fucntion
sorting_rainfall()

#Get the Minimum and Maximum months with rainfall 
def minimum_maximum():
    print('The lowest rainfall amount was', float(min(rainfall_list)))
    lowest=input('Which Month had the lowest?:               ')
    print(lowest)
    print('The highest rainfall amount was', float(max(rainfall_list)))
    highest=input('Which Month had the highest?:            ')
    print(highest)
#Call back to the min max fucntion
minimum_maximum()
    



