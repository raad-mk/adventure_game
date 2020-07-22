# Imports a module to add a pause
import time
# To choose random Monster
import random
# Figuring out how users might respond
answer_1 = "1"
answer_2 = "2"
Monsters = ["The Dragon", "The HR Personnel", "The Tiger", "Dixter"]
selectaMonster = random.choice(Monsters)
# Cutting down on duplication
required = ("\nUse only 1 or 2\n")
# The story is broken into sections, starting with "intro"
# This code is the starting of the game


def intro():
    print("Hello")
    time.sleep(2)
    print("My Name is Raad, And I wanna play a GAME")
    time.sleep(1)
    print("You find yourself standing in an open field,")
    print("filled with grass and, yellow wildflowers.")
    time.sleep(1)
    print("Rumor has it that a wicked fairie is somewhere ")
    print("around here, and has been terrifying the nearby village.")
    time.sleep(1)
    print("In front of you is a house.")
    time.sleep(1)
    print("To your right is a dark cave.")
    time.sleep(1)
    print("In your hand you hold your trusty (but not very effective) dagger.")
    time.sleep(1)
    print()
    print("Enter 1 to knock on the door of the house.")
    print("Enter 2 to peer into the cave.")
    print()

    choice = input(">>> ")

    if choice in answer_1:
        knockTheDoor()
    elif choice in answer_2:
        goToCave()
    else:
        print(required)
        intro()


# knock the door for the first time
def knockTheDoor():
    print("You approach the door of the house.")
    time.sleep(2)
    print("You are about to knock")
    print("When the door opens and out steps", selectaMonster)
    time.sleep(2)
    print("Eep! This is ", selectaMonster, "'s house!")
    time.sleep(2)
    print(selectaMonster, " attacks you!")
    time.sleep(2)
    print("You feel a bit under-prepared for this")
    print("What with only having a tiny dagger.")
    time.sleep(2)
    print("whould you like to (1) fight or (2) run away?")
    print()
    choice = input(">>> ")
    if choice in answer_1:
        print("You Do Your Best ...")
        time.sleep(2)
        print("But your digger is no match for ", selectaMonster)
        time.sleep(2)
        print("You have been defeated! Sorry...")
    elif choice in answer_2:
        backToField()
    else:
        print(required)
        knockTheDoor()


# knock the door for the 2nd time
def knockTheDoor2():
    print("You approach the door of the house.")
    time.sleep(2)
    print("You are about to knock")
    print("when the door opens and out steps", selectaMonster)
    time.sleep(2)
    print("Eep! This is ", selectaMonster, "'s house!")
    time.sleep(2)
    print(selectaMonster, " attacks you!")
    time.sleep(2)
    print("whould you like to (1) fight or (2) run away?")
    print()
    choice = input(">>> ")
    if choice in answer_1:
        print("As ", selectaMonster, "moves to attack,")
        print("you unsheathyour new sword.")
        time.sleep(2)
        print("The Sword of Ogoroth shines brightly in your hand")
        print("as you brace yourself for the attack.")
        time.sleep(2)
        print("But ", selectaMonster, "takes one look at your shiny new toy")
        print("and runs away!")
        time.sleep(2)

        print("You have rid the town of ")
        print(selectaMonster, ". ******* You are victorious! *******")
        time.sleep(2)
        print()
    elif choice in answer_2:
        backToField2()
    else:
        print(required)
        knockTheDoor2()


# Go back to the cave for the first time
def goToCave():
    print("You peer cautiously into the cave.")
    time.sleep(1)
    print("It turns out to be only a very small cave.")
    time.sleep(1)
    print("Your eye catches a glint of metal behind a rock.")
    time.sleep(1)
    print("You have found the magical Sword of Ogoroth!")
    time.sleep(1)
    print("You discard your silly old dagger and take the sword with you.")
    time.sleep(1)
    print("You walk back out to the field.")
    time.sleep(1)
    print()
    print("Enter 1 to knock on the door of the house.")
    print("Enter 2 to peer into the cave.")
    print()
    choice = input(">>> ")
    if choice in answer_1:
        knockTheDoor2()
    elif choice in answer_2:
        goToCave2()
    else:
        print(required)
        goToCave()


# Go back to the cave for the 2nd time
def goToCave2():
    print("You peer cautiously into the cave.")
    print("You've been here before, and getting all the good stuff.")
    print("It's just an empty cave now.")
    print("You walk back out to the field.")
    time.sleep(1)
    print()
    print("Enter 1 to knock on the door of the house.")
    print("Enter 2 to peer into the cave.")
    print("please enter 1 or 2")
    print()
    choice = input(">>> ")
    if choice in answer_1:
        knockTheDoor2()
    elif choice in answer_2:
        goToCave2()
    else:
        print(required)
        goToCave2()


# Go back to the field first time
def backToField():
    print("You run back into the field.")
    print("Luckily, you don't seem to have been followed.")
    time.sleep(1)
    print()
    print("Enter 1 to knock on the door of the house.")
    print("Enter 2 to peer into the cave.")
    print("please enter 1 or 2")
    print()
    choice = input(">>> ")
    if choice in answer_1:
        knockTheDoor()
    elif choice in answer_2:
        goToCave()
    else:
        print(required)
        backToField()


# Go back to the field 2nd time
def backToField2():
    print("You run back into the field.")
    print("Luckily, you don't seem to have been followed.")
    time.sleep(1)
    print()
    print("Enter 1 to knock on the door of the house.")
    print("Enter 2 to peer into the cave.")
    print("please enter 1 or 2")
    print()
    choice = input(">>> ")
    if choice in answer_1:
        knockTheDoor2()
    elif choice in answer_2:
        goToCave2()
    else:
        print(required)
        backToField2()


# to keep playing until other than 1 key is clicked
playAgain = "1"
while playAgain == "1":
    intro()
    print("Do you want to play again?")
    print("Enter 1 to continue playing")
    print("Enter any key to Exit: ")
    playAgain = input(">>> ")
# Thank you --RMG--
