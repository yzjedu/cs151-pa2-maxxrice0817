# Final Design Document
#### PLEASE! PLEASE! PLEASE! Complete all the NOs in the feedback document 
1. import random

2. set p1_loss equal to zero
3. set p2_loss equal to zero
4. set p3_loss equal to zero


5. Print 'WELCOME TO THE STICK GAME'
6. output 'The rules of the game: 3 players each take turns drawing sticks from a pile and the player who pulls the last stick losses. player one and two are users while player three is the computer'
7. ask user to input "would you like to play a game of sticks? yes or no" and set answer to play
8. While play equals yes
   - 1. ask user "which will start player one or two"
   - 2. while player does not equal one or two
     - 3. output "INVALID INPUT: please enter either one or two"
   - 4. set starting sticks to user inputs
   - 5. If user input is not an integer 
   
   - 6. while sticks is greater then 1
     - 7. if player equals 1 or 2
       - 8. output "it is the {value of player} turn"
       - 9. ask user to pick a number of sticks to take between 1 and 3 and set that to sticks taken
       - 10. while sticks taken is greater than 3 or less than 1
        - 11. ask user to pick a number of sticks to take between 1 and 3 and set that to sticks taken
       - 12. if value of player is 3 
         - 13. if sticks is equal to 2
             14. player 3 takes 1 stick
           15. if sticks is equal to 3
               16. player 3 takes 2 sticks
           17. if sticks is equal to four
               18. player 3 takes 3 sticks
         19. otherwise sticks taken is a random integer between 1 and 3
       - 20. set sticks to number of sticks minus sticks taken
       - 21. output "there is now (value of sticks) sticks left"
     - 22. if player equals one 
          - 23. set players equal to two 
     - 24. else if players equal to two 
       - 25. set players equal to three
   - 26. if player equals one
     - 27. add one to p1_loss
   - 28. if player equals two
     - 29. add one to p2_loss
   - 30. if player equals to three
     - 31. add one to p3_loss

9. output " {value of player} player lost thanks for playing"
10. out "player one losses {value of p1_loss}, player two losses {value of p2_loss}, player 3 losses {Value of p3_losses}"
11. ask user to input if they would like to play again and set value to play
  - 11a. set answer to all lowercase
12. if play again is no
  - 12a. output "thanks for playing"
13. while play again doe not equal 'yes' or 'no'
  - 13a. ask user to input if they would like to play again? yes or no?
    - set answer to lowercase