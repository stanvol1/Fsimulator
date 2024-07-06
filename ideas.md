# Bosses
- A level 10 boss of some type, maybe a demon father, who transformed after a freak accident
- Teacher boss, at the end of the school level
# New UI ideas (example: health, defence etc)

- inventory array including keys and quest items, not able to be sold

- Maybe include basic tier character building like Fallout? I propose: Strength, Intuition, Speech and Luck as the only 4, have the player assign points at the start
  - Maybe add collectibles that increase said stats? (charms)
  - Include (special) actions that require a minimum stat requirement

- System that does a "dice roll" after a certain number of player actions to determine whether the player will have an encounter or not.

- System that acts as a shanty inventory, maybe allow 2 pieces of Armor (Head and body), 3 consumables and a light and heavy weapon at any given time and a charm. We could use a simple array to store that data.

- Basic turn based combat with consumable use and attack (either use consumable or attack, can't do both in the same turn obv.)

- Should we allow for 2 weapons or just one? Having two weapons in combat might allow for more creative plays.
  - We could introduce a heavy and light weapon class to balance things out, make sure people don't just spam heavy attacks.

- Consumable item duration to further encourage strategy (1 turn being instant heal).

- Further uses for Stats outside of in game actions to encourage character building, reminder that all of these are for per point assigned:
  - Strength:
    - +1 heavy damage

  - Luck:
    - +3% dodge (base chance = 5%)
    - +5% coin
  
  - Intuition:
    - +1 light damage

  - Speech:
    - Idk tbh, maybe  offer pacifist options in some fights?
    - we could give better options to players with higher speech

- UI print out that specifies the temporary and non temporary buffs you have from items.

- a sort of "reputation" system, which can be used in clans
# Ideas for parts of levels

- One of those McDonald's style plastic jungle jim play areas with all sorts of weird little characters.
- A school level, where you have to navigate through the social hierarchy, interacting with people as you go along. Maybe this can be level 5.
- clans, groups you could join. They can give good rewards if your reputation among the clan itself is high enough. I don't know when we would code this, but we could store reputation in a variable. The interactivity of this could be added later. 
# Item Ideas

## Weapons

### Light

- "Concerningly sharp paper airplane": (light)
  - Damage: 3
  - Uses: 3
  - Cost: found at school (later thing)

- "Charger cable whip": (light)
  - Damage: 1
  - Uses: 7
  - Cost: 5

- "Respiratory risk hair spray": (light)
  - Damage: 1 per turn (stacks)
  - Uses: 10
  - Cost: ???

- "Surprisingly throwable snow-globe": (light)
  - Damage: 15
  - Uses: 1
  - Cost: ???

- "CD ninja star": (light)
  - Damage: 4
  - Uses: 3
  - Cost: ???

### Heavy

- "Scuffed Badminton Racket": (heavy)
  - Damage: 7
  - Uses: 5
  - Cost: found in-game

- "Safety Scissors": (heavy)
  - Damage: 6
  - Uses: 6
  - Cost: 7 


## Consumables

- "Chonky-donky choco bar"
  - Effect: +3 Health
  - Duration: 1 turn
  - Cost: 3

- "Trail mix with raisins"
  - Effect: +8 health
  - Duration: 1 turn
  - Cost: 5 (given the 10 health, this is a huge buff)

- "Left over lasagna"
  - Effect: +6 health, -1 Strength
  - Duration: 1 turn
  - Cost: 3

- "Extremely minty gum"
  - Effect: +1 health, +1 Speech
  - Duration: 1 turn for health, Speech lasts until the end of the level.
  - Cost: 2

- "Unicorn sticker bandaids"
  - Effect: +2 health per turn
  - Duration: 3 turns
  - Cost: ???

## Armor

### Head Armor

- "Nifty sunglasses"
  - Defense: 1
  - Effect: +1 Speech
  - Cost: 2

- "Mildly scary glow-in-the-dark halloween mask"
  - Defense: 3
  - Effect: -1 Speech
  - Cost: 3

### Body Armor:

- "Cub scouts outdoor sweater"
  - Defense: 3
  - Effect: null
  - Cost: found in game

- "Padded Labor Jumpsuit"
  - Defense: 10
  - Effect: -1 Speech, +1 Strength
  - Cost: 3

## Charms

- "Pocket sized print of 1984"
  - Effect: +1 Intuition, +3 Reputation
  - Cost: found at school library maybe (maybe we can make it one of the endings of the school level)

- "Polished 8-ball"
  - Effect: +1 Luck
  - Cost: 2

- "Motivational poster"
  - Effect: +2 Strength, -1 Speech
  - Cost: given in the vents


