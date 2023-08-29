# TIC TAC TOE Game

The Tic Tac Toe Game is very popular and is quite simple in itself.
There will be one player in a game against the computer. Two signs represent each player. The general signs used in the game are X and O. Finally, there will be a  game board with 9 empty spaces.
## Here is live version of my project
![Picture of the website in different devices](assets/images/responsive.img.png)

Visit the deployed site: [Tic Tac Toe](https://shazi-dani.github.io/)
## User Experience (UX)

### User Stories

* As a user, I want to be able to understand how to play this game.all instructions are given in detail when start the game.

## How to Play

Tic-tac-toe (American English), noughts and crosses (Commonwealth English), or Xs and Os (Canadian or Irish English) is a paper-and-pencil game for two players who take turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner. 
Step 1 - The tic tac toe game begins with empty cells in a square grid. This is the tic tac toe board.

Step 2 - First player will place their sign in one of the available empty boxes.

Step 3 - The second user computer will place their sign in one of the available empty boxes.

Step 4 - The goal of the players is to place their respective signs completely row-wise or column-wise, or diagonally.

Step 5 - The game goes on until a player wins the game or it ended up in a draw by filling all boxes without a winning match.

you can read more about this game on  [Wikipedie](https://en.wikipedia.org/wiki/Tic-tac-toe)

## Features
* The game start with the instructions how to play and displaying game board then ask the user inputting number from 1-9.Each number represent a place on game board.
![Picture of the game board and game instructions](assets/images/)

* user plays against computer.e.g
if user enter number 1 then "X" sign will takes first spot on the board.then computer place "O" sign randomly on the board automatically when user press enter after entering number.
![Picture of the game board after entering first number](assets/images/)


* Validation is also done in this game if user enter any other number rather then 1-9 or add any other letter or space is already occupied then user can see a clear error message on the screen which shows how to resolve this errror and game run again and again until user enters valid number.
Validation Images

![Picture of all validation errors](assets/images/responsive.img.png)

* Restar Game: When game ends user can see an option " Do you want to play again then according to user input game end or restart again.

![Picture of game ending stage](assets/images/responsive.img.png)


## Future Implementations

* Update the game with few challanges which makes the game more intresting.
* User can select any sign on his own choice.
* Player can play the game with his/her name.
* Add score board which can store both players scores

## Technologies Used

### Languages used
 * Python

### Frameworks, Libraries & Programs Used

[Github](https://github.com/) - To save and store the files for the game.

[GitPod](https://www.gitpod.io/) - IDE

[Am I Responsive?](http://ami.responsivedesign.is/) To show the website image on a range of devices.

[CI Python Linter](https://pep8ci.herokuapp.com/) For resolving code errors

## Testing

Testing was ongoing throughout the entire build. I have manually tested this game by doing folowing steps:

* Passed the code through PEP8 Linter and confirmed there are no problems

![Picture of PEP8 Linter](assets/images/testing)

* Test input by giving out of range numbers,different symbols or alphebets and gve same number twice.

![Picture of all validation errors](assets/images/responsive.img.png)

* Tested in my local terminal and in Code Institue Heroku Terminal.

### Solved Bugs

* firstlly I find out validation is not working if user enters any alphbate game crash then I add a seprate validation fuction and use try and catch method for validation its works for me.all validation are working properlly now.
* Secondly when game ends user is asked for choice if he/she wants to play game again.if user enter no game ends if user enter yes game will not restert again.its start from the point where its end mean game board is not empty.

![Picture of error](assets/images/)

* then I resolved this Error by adding new function in the code setboard() which will reset game when user wants to play game again

## Credits

* Code Institute without who I would have had no base to begin a project & Readme.md Template. https://codeinstitute.net/ie/

* GitHub for my workspace and saving all my work. https://github.com/

* Gitpod for my coding. https://app.codeanywhere.com/

* The Slack community - for someone always been there no matter the time and with advice or direction. https://slack.com

* Heroku for deploying the project. https://heroku.com

* StackOverflow for all the information to assit with my project .https://stackoverflow.com

* CI Python Linter  For resolving code errors. https://pep8ci.herokuapp.com

* I am Responsive for a fantastic spot to see a visual of responsiveness . https://ui.dev/amiresponsive?url=https://8000-shazidani-gponline-9wlpxvh7fwf.ws-eu99.gitpod.io


* Youtube Tutorials and google For getting ideas and inspiration for the game.Instructions on how to right algorithm for game. [Some websites links]
(https://geekflare.com/tic-tac-toe-python-code)
(https://www.guru99.com/tic-tac-toe-python.html)
(https://geekflare.com/tic-tac-toe-python-code)

Copied Code / Code assistance As stated in Technologies / Support Used I used and sort out help and code from numerous sources. Stack over flow and Mentore Support played a huge roll in my overall development.





