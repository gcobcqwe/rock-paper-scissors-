# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
i=0
name=""
str = raw_input("Enter your input: ");

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if str=="rock":
        i=0
    if str=="Spock":
        i=1
    if str=="paper":
        i=2
    if str=="lizard":
        i=3
    if str=="scissors":
        i=4    
    # convert name to number using if/elif/else
    # don't forget to return the result!
    #print i

def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if i==0:
        name="rock"
    if i==1:
        name="Spock"
    if i==2:
        name="paper"
    if i==3:
        name="lizard"
    if i==4:
        name="scissors"    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    #print name
    
def rpsls(str): 
    # delete the following pass statement and fill in your code below
    x=random.randint(0,5);
    #print x
    name_to_number(str);
    number_to_name(x);
    
    
    if i==0:
        print "Player chooses rock"
        if x==3 or x==4:
            if x==3:
                print "Computer chooses lizard"
            else:
                print "Computer chooses scissors"
            print "Player wins!"
        elif x==0:
            print "Computer chooses rock"
            print "tie"
        elif x==1 or x==2:
            if x==1:
                print "Computer chooses Spock"
            else:
                print "Computer chooses paper"
            print "Computer wins!"
    elif i==1:
        print "Player chooses Spock"
        if x==4 or x==0:
            if x==0:
                print "Computer chooses rock"
            else:
                print "Computer chooses scissors"
            print "Player wins!"
        elif x==1:
            print "Computer chooses Spock"
            print "tie"
        elif x==3 or x==2:
            if x==3:
                print "Computer chooses lizard"
            else:
                print "Computer chooses paper"
            print "Computer wins!"
    elif i==2:
        print "Player chooses paper"
        if x==0 or x==1:
            if x==0:
                print "Computer chooses rock"
            else:
                print "Computer chooses Spock"
            print "Player wins!"
        elif x==2:
            print "Computer chooses paper"
            print "tie"
        elif x==3 or x==4:
            if x==3:
                print "Computer chooses lizard"
            else:
                print "Computer chooses scissors"
            print "Computer wins!"
    elif i==3:
        print "Player chooses lizard"
        if x==1 or x==2:
            if x==1:
                print "Computer chooses Spock"
            else:
                print "Computer chooses paper"
            print "Player wins!"
        elif x==3:
            print "Computer chooses lizard"
            print "tie"
        elif x==0 or x==4:
            if x==0:
                print "Computer chooses rock"
            else:
                print "Computer chooses scissors"
            print "Computer wins!"
    elif i==4:
        print "Player chooses scissors"
        if x==2 or x==3:
            if x==2:
                print "Computer chooses paper"
            else:
                print "Computer chooses lizard"
            print "Player wins!"
        elif x==4:
            print "Computer chooses scissors"
            print "tie"
        elif x==0 or x==1:
            if x==0:
                print "Computer chooses rock"
            else:
                print "Computer chooses Spock"
            print "Computer wins!"
    
    
    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls(str)


# always remember to check your completed program against the grading rubric


