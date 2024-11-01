
import time
import sys
import threading
import random
import pygame
import keyboard
pygame.init()
pygame.mixer.init()

# functions
def hall_monitor():
    global speech
    global coins
    global inventory
    print("Well well well")
    time.sleep(3)
    print("what do we have here...")
    time.sleep(3)
    print("what are you doing on my turf at this hour, chum?")
    print("See this badge? It invests in me the authority to do whatever I want with you if I catch you in my hallway, and I ask of you 2 coins")
    print("now now, I will have to punish you for this")
    input("why are you in this hallway anyway?")
    if speech > 4:
        print("well, I suppose I could let you pass, no need to pay me anything")
    elif "uno_reverse" in inventory:
        unocard = input("You have an Uno reverse card, you could use this to escape")
        print("Why, you have a reverse card, I suppose I must punish myself now")
        print("Here are the two coins I demanded of you")
        coins = coins + 2
        
    elif coins == 0:
        print("No coins means a beating")
        strength = strength - 2
        print("-2 strength")
        
    elif coins >= 2:
        print("You have 2 coins or more, you can buy your way out of this")

# sounds using pygame
brickinwall = pygame.mixer.Sound("5959375254061056.mp3")

# general vars
ventsloop = True
test = "I can't be bothered to put anything in here yet"
coins = 1000000
health = 10
score = 0
reputation = 0
menupoints = 7
scissors_uses = 6



#Traits
damage = 3
strength = 0
speech = 0
luck = 0
defence = 0
attack_damage = 0.75 * strength
# Combat damage
def bossfight():
    player_health = 40
    strength = strength + 3
    teacher_health1 = 50
    teacher_health2 = 50
    def typing(text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.15)
    typing("You found a mace on the floor. Next to it lies a note. On it is written the following")
    typing("-this thing seems to be the only thing that can damage the teacher... OH FUCK HERE HE COMES AHHHHHHHH-")
    print("In front of you appears a door")
    print("You seem drawn to it, and you lose control of your arm, which then moves towards it and open the door")
    typing("entering teacher's office")
    typing("well well well, what have we got here")
    print("you are now in combat")
    typing("the head teacher sees you, and begins to move towards you.")
    teacher_loop1 = True
    while teacher_loop1:
        print("you pick up the mace")
        teacher_mace_loop1 = True
        while teacher_mace_loop1:
            teacher_mace_input1 = input("Do you want to [a]ttack or [l]ose the shot (if your attack fails, you will take a small amount of damage, but it you lose the shot, you lose the chance to attack)")
            teacher_mace_input1_loop = True
            while teacher_mace_input1_loop:
                if teacher_mace_input1 == "a":
                   teacher_mace_input1_rand = random.choice([1, 0])
                   if teacher_mace_input1_rand == 1:
                        print("your attack failed! You take 1 damage")
                        player_health = player_health - 3
                        if player_health < 1:
                            print("You died (L) hope you had fun!")
                            quit()
                        teacher_mace_input1_loop = False
                if teacher_mace_input1_rand == 0:
                    print("Your attack did 5 damage! (-wow this mace is powerful- You think)")
                    


            
