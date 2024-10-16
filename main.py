# Code goes here and DO NOT FORGET INTRO COMMENTS
print('Welcome to the stick game')
print('Here is how the game is played')
#errorchecking goes here
play_again = 'yes'
while play_again == 'yes':
        player = input('either player 1,2,3:')
        sticks = int(input('How many sticks?'))
        while sticks > 0:
            print(f'it is player {player} turn')
            sticks_taken = int(input('How many sticks would you like to take?'))
            #errorchecking here
            sticks = sticks - int(sticks_taken)
            print(f'there is now {sticks} sticks left')
            if player == '1':
                player = '2'
            elif player == '2':
                player = '3'
            else:
                player = '1'
        print(f'player {player} lost. Thank you for playing!')
        play_again = input('Do you want to play again?(yes/no)')