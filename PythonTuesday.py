import turtle

#
#NOTE: This is a modern kitten world.


#Global Variables
answer = " "
villianTurtle = turtle.Turtle()


#Function Definition
def dance(time):

    if time == 0:
        
        print("Turtle power!")
        return True
    
    else:
        
        villianTurtle.shape("turtle")
        villianTurtle.pendown()
        villianTurtle.forward(200)
        villianTurtle.right(90) #turns right by 90 degrees
        villianTurtle.forward(100)
        villianTurtle.right(90)

        dance(time - 1)
        #Function exits
        print("Exit")
    
def profession():
    answer = input() #this is where the user's choice is stored

    #VillainCat
    if(answer == "no"):

        #Villian Turtle appears
        dance(5)
        
        print("Sarah has been a neighbor to the squirrel for 10 years.")
        print("Sarah knows exactly where the squirrel lives. But Sarah does not want to help.")
        print("So Sarah laughs and walks away.")
        print("")
        print("LEVEL UP: Sarah just became a VillianCat!")
    
        #VillianPack
        food = "Deviled Eggs with Salmon" #this is special food that gives Sarah laser eyes 
        cape = "electric black cape" #this lets Sarah cut off the power within a 20-mile radius
        vehicle = "Motorized Cat Tree with 3 Floors" #this vehicle can go up to 200 mph

    #Supercat
    if(answer == "yes"):
        print("Sarah has been a neighbor to the squirrel for 10 years.")
        print("Sarah knows exactly where the squirrel lives. So, the squirrel ")
        print("jumps on Sarah's back to be taken home.")
        print("")
        print("LEVEL UP: Sarah just became a supercat!")

        #Superhero Backpack
        sidekick = "Steve the Squirrel"
        food = "Cans of Tuna" #this is special tuna that turns the cat into a fish
        cape = "electric green cape" #this lets Sarah JOPE (this means to jump bery high)

    
    return answer

#Introduction - Set the Scene
print("Welcome to Catville!")
print("Sarah the Kitten thought her day was going to be typical.")
print("But little did she know that someone was going to give her nachos.")
print("What should Sarah do today?")

#There are 4 destinies that the cat can do. The user
#gets to choose that destiny.
print("Sarah sees a squirrel outside. However, the squirrel forgot where he lives.")
print("The trees look too identical to the squirrel.")
print("Will Sarah help the squirrel?")



print("Sarah tells the squirrel: " + str(profession())) #prints the user's answer

#####################################
        # CAT TOY FILTER #
#####################################
catToys = [ " ", " ", " ", " ", " "]

#Filter Function Definition
def filterToys(listOfToys):
    print(listOfToys[1])
    return True

print("Sarah returns home. To her surprise, her owner offers her toys.")
print("Which toy does Sarah love?")

for items in catToys:
    answer = input()
    catToys[items] = str(answer)

    filterToys(catToys)

#Work at McTurkeys

#College Undergraduate

#####################################
#####################################

#Mission1


#Mission2


#Mission3

#####################################
#####################################
#Plot Twist


#Fun Ending
