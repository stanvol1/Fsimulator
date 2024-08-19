import time
import sys
import threading
import random
import winsound
import pygame
pygame.init()
pygame.mixer.init()
# sounds using pygame
brickinwall = pygame.mixer.Sound("5959375254061056.mp3")

# general vars
coins = 0
health = 10
score = 0
reputation = 0
menupoints = 7


#Traits
damage = 3
strength = 0
speech = 0
luck = 0
defence = 0

#Character creator


# adding empty arrays
vending_machine = ["CD ninja star", "safety scissors", "trail mix with raisins" "Nifty sunglasses"]
inventory = [""]
heavy = [""]
light = [""]
consumables = [""]
armour = [""]
# all of this could be added later, but for now it's too buggy
# code for the basic health bar thing
# hbar = True
# adding threading for the health bar (first time, so it's going to be inefficient and the code itself is going to be awful) yes
# def health_bar_thing():
   # while hbar is True:
       # player_input = input()
        # here I'm just trying out a little thing to see if I can make health bars or indicators that can be checked throughout the game
       # if player_input == "health":
          #  print("your health is " + str(health))
# thread = threading.Thread(target=health_bar_thing)
# thread.start()
# considering a print("LEVEL 0") thing here
# clean up this piece of code
def typing(text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.15)
            # now, if you want to make a typewriter effect in any place within the code, just write typing("") instead of print("") don't forget to add a \n at the end though.
menuloop = True
while menuloop:
    typing("FATHER SIMULATOR\n")
    print("the place where your father is digitalised")
    print("Main menu: ")
    startmenu = input("[Continue]   [New game]\n")
    match startmenu:
        case "Continue":
            print("")
            # add ids and identifiers for progress etc
            menuloop = False
            break
        case "New game":
            menuloop = False
            break
        case _:
            print("Please input a valid word (either Continue or New game). Remember, it is case sensitive!")

#  need a points system here, giving a set amount of points that can be used, im thinking of storing it in a variable


print("Welcome to level 0. This is an easy level. Here, there is no way to alter how the game ends. Good luck!")
print("Welcome to father simulator, where all the decisions fathers make have been digitalised! For each right answer, you will gain a point, but if you chose wrong, your health will deplete. You start off with 10 health, and if it runs out, you will die (this happens at the very end of the playthrough)")
input_traits = True
while input_traits:
    print("Please assign your skills: ")
    strength = int(input("Please assign strength:\n"))
    speech = int(input("Please assign speech:\n"))
    luck = int(input("Please assign luck:\n"))
    if strength + speech + luck == 7:
        break
    else:
        print("Please input exactly 7 points")
        continue

i = int(input("You want an item, but it might be too expensive! Put in a price here, and if your lucky, father might allow you to buy it! (please only respond with a number):\n "))
if i < 10:
    print("Father approves of the price, you can buy your item! Your score will be increased by 1")
    print("+ 1 score!")
    score = score + 1
else:
    print("Father disapproves of the price, you will be punished")

time.sleep(2)

print("Now you have to go out for a walk, but you don't want to. Do you A:")
print("Complain")

time.sleep(3)

print("or B")
print("go out on the walk")

time.sleep(2)

a = input("choose either A or B, but pick your answer wisely, or you will suffer a fate worse than death: ")

if a.lower() == "a":
    print("you chose wrong, you will now have to empty the dishwasher")
    print("-2 health")
    health = health - 2

if a.lower() == "b":
    print("well done! You chose correctly, a point will be added to your score")
    score = score + 1

time.sleep(5)

print("finally, at the end of the day, you are lying down on the sofa, but father comes in and asks you to make dinner")

time.sleep(2)
questionloop3 = True
while questionloop3:
    v = input("you can respond with yes or no, but once again, choose your answer carefully, as this answer could seal your fate:\n")
    if v == "no":
        print("- 10 health")
        print("You died...")
        health = health - 10
        quit()
    elif v == "yes":
        print("Well done! You passed the level, and now you may sleep...")
        time.sleep(2)
        score = score + 1
        print("LEVEL UP! 0 -> 1")
        print('Your score was ' + str(score))
        break
    else:
        print("Please respond with a valid answer")
        continue