def encounter():
    def typing(text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.15)
    player_health = 50
    global attack_damage
    chomik_health = 20
    print("you enter the room, but as you walk in, you see a small animal looking around; it's a hamster")
    print("You recognise it as the english classes's pet, chomik.")
    print("Although he doesn't seem aggressive, you suddenly see a boss bar appear out of thin air (-huh, that isn't normal, you think-)")
    print("chomik has 20 health")
    typing("you are now in combat\n")
    cturn1 = True
    cturn2 = False
    while cturn1:
        cturninp = input("It is your turn. Do you want to [A]ttack, [T]alk or [R]un ")
        if cturninp == "a":
            randomchancecombat = random.choice([1, 0])
            if randomchancecombat == 1:
                chomik_health = chomik_health - attack_damage
                print("Your attack did " + str(attack_damage))
                print("chomik now has " + str(chomik_health))
                if chomik_health < 1:
                    print("You won the fight!")
                    break
                else:
                    cturn1 = False
                    cturn2 = True
                while cturn2:
                    chomik_damage = 1
                    player_health = player_health - 1
                    print("chomik did 1 damage")
                    print("You now have " + str(player_health))
                    if player_health < 1:
                        print("you lost the fight (HOW, THIS IS THE EASIEST FIGHT IN THE GAME, I APPLAUD YOU FOR THIS)")
                    cturn2 = False
                    cturn1 = True
                continue
            if randomchancecombat == 0:
                print("your attack failed!")
                typing("You lost 1 health!")
                player_health = player_health - 1
                if player_health < 1:
                    print("you lost the fight (HOW, THIS IS THE EASIEST FIGHT IN THE GAME, I APPLAUD YOU FOR THIS)")    
                continue
        elif cturninp == "t":
            if speech < 3:
                typing("no can do, your social skills are so terrible that you can't even talk to a hamster...\n")
            else:
                typing("it's a bloody hamster, it doesn't matter how charismatic you are, you don't speak in squeaks. (really, what did you expect? You're not a fucking wizard)\n")
        elif cturninp == "r":
            print("a ring of squeaks follow you, and you peer back to see a very angry hamster rushing towards you at almost superhuman speeds. It looks like you are forced to take the fight.\n")

