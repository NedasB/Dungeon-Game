#Import functions that were use, sys for sys.exit() and random for random.randrange() etc for random generation.
import sys
import random

class Room:
    #Defines the characteristics of a room
    def __init__(self, Room_Name, North_Exit, East_Exit, South_Exit, West_Exit):
        self.Room_Name = Room_Name
        self.North_Exit = North_Exit
        self.East_Exit = East_Exit
        self.South_Exit = South_Exit
        self.West_Exit = West_Exit
    #A function that allows for easier access of each room's status, also lets the user know what room they are in.
    def Look(self):
        print ("*You use your torch and look around*")
        print ("You are in the:", self.Room_Name)
        print ("You have an exit to the:")
        if(self.North_Exit):
            print("-North-", end=" ")
        if(self.East_Exit):
            print("-East-", end=" ")
        if(self.South_Exit):
            print("-South-", end=" ")
        if(self.West_Exit):
            print("-West-")
    #A function very similar to the above, difference being it provides less information. 
    def Move(self):
        print("Your options are:")
        if(self.North_Exit):
            print("[North]", end=" ")
        if(self.East_Exit):
            print("[East]", end=" ")
        if(self.South_Exit):
            print("[South]", end=" ")
        if(self.West_Exit):
            print("[West]")
#Features of each room.
Entrance_Room = Room("Entrance room", True, True, True, True)
North_Room = Room("North room", False, False, True, False)
East_Room = Room("East room", False, False, False, True)
West_Room = Room("West room", True, True, False, False)
North_West_Room = Room("North Western room", False, False, True, False)

#Extra variables that needed pre defining, keeps the code cleaner also.
North_Key = 0
Clue_Complete = 0
Coin_Bag = random.randint(5,20)
#Definition for a global variable, changes hence set as global so it keeps its value. 
def Pick_Up_key():
    global North_Key
    North_Key = 1
#""   
def Complete_Clue():
    global Clue_Complete 
    Clue_Complete = 1
#kept in a global like the above, allows the user more options to respond to things.
def Lists():
    global Yes 
    global No
    global Move
    global Look
    global Use
    global Collect
    global South
    global North
    global East
    global West
    global Key
    global Bag
    Yes = ("Yes", "YES", "yes")
    No = ("No", "NO", "no")
    Look = ("Look", "look", "LOOK")
    Move = ("Move", "move", "MOVE")
    Use = ("Use", "use", "USE")
    Collect = ("Collect", "collect", "COLLECT")
    South = ("South", "south", "SOUTH")
    West = ("West", "west", "WEST")
    North = ("North", "north", "NORTH")
    East = ("East", "east", "EAST")
    Key = ("Key", "key", "KEY")
    Bag = ("Bag", "bag", "BAG")

#Choice options for the entrance room.
def Choice_Entrance():
    Lists()
    print ("What would you like to do?")
    Choice_Made_Entrance = input("[Use] [Collect] [Move] [Look]\n")
    if Choice_Made_Entrance in Look:
        print("")
        Entrance_Room.Look()
        print("")
        Choice_Entrance()
    if Choice_Made_Entrance in Move:
        print("")
        Entrance_Room.Move()
        Move_Entrance()
    if Choice_Made_Entrance in Collect:
        print("\nThere is nothing to collect in this room\n")
        Choice_Entrance()
    if Choice_Made_Entrance in Use:
        print("\nThere is nothing you can use at the moment,")
        print("the door to the north seems interesting...")
        print("*try moving to it*\n")
        Choice_Entrance()
    else:
        print("\nThis is not a valid choice, please try again!\n")
        Choice_Entrance()
