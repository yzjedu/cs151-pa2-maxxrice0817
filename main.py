# Code goes here and DO NOT FORGET INTRO COMMENTS
import random

print('Welcome to the stick game')
print('Here is how the game is played')
#errorchecking goes here
play_again = 'yes'
while play_again == 'yes':
        player = input('either player 1,2,:')
        sticks = int(input('How many sticks will there be to begin with?'))
        while sticks > 0:
            print(f'it is player {player} turn')
            if player == '3':
                sticks_taken = random.randint(1, 3)
                print(f'Player 3 has taken {sticks_taken} stick')
            if player == '2' or player == '1':
                sticks_taken = int(input('How many sticks would you like to take?'))

#errorchecking here
            sticks = sticks - int(sticks_taken)
            print(f'there is now {sticks} sticks left')
            if player == '1':
                player = '2'
            elif player == '2':
                player = '3'
            elif player == '3':
                player = '1'

        print(f'player {player} lost. Thank you for playing!')
        play_again = input('Do you want to play again?(yes/no)')