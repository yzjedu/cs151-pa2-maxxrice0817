#Programmer: Max Rice
#Course: CS151, [Dr. Yalew]
#Assignment due: 10/23/2024
#Programming assignment: PA 2
#Problem statement: program runs a game of sticks where the goal is to grab the last stick
#Data in: Player number, amount of stick you start with, amount of sticks taken each turn, PLay again
#Data out: Welcome, how game is played, number of sticks left, loss count for each player,thanks for playing, ask if player would like to play again
#Purpose of program: to create a game of sticks which showcases all I have been learning in class
import random
from unicodedata import digit

#Set all loses equal to zero to begin with
p1_loss = 0
p2_loss = 0
p3_loss = 0


print('Welcome to the stick game')
print('Here is how the game is played: there will be an initial amount of sticks and the goal is to not grab the last stick \nplayer one and two will both be played by the two users and player three will be played by a computer.')
#errorchecking goes here
play_again = 'yes'
while play_again == 'yes':
        player = input('either player 1,2,:')
        if player < '1' or player > '2':
                player = input('please enter either 1 or 2')
        sticks = int(input('How many sticks will there be to begin with?'))
            print('zoinks')
            print(f'it is player {player} turn')
            if player == '3':
                sticks_taken = random.randint(1, 3)
                print(f'Player 3 has taken {sticks_taken} stick')
            if player == '2' or player == '1':
                sticks_taken = int(input('How many sticks would you like to take between 1 and 3?'))
                if sticks_taken != 1 or sticks_taken != 2 or sticks_taken != 3:
                    input('please enter either 1, 2, or 3')

#errorchecking here
            sticks = sticks - int(sticks_taken)
            print(f'there is now {sticks} sticks left')
            if player == '1':
                player = '2'
            elif player == '2':
                player = '3'
            elif player == '3':
                player = '1'
#counting and displaying number of losses per player
            if player == '1':
                p1_loss += 1
            if player == '2':
                p2_loss += 1
            if player == '3':
                p3_loss += 1
            print(f'player {player} lost. Thank you for playing!')
            print('Player one losses', p1_loss, '\nPlayer two losses', p2_loss, '\nPlayer three losses', p3_loss)
            play_again = input('Do you want to play again?(yes/no)').lower()

            if play_again == 'no':
                print('Thank you for playing!')