#Movement options for the entrance room.
def Move_Entrance():
    Lists()
    Move_Entrance_Choice = input("\nWhere would you like to go to?\n")
    if Move_Entrance_Choice in North:
        if North_Key == 0:
            print("\n*You walk to the Northern door and try to open it*")
            print("The door is locked and you are unable to open it.\n")
            Choice_Entrance()
        if North_Key == 1:
            print("\nYou walk up to the door and find that it is locked.\n")
            print("You have previously found a key, would you like to try it?")
            Try_Key = input ("[Yes] [No]\n")
            if Try_Key in Yes:
                print ("\nYou use the key and unlock the door\n")
                print ("You enter the room.")
                print("You notice something on the wall,")
                print("the writing would require a closer *look* to be seen.")
                Choice_North_Room()
            if Try_Key in No:
                Choice_Entrance()
            else:
                print ("\nYou have entered an invalid input, please try again!\n")
                Move_Entrance()
        else:
            print ("\nYou have entered an invalid input, please try again!\n")
            Move_Entrance()
    if Move_Entrance_Choice in West:
        print("\nYou enter the Western entrance.")
        Choice_West_Room()
    if Move_Entrance_Choice in South:
        print("\nThis exit leads to the way out the dungeon,")
        print("are you sure you would like to continue?")
        Quit_Game = input ("[Yes] [No]\n")
        if Quit_Game in Yes:
            print("Goodbye, hope you come back soon!")
            sys.exit()
        if Quit_Game in No:
            Run("")
        else:
            print ("\nYou have entered an invalid input, please try again!")
            Move_Entrance()
    if Move_Entrance_Choice in East:
        print("\n*You walk to the Eastern entrance and go through it*")
        print ("*Visibility is very low but you spot a table in the middle of it*")
        print ("*Taking a look may be a good idea*")
        Choice_East_Room()
    else:
        print ("\nYou have entered an invalid input, please try again!")
        Move_Entrance()

#Choice options for the east room.
def Choice_East_Room():
    print ("\nWhat would you like to do?")
    Choice_Made_EastR = input("[Use] [Collect] [Move] [Look]\n")
    if Choice_Made_EastR in Look:
        print("")
        East_Room.Look()
        print("You also find a key and a bag of coins on the table!")
        Choice_East_Room()
    if Choice_Made_EastR in Move:
        print("")
        East_Room.Move()
        Move_East()
        print("")
    if Choice_Made_EastR in Collect:
        print ("\nWhat would you like to collect?")
        Collection_Choice_EastR = input("[Key] [Bag]\n")
        if Collection_Choice_EastR in Key:
            print ("\n*You pick up the key*")
            Pick_Up_key()
            Choice_East_Room()
        if Collection_Choice_EastR in Bag:
            print("\nYou pick up the bag,")
            print("Upon opening the bag, you find that it contains", Coin_Bag, "coins.")
            Choice_East_Room()
        else:
            print ("You have entered an invalid input, please try again")
            Choice_East_Room()
    if Choice_Made_EastR in Use:
        print("\nThere is nothing you can use inside this room.")
        Choice_East_Room()
    else:
        print ("You have entered an invalid input, please try again!")
        Choice_East_Room()
#Movement options for the east room. 
def Move_East():
    Move_East_Choice = input("Where would you like to go to?\n")
    if Move_East_Choice in West:
        print("\nYou enter the Wastern exit and end up in the entrance room.")
        Choice_Entrance()
    else:
        print("\nThat is not an option, please select a valid option")
        Choice_East_Room()

#Choice options for the west room.
def Choice_West_Room():
    print ("\nWhat would you like to do?")
    Choice_Made_WestR = input("[Use] [Collect] [Move] [Look]\n")
    if Choice_Made_WestR in Look:
        West_Room.Look()
        print("")
        Choice_West_Room()
    if Choice_Made_WestR in Move:
        print("")
        West_Room.Move()
        print("")
        Move_West()
    if Choice_Made_WestR in Collect:
        print("\nThere is nothing to collect here.")
        Choice_West_Room()
    if Choice_Made_WestR in Use:
        print ("\nThere is nothing that you can use in this room.")
        Choice_West_Room()
    else:
        print("That is not an option, please select a valid option")
        Choice_West_Room()
#Movement options for the east room. 
def Move_West():
    Move_West_Choice = input("Where would you like to go to?\n")
    if Move_West_Choice in East:
        print("You enter the Eastern exit and end up in the entrance room.")
        Choice_Entrance()
    if Move_West_Choice in North:
        if Clue_Complete == 0:
            print("\nYou walk up to the Northern exit and you try to open the door.")
            print("The door is locked, luckily you notice a key mechanism to the side.")
            print("It seems to be locked behind a sequence of numbers.")
            Choice_West_Room()
        if Clue_Complete == 1:
            print("\nYou walk up to the door")
            print("Would you like to try the key mechanism?")
            Use_Digits = input("[Yes] [No]\n")
            if Use_Digits in Yes:
                Number_Entry = input("You try to enter in the digits:\n")
                if Number_Entry == "249":
                    print("\nThe code seems to work, the door unlocks and swing open")
                    print("You enter the door and enter the North Western room")
                    Choice_North_West_Room()
                else:
                    print("The code did nothing, seems like its the wrong one...")
                    Choice_West_Room()
            if Use_Digits in No:
                Choice_West_Room()
            else:
                print("This is not a valid input, please try again")
                Choice_West_Room()
        else:
            print("This is not a valid input, please try again")
            Choice_West_Room()
    if Move_West_Choice in East:
        print("You walk through the eastern exit")
        Choice_Entrance()
    else:
        print("This is not a valid input, please try again")
        Choice_West_Room()

#Choice options for the north western room
def Choice_North_West_Room():
    print ("\nWhat would you like to do?")
    Choice_Made_NorthWestR = input("[Use] [Collect] [Move] [Look]\n") 
    if Choice_Made_NorthWestR in Look:
        North_West_Room.Look()
        print("")
        print("\nAll of a sudden you faint and fall unconcious")
        print("You wake up outside the dungeon with", Coin_Bag, "coins.")
        sys.exit()
    if Choice_Made_NorthWestR in Move:
        print("")
        North_West_Room.Move()
        print("")
        Move_North_West()
    if Choice_Made_NorthWestR in Use:
        print("There is nothing you can use your items on here.")
        Choice_North_West_Room()
    if Choice_Made_NorthWestR in Collect:
        print("There is nothing to collect here")
        Choice_North_West_Room()
    else:
        print("This is not a valid input, please try again")
        Choice_North_West_Room()
#Movement options for the north western room
def Move_North_West():
    Move_North_West_Choice = input ("Where would you like to go?\n")
    if Move_North_West_Choice in South:
        print("You enter the southern entrance and end up in the western room>")
        Choice_West_Room()
    else:
        print("This is not a valid input, please try again")
        Choice_North_West_Room()

#Choice options for the north room
def Choice_North_Room():
    print ("\nWhat would you like to do?")
    Choice_Made_NorthR = input("[Use] [Collect] [Move] [Look]\n")
    if Choice_Made_NorthR in Look:
        print("")
        North_Room.Look()
        print("")
        print("Upon closer inspection with the torch, the numbers read 249")
        print("")
        Complete_Clue()
        Choice_North_Room()
    if Choice_Made_NorthR in Move:
        print("")
        North_Room.Move()
        print("")
        Move_North()
    if Choice_Made_NorthR in Collect:
        print("\nThere is nothing to collect in this room.")
        Choice_North_Room()
    if Choice_Made_NorthR in Use:
        print("\nThere is nothing you can use your items on here")
        Choice_North_Room()
    else:
        print("\nThat is not an option, please select a valid option")
        Choice_North_Room()
#Movement options for the north room
def Move_North():
    Move_North_Choice = input("Where would you like to go to?\n")
    if Move_North_Choice in South:
        print("\nYou enter the southern entrance and end up in the entrance room>")
        Choice_Entrance()
    else:
        print("That is not an option, please select a valid option")
        Choice_North_Room()
    


#Code to start the game.
def Run(welcome):
    print(welcome)
    Choice_Entrance()

#The function that starts the game, has a custom start message within it. 
Run("""
You are an explorer lost in the forest.
You stumble upon a mysterious dungeon and decide to explore it,
there is very little light coming in from the entrance,
dripping water can be heard from somewhere within.
*This better be worth it*
""")
