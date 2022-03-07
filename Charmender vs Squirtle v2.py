import random

#STATS
strenght_squirtle = 3
ps_squirtle = 15

strenght_charmender = 4
ps_charmender = 12

#POKEMON SELECTION
pokemon = input("Do you want Charmender or Squirtle? ")

if (pokemon) == "c":
    pokemon = "Charmender"
    print("\n You have chosen Charmender \n")

if (pokemon) == "s" :
    pokemon = "Squirtle"
    print("\n You have chosen Squirtle \n")

print("TIME TO FIGHT!!! \n")

#BATTLE
while (ps_squirtle) > 1 and (ps_charmender) > 1:
    turn =  (random.randint(1,10))  
    if (turn) > 5 :
        ps_squirtle = ps_squirtle - strenght_charmender
        print("Charmender (", ps_charmender, ") attacks Squirtle (", ps_squirtle, ") \n")
    if (turn) <= 5 :
        ps_charmender = ps_charmender - strenght_squirtle
        print("Squirtle (",ps_squirtle, ") attacks Charmender (", ps_charmender,") \n")

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


