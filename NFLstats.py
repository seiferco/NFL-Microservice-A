import time
import os
import pandas as pd

while (True):
    #sleep for 1 second
    time.sleep(10)

    # open player-stats.txt
    with open("player-stats.txt", "r") as image_txt_file:
        content = image_txt_file.read()
    
        
    if (len(content) < 6):
        number = int(content)

        # Load data from csv file
        data = pd.read_csv('NFLstats.csv')

        playerName = data.loc[number,'name']
        college = data.loc[number,'college']

        playerStats = [playerName, college]
        
        # Write random player to player-stats.txt
        with open("player-stats.txt", "w") as image_txt_file:
            image_txt_file.write(str(playerStats))
        
 

            