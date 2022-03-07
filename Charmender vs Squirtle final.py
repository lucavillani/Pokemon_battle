from pickle import TRUE
import random
from re import S

print(" \n WELCOME TO THE POKEMON ARENA \n")

play = True


def pokemon_battle(): 
    #POKEMON STATS
    ps_squirtle = 18
    ps_charmender = 14
    print("""You can choose between:
            
            CHARMENDER                                SQUIRTLE
        HP      |       ATTACKS                   HP      |       ATTACKS
        14      |       Scratch (4, 50%)          18      |       Bubble (3, 90%) 
                |       Flamethrower (5, 50%)             |       Idropump (10, 10%) \n""")
    #POKEMON SELECTION 
    pokemon = input("Do you want Charmender or Squirtle? ")

    if (pokemon) == "C":
        pokemon = "Charmender"
        print("\n You have chosen Charmender \n")

    if (pokemon) == "S" :
        pokemon = "Squirtle"
        print("\n You have chosen Squirtle \n")

    print("TIME TO FIGHT!!! \n")

    #BATTLE
    while (ps_squirtle) >= 1 and (ps_charmender) >= 1:
        turn = (random.randint(1,10))  
        
        if (turn) > 5 :
            attack_type_charmender = (random.randint(1,10)) 
            if (attack_type_charmender) > 5 :
                attack_strenght_charmender = 5
                attack_name_charmender = "Flamethrower"
            if (attack_type_charmender) <= 5 :
                attack_strenght_charmender = 4
                attack_name_charmender = "Scratch"
            ps_squirtle = ps_squirtle - attack_strenght_charmender
            print("Charmender uses", attack_name_charmender, "--> Squirtle loses", attack_strenght_charmender,"ps           Charmender:", ps_charmender, "ps | Squirtle:", ps_squirtle, "ps \n")
        
        if (turn) <= 5 :
            attack_type_squirtle = (random.randint(1,10)) 
            if (attack_type_squirtle) > 9 :
                attack_strenght_squirtle = 10
                attack_name_squirtle = "Idropump"
            if (attack_type_squirtle) <= 9 :
                attack_strenght_squirtle = 3
                attack_name_squirtle = "Bubble"
            ps_charmender = ps_charmender - attack_strenght_squirtle
            print("Squirtle uses", attack_name_squirtle, "--> Charmender loses", attack_strenght_squirtle,"ps            Charmender:", ps_charmender, "ps | Squirtle:", ps_squirtle, "ps \n")

    #DECLARING VICTORY
    if (ps_squirtle) < 1:
        print("Squirtle is dead \n")
        if (pokemon) == "Squirtle":
            print("YOU LOST \n")  
        if (pokemon) == "Charmender": 
            print("YOU WON \n")   

    if (ps_charmender) < 1:
        print("Charmender is dead \n")
        if (pokemon) == "Charmender":
            print("YOU LOST \n")
        if (pokemon) == "Squirtle":
            print("YOU WON \n")

while play:
    pokemon_battle()

    #PLAY AGAIN? QUALCHE ERRORE QUANDO SI CAMBIA POKEMON
    again = str(input("Do you want to play again (Y/N)? "))
    if again == "N":
        print("Thank you and goodbye! \n")
        play = False
    else:
        pokemon_battle()  

#AGGIUNGERE CONTATORE VITTORIE/SCONFITTE