encounter()
def hit():
    global damage
    global health
    global attack_damage
    global inventory
    if "scissors" in inventory:
        scissors_hit = ("You have safety scissors in your inventory, would you like to use them?")
        if scissors_hit == "y":
            print("6 damage!")
            scissors_uses = scissors_uses - 1
            print("safety scissors uses:" + scissors_uses)


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
    print("This is the character creator. Here, you assign your skills. The total sum of the skills must add up to 7.")
    time.sleep(3)
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
        while ventsloop:
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
                        doors = input("There are five doors, you now may choose which one to enter. There is also a vending machine, costing 5 coins, which you can search through by inputting [v]. To enter a door, input a number from 1 - 5\n")
                        match doors:
                            case "Darkmoon":
                                print("")
                            case "InTheRainbows":
                                typing("Yeah, I\n")
                                typing("I hit the bottom\n")
                                typing("Hit the bottom and escape\n")
                                typing("Escape.\n")
                            case "1":
                                encounter_loop = True
                                while encounter_loop:
                                    encounter_chance = random.choice([4, 3, 2, 1, 0])            
                                    if encounter_chance == 4:
                                        encounter()
                                    else:
                                        encounter_loop = False
                                        
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
                                            print("You found: Safety scissors!\n")
                                            typing("these give you +7 damage, but they only have 5 uses\n")
                                            inventory.append("scissors")
                                        case "back":
                                            break
                                        case _:
                                            print("Please input a valid response. Remember, they are case sensitive!")
                                    
                            case "2":
                                while encounter_loop:
                                    encounter_chance = random.choice([4, 3, 2, 1, 0])            
                                    if encounter_chance == 4:
                                        encounter()
                                    else:
                                        encounter_loop = False
                                        
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
                                        typing("-Want to see something?-\n")
                                        print("sure")
                                        print("I have balloons filled with coloured paint. This school hasn't had any sort of colour within it for centuries.")
                                        print("Can you throw it?")
                                        maths_classroom_question = input("[y]es, [n]o")
                                        match maths_classroom_question:
                                            case "y":
                                                print("Great, throw it!")
                                                typing("You throw the balloons, they burst all over the classroom...\n")
                                                print("This awakens something within the students")
                                                print("They riot, breaking windows, vandilizing walls and perform all sorts of strange actions, taking full advantage of their new found freedom")
                                                print("You see something fall. It's a brick")
                                                print("Item gained! Another brick in the wall.")
                                            case "n": 
                                                print("I expected better from you...")
                                                typing("You leave the classroom, banished for the entirety of the run\n")
                                                inventory.append("class_ban2")
                                        # I will play another brick in the wall here
                                    else:
                                        print("You haven't got a textbook, come back when you do")
                                        continue

                            case "3":
                                while encounter_loop:
                                    encounter_chance = random.choice([4, 3, 2, 1, 0])            
                                    if encounter_chance == 4:
                                        encounter()
                                    else:
                                        encounter_loop = False
                                typing("entering the english classroom...\n")
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
                                        print("Huh? I can't understand you.")

                            case "4":
                                while encounter_loop:
                                    encounter_chance = random.choice([4, 3, 2, 1, 0])            
                                    if encounter_chance == 4:
                                        encounter()
                                    else:
                                        encounter_loop = False
                                typing("entering the the gymnasium \n") # add a classroom

                            case "5":
                                while encounter_loop:
                                    encounter_chance = random.choice([4, 3, 2, 1, 0])            
                                    if encounter_chance == 4:
                                        encounter()
                                    else:
                                        encounter_loop = False
                                typing("entering the lab\n") # once again, add a classroom

                            case "v":
                                if luck <= 2:
                                    if coins > 4:
                                        vendingchance = random.choice(vending_machine)
                                        typing("You found: \n" + vendingchance + "\n")
                                        vending_machine.remove(vendingchance)
                                        inventory.append(vendingchance) # adds item to inventory
                                        print("The locker may have the following items: ")
                                        for lockeritems in vending_machine:
                                            print(vending_machine)
                                        match vendingchance:
                                            case "CD ninja star":
                                                print("When used, this does 3 damage!")
                                                damage = damage + 3
                                            case "safety scissors":
                                                print("when used, this does 6 damage!")
                                                damage = damage + 6
                                            case "trail mix with raisins":
                                                print("when used, this heals you for 10 hitpoints!")
                                                trailmixuses = 1
                                            case "Nifty sunglasses":
                                                print("These add to your speach stat by 1!")
                                                print("Press e to equip them!")
                                                if keyboard.is_pressed("e"):
                                                    print("You equipped nifty sunglasses!")
                                                    speech = speech + 1

                                    else:
                                        print("Come back when you have at least 5 coins!")
                                        break
                                elif luck > 2:
                                    if coins > 4:
                                        chance = 0.10
                                        multiply = luck
                                        trailmixchance = luck * chance
                                        items = ['trailmix', 'sunglasses', 'cd', 'scissors']
                                        weights = [trailmixchance, 0.3, 0.4, 0.2]
                                        chosen_item = random.choices(items, weights=weights, k=1)[0]
                                        match chosen_item:
                                            case "trailmix":
                                                trailmixuses = 1
                                                typing("You found a trail mix with raisins!\n")
                                                print("This item can be used to heal 10 health 1 time.")
                                            case "cd":
                                                typing("You found the CD ninja star\n!")
                                                print("This can be used once to deal 3 damage!")
                                            case "scissors":
                                                print(test)
                                            case "sunglasses":
                                                print(test)
                                    else:
                                        print("Come back when you have at least 5 coins!")
                                        break

            if choice == "b":
                print("This is a work in progress, at the moment this cannot be played, as we spent all of our non-existant budget on the vents. This will be completed at some point later")
            # print("You now must go via the basement")
       # time.sleep(3)
       # print()
       # print("-this is creepy-, you think. You begin to hear voices...")
       # time.sleep(3)
       # print("You see two people arguing with eachother. They have clothes with two different symbols on them.")
       # time.sleep(1)
       # print("You walk up to them")
       # time.sleep(0.5)
       # print("-Hello, who are you?- they ask. You respond: -I am but a lost child, please be kind to me, for I have not felt the love of a living being in many years-")
       # print("They take pity on you, and let you stay with them for the night. When they think you are asleep, they resume their argument:")
       # typing("-No! You cannot join them, it would be considered betrayal by our clan!-\n")
       # time.sleep(0.5)
       # typing("-But what if what they say is true? What if it really is better there?-\n")
       # time.sleep(0.5)
       # typing("-You must not fall for their propoganda. You know what they are like. Now go to sleep, I don't want to here anything else coming out of your mouth until morning comes-\n")
            # this will need another story, with different situations leading to a feature that we want to implement, but a different item should be added to the players inventory first
if l.lower() == "b":
    print("this is a work in progress, this game needs a lot of work done to it before we can actually start on this level, although in the future, this will be an arcade level")
    typing("at the moment, you will be sent to the only working level, the School.\n")
    # print("Well done! You picked the right answer. You will now be rewarded with 5 coins!")
    # coins = coins + 5