from pickle import TRUE
import random
from re import S

play = True

#POKEMON STATS
hp_charmender = 14
scratch = ["Scratch", 4]
flamethrower = ["Flamethrower", 5]
attacks_charmender = [scratch, flamethrower]
attack_probability_charmender = [60, 40]
charmender = ["Charmender", hp_charmender, attacks_charmender, attack_probability_charmender]

hp_squirtle = 18
bubble = ["Bubble", 3]
idropump = ["Idropump", 10]
attacks_squirtle = [bubble, idropump]
attack_probability_squirtle = [90, 10]
squirtle = ["Squirtle", hp_squirtle, attacks_squirtle, attack_probability_squirtle]

hp_bulbasaur = 16
tackle = ["Tackle", 3]
razor_leaf = ["Razor Leaf", 7]
attacks_bulbasaur = [tackle, razor_leaf]
attack_probability_bulbasaur = [70, 30]
bulbasaur = ["Bulbasaur", hp_bulbasaur, attacks_bulbasaur, attack_probability_bulbasaur]

pokemon = (charmender, squirtle, bulbasaur)
pokemon_player = pokemon
pokemon_opponent = pokemon
turn = [0,1]



def pokemon_royale():

    #WELCOME
    print(" \n WELCOME TO THE POKEMON ARENA \n")

    #POKEMON SELECTION
    pokemon_choice = input("Which Pokemon do you want to choose? ") 
    if (pokemon_choice) == "C":
        pokemon_player = pokemon[0]
    elif (pokemon_choice) == "S":
        pokemon_player = pokemon[1]
    elif (pokemon_choice) == "B":
        pokemon_player = pokemon[2]
    pokemon_opponent = random.choice(pokemon)
    while pokemon_opponent == pokemon_player:
        pokemon_opponent = random.choice(pokemon)
        
    print("\nYou have chosen", pokemon_player[0], "\n")
    print("Your opponent has chosen", pokemon_opponent[0], "\n")

    print("TIME TO FIGHT!!! \n")
    
    while (pokemon_player[1]) >= 1 and (pokemon_opponent[1]) >= 1:
        
        #ESTABLISHING ATTACKING TURNS  
        current_turn = (random.choice(turn))

        if (current_turn) == 0:
            attacking_pokemon = pokemon_player
            defending_pokemon = pokemon_opponent
        else:
            attacking_pokemon = pokemon_opponent
            defending_pokemon = pokemon_player

        #BATTLE
        attack = (random.choices(attacking_pokemon[2], weights=(attacking_pokemon[3]), k=1))
        defending_pokemon[1] = defending_pokemon[1] - int((attack[0][1]))
        print(attacking_pokemon[0], "uses",(attack[0][0]), "--->",defending_pokemon[0], "loses", int((attack[0][1])), "ps       ", pokemon_player[0][0:4].upper(),pokemon_player[1],"|", pokemon_opponent[0][0:4].upper(),pokemon_opponent[1], "\n")

    #DECLARING VICTORY
    if (pokemon_player[1]) < 1:
        print(pokemon_player[0],"is dead \n")
        print("YOU LOST \n")

    if (pokemon_opponent[1]) < 1:
        print(pokemon_opponent[0],"is dead \n")
        print("YOU WON \n")


#GAME LOOP
while play:
    pokemon_royale()

    #PLAY AGAIN? - CURRENTLY NOT RESETTING POKEMON'S HP
    again = str(input("Do you want to play again (Y/N)? "))
    if again == "N":
        print("Thank you and goodbye! \n")
        play = False
    else:
        play = True 