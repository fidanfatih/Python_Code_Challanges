'''
Rock-Paper-Scissors Game
'''

from random import choice
from time import sleep

player_1 =input('1st Player Name: ').upper()
player_1_points =0

player_2 = input('2st Player Name: ').upper()
player_2_points=0

colors={player_1:'\033[92m', 
        player_2:'\033[94m', 
        'draw':'\033[91m'}

mylist = ["Rock","Paper","Scissors"]
tour = 10

for i in range(tour):
    case_1=choice(mylist)
    sleep(0.11)
    case_2=choice(mylist)
    winner='draw'
    if (case_1 != case_2):
        if ((case_1=='Rock' and case_2=='Scissors') or 
            (case_1=='Scissors' and case_2=='Paper') or 
            (case_1=='Paper' and case_2=='Rock')):
            winner=player_1
            player_1_points+=1
        else: 
            winner=player_2
            player_2_points+=1
    print(f'{colors[winner]}{i+1:<2}- {player_1} :{case_1:<8}',
          f'{player_2} :{case_2:<8}',
          f'=====> Winner:{winner}')

    
winner=player_1 if player_1_points > player_2_points else player_2 if player_1_points < player_2_points else 'draw'
print(f'\n{colors[winner]}{player_1}:{player_1_points}   {player_2}:{player_2_points}'
        f'\nWINNER is {winner} !')


# In[ ]:




