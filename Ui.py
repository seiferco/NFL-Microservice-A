import time
import random
import os
import ast

while (True):
    print("===> Welcome to the NFL player generator <===")
    choice = input("Would you like to generate a random player? (y/n): ")
    
    if (choice == 'y'):

        rand_int = random.randint(1,23733)

        # Request random player from txt communication pipe
        with open('player-stats.txt', 'w') as image_txt_file:
            image_txt_file.write(str(rand_int))

        # Sleep for 10 seconds
        time.sleep(10)

        # Recieve random player from txt comminication pipe
        with open('player-stats.txt', 'r') as image_txt_file2:
            playerStats = image_txt_file2.read()
            playerStats = ast.literal_eval(playerStats)
            print(f"Random Player Name: {playerStats[0]}")
            print(f"College they went to: {playerStats[1]}")

        

        

    elif (choice == 'n'):
        break
    else:
        print("Unknown option")

