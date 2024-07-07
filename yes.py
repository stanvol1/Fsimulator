import time
import threading
import random
# general vars
coins = 0
health = 10
score = 0
reputation = 0


#Traits
strength = 0
intuition = 0
speech = 0
luck = 0
defence = 0



# adding empty arrays
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
# clean up this piece of cod
print("Welcome to father simulator, where all the decisions fathers make have been digitalised! For each right answer, you will gain a point, but if you chose wrong, your health will deplete. You start off with 10 health, and if it runs out, you will die (this happens at the very end of the playthrough)")


check = False 

while not check:
    i = input("You want an item, but it might be too expensive! Put in a price here, and if your lucky, father might allow you to buy it! (please only respond with a number): ")
    if i in "123456789":
        check = True
    else:
        print("Input value must be an integer")
if int(i) < 10:
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

v = input("you can respond with yes or no, but once again, choose your answer carefully, as this answer could seal your fate: ")
if v == "no":
    print("- 10 health")
    print("You died...")
    health = health - 10

if v == "yes":
    print("Well done! You passed the level, and now you may sleep...")
    time.sleep(2)
    score = score + 1
    print("LEVEL UP! 0 -> 1")
    print('Your score was ' + str(score))

if health <= 0:
    time.sleep(1)
    print("You lost. Try again next time")
    quit()

time.sleep(3)

print("LEVEL 1")

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
l = input("you must respond, but what do you say, respond with A: That's ridiculous! The garden has no weeds in it. Or B: OK, let's try and weed the garden")
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
        print("you must escape, but how? there are two possibilities, but one is more dangerous than the other, but you must be quick, as Father is getting closer. You toss a coin. There is a 50/50 chance of each one: ")
        # This needs to be cleaned up a huge amount
        def coin():
            return random.random() < .5
        if coin():
            print("You now must go via the vents")
            time.sleep(2)
            print("It is a treacherous journey, and for this reason, you have been granted the motivational poster!")
            inventory.append("Motivational Poster")
            for l in inventory:
                print(l)
            print("+ 2 strength")
            print("-1 speech")
            Speech = Speech - 1
            strength = strength + 2
            # this will need a story added onto it. This story should lead to the school.
            print("After many long hours of crawling through the vents, you begin to see light...")
            time.sleep(3)
            print("You see a mesh vent leading into a dull room at ground level...")
            time.sleep(3)
            print("To open the vent you could either: [pry] - Pry the vent cover open with your hands (min strength: 4), [brute] - Brute force the vent cover open (-2 health, no requirement)")
            prybash = input("Please pick: ")

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
                    
            # Under construction, have to incorporate player stats first


        else:
            print("You now must go via the basement")
            time.sleep(3)
            print()
            print("-this is creepy-, you think. You begin to hear voices...")
            # this will need another story, with different situations leading to a feature that we want to implement, but a different item should be added to the players inventory first
# before continuing, we need to add the array for the inventory
if l.lower() == "b":
    print("Well done! You picked the right answer. You will now be rewarded with 5 coins!")
    coins = coins + 5