if health <= 0:
    time.sleep(1)
    print("You lost. Try again next time (Please, we want players xD)")
    quit()

time.sleep(3)

typing("LEVEL 1\n")

time.sleep(2)

health = 10
score = 0

print("This is the first proper level. Here, you will be tested to see if you have what it takes to face the wrath of the almighty Father.")
time.sleep(1)
print("this time, one wrong answer subtracts 5 health instead of 2, but you get 2 points instead of 1 per correct answer. Your initial health bar will look like this ----------")
time.sleep(1)
print("you now also have an extra stat, defence. This stat can be boosted through armor or levels. Every level from this point onwards will increase your defence by 1")
print("+1 defence")
defence = defence + 1
time.sleep(3)
print("part 1... the garden")
time.sleep(3)
print("You are now going out to the garden. It needs to be worked on. The following is a recording, recovered from a spontaneous fire in Father's study")
print("Come on, we need to weed the garden, it's an absolute mess.")
l = input("you must respond, but what do you say, respond with A: That's ridiculous! The garden has no weeds in it. Or B: OK, let's try and weed the garden\n")
if l == "A" or "a":
    if defence >= 1:
        health = health - 4
        print("You chose wrong, but you have 1 defence, so you will only have 4 health subtracted. You now have 6 health.")
        time.sleep(1)
        print("------")
        print("-4 health")
        print()
        print("Because you chose wrong, you will now have to suffer through a grueling punishment")
        print()
        print("Father has transformed into a higher type of being, able to execute punishments beyond human comprehension")
        print()
        print("you must escape, but how? there are two possibilities, but one is more dangerous than the other, but you must be quick, as Father is getting closer. ")
        # This needs to be cleaned up a huge amount
    choice = input("you can escape via the [b]asement or the [v]ents\n")
    if choice == "v":
            print("You now must go via the vents")
            time.sleep(2)
            print("It is a treacherous journey, and for this reason, you have been granted the motivational poster!")
            inventory.append("Motivational Poster")
            for l in inventory:
                print("You have:")
                print(l)
            print("In your inventory")
            print("+ 2 strength")
            print("-1 speech")
            speech = speech - 1
            strength = strength + 2
            # this will need a story added onto it. This story should lead to the school.
            print("After many long hours of crawling through the vents, you begin to see light...")
            time.sleep(3)
            print("You see a mesh vent leading into a dull room at ground level...")
            time.sleep(3)
            print("To open the vent you could either: [pry] - Pry the vent cover open with your hands (min strength: 4), [brute] - Brute force the vent cover open (-2 health, no requirement)")
            prybash = input("Please pick:\n")

            while True:
                match prybash:
                    case "pry":
                        if strength >= 4:
                            print("You pried open the vent cover!")
                            break
                        elif strength < 4:
                            print("You must have 4 or more strength to do that!")
                    case "brute":
                        print("You put your body weight into it and bash open the vent cover, your ribs ache a bit.")
                        print("-2 health!")
                        health = health - 2
                        break
                    # needs cleaning up
            print("As you stumble out of the vents, you see a building in the distance")
            time.sleep(3)
            print("You begin to walk to the building")
            print("The sign on the wall says: School")
            typing("Level: School\n")
            print("You open the door, and as you enter, you notice a strange thing, there is no sound")
            print("You arrive at a corridor")
            doors_loop = True
            while doors_loop:
                doors = input("There are five doors, you now may choose which one to enter. There are also lockers, which you can search through by inputting [l]. To enter a door, input a number from 1 - 5\n")
                match doors:
                    case "1":
                        typing("entering the art classroom...\n")
                        print("within the arts classroom, there are multiple badly drawn posters, messy paintings and terrible cards adressed to now forgotten relatives and friends\n")
                        typing("It is obvious that this classroom hasn't seen use in a long while\n")
                        artclassloop = True
                        while artclassloop:
                            art_classroom_input = input("There is a chest of [d]rawers, some [de]sks and a [b]ox. Input one of the characters in brackets. To go back to the hallway, input [back]\n")
                            match art_classroom_input:
                                case "d":
                                    typing("Searching drawers...\n")
                                    print("You found a: Bad painting")
                                    inventory.append("Bad painting")
                                case "de":
                                    typing("Searching desks...\n")
                                    print("You found... Textbook!")
                                    inventory.append("textbook")
                                case "b":
                                    typing("Searching box...")
                                    print("You found: Safety scissors! ")
                                    typing("these give you +7 damage, but they only have 5 uses")
                                    damage = damage + 7
                                case "back":
                                    break
                                case _:
                                    print("Please input a valid response. Remember, they are case sensitive!")
                            
                    case "2":
                        typing("entering maths classroom...\n")
                        if "class_ban2" in inventory:
                            print("You shall not pass")
                        else:
                            if "textbook" in inventory:
                                print("Come in")
                                brickinwall.play()
                                print("You step inside the classroom")
                                print("-Come on, sit down, or you will be punished-  ")
                                print("You choose a seat next to a strange but kind looking student. They ask you something")
                                typing("-Want to see something?-")
                                print("sure")
                                print("I have balloons filled with coloured paint. This school hasn't had any sort of colour within it for centuries.")
                                print("Can you throw it?")
                                maths_classroom_question = input("[y]es, [n]o")
                                match maths_classroom_question:
                                    case "y":
                                        print("Great, throw it!")
                                        typing("You throw the balloons, they burst all over the classroom...")
                                        print("This awakens something within the students")
                                        print("They riot, breaking windows, vandilizing walls and perform all sorts of strange actions, taking full advantage of their new found freedom")
                                        print("You see something fall. It's a brick")
                                        print("Item gained! Another brick in the wall.")
                                    case "n": 
                                        print("I expected better from you...")
                                        typing("You leave the classroom, banished for the entirety of the run")
                                        inventory.append("class_ban2")
                                # I will play another brick in the wall here
                            else:
                                print("You haven't got a textbook, come back when you do")
                                continue                
                    case "3":
                        typing("entering the english classroom...")
                        print("you enter, and see that they are reading shakespeare.")
                        englishloop1 = True
                        while englishloop1:
                            english_question = input("The teacher asks -have you got your book?- ([y]es or [n]o) ")
                            if english_question.lower == "y":
                                print("come in then!")
                                break
                            elif english_question.lower == "n":
                                print("well, I suppose you may come in and listen, but don't distract anyone")
                                break
                            else:
                                print("Huh? I don't understand you.")
                    case "4":
                        typing("entering the the gymnasium ") # add a classroom
                    case "5":
                        typing("entering the lab") # once again, add a classroom
                    case "l":
                        if coins > 4:
                            lockerchance = random.choice(vending_machine)
                            typing("You found: \n" + lockerchance + "\n")
                            vending_machine.remove(lockerchance)
                            inventory.append(lockerchance) # adds item to inventory
                            print("The locker may have the following items: ")
                            for lockeritems in vending_machine:
                                print(vending_machine)
                            # here I will have to add either cases or if functions
                            match lockerchance:
                                case "CD ninja star":
                                    damage = damage + 3
                                case "safety scissors":
                                    damage = damage + 6
                                case "trail mix with raisins":
                                    trailmixuses = 1
                                case "Nifty sunglasses":
                                    speech = speech + 1
                        else:
                            print("Come back when you have at least 5 coins!")
                        # todo. Add effects and traits to the items given.
    elif choice == "b":
            print("You now must go via the basement")
            time.sleep(3)
            print()
            print("-this is creepy-, you think. You begin to hear voices...")
            print("You see two people arguing with eachother. They have clothes with two different symbols on them.")
            print("You walk up to them")
            # this will need another story, with different situations leading to a feature that we want to implement, but a different item should be added to the players inventory first
# before continuing, we need to add the array for the inventory
if l.lower() == "b":
    print("Well done! You picked the right answer. You will now be rewarded with 5 coins!")
    coins = coins + 5