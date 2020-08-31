import random #importing the random library to get H/T values
import re #importing regex to find instances of H/T values of 6 or greater streak
nRuns = 10000
flipsPerRun = 100
totalInstances = nRuns * flipsPerRun
numberOfStreaks = 0 
for experimentNumber in range(nRuns):
    HTLists = [] #Intializing a list for the 100 Heads or Tails values
    HTStreak = [] #Holds the list returned by findall
    HTIntermediary = '' #Holds the string before passing it off to findall
    # Code that creates a list of 100 'heads' or 'tails' values
    for amount in range(flipsPerRun): 
        HTLists.append(random.randint(0,1))
    HTIntermediary = HTIntermediary.join(map(str, HTLists)) #Maps the list of values as a string, then joins them, and sets it to the Intermediary
    HTRegex = re.compile(r'1{6,}|0{6,}') #Only counts instances of 6 or greater for either heads or tails
    HTStreak = HTRegex.findall(HTIntermediary) #Finds all instances of 6 or greater in the string HTIntermediary, then returns a list with all relevant values
    numberOfStreaks += len(HTStreak) #Adds the streaks from the current run to the total
    print(numberOfStreaks)
    HTStreak = 0 #Resets the Streak, so that each run is individualized
    
chance = (numberOfStreaks / totalInstances)

def toPercent(decimal): #Making a function to change the decimal value of the chance to a percentage, rounded to 4 decimal places
    return round((decimal * 100),4)

chancePercent = toPercent(chance)

print('Chance of streak: %s%%' % chancePercent) #Printing final results