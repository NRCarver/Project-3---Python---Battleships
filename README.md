# Battleships - A python game 

[Link to Game](https://battleships-python-project3.herokuapp.com/)

I have created a game of battleships, written in Python, that can be played using the Code Institue mock terminal on Heroku.

Battleships is a simple game where you and you opponent have a battleship hidden somewhere on your grid. You take it in turns to guess where your opponents battleship is and whoever sinks the others ship is the winner!

### How to Play

 Battleships is a game of luck and after entering your name and the board dimensions, the player will guess one of the computers coordinates on their grid by selecting the row and column of their choice. Note that the grid starts at (0,0) in the top left corner. If the player hits the computers ship, the game ends. If the player misses, then the computer will guess a coordinate. Gameplay continues until either the player or computer hits the opponents battleship and the game is over!

![](./assets/README%20images/battleships_logic.png)
![](./assets/README%20images/intro_screenshot.png)
![](./assets/README%20images/board_creation.png)
![](./assets/README%20images/board_w_guess_screenshot.png)
![](./assets/README%20images/youwin_screenshot.png)

 ### Features

 - Enter your name to name your grid.
 - Select the grid size from 3x3 up to 7x7.
 - You battleship is randomly assigned on your board and the terminal will tell you where your ship has been placed.
 - The player cannot see the computers battleship.
 - After each miss, the guessed coordinate will change from 'O' to '-' so the player can see all their previous guesses.

 ### Game Validation 

 - The game will not allow the user to have the name 'Computer' and they must pick another.
 - The user has to enter proper integers for their guesses.
 - The user is not able to guess grid coordinates that are not available.


 ### Future Features to implement

 - On larger board sizes, the players will have multiple ships.
 - Allow the player to place their ships manually.


 ## Testing

 - PEP8 linter was used to validate my code.

 Initially my code was too long on certain lines so have introduced breaks at appropriate times or split strings to avoid this issue.

 - Manual Testing 

 I have manually tested my game to make sure appropriate error messages come up when players incorrectly input. I have also asked some friends and family to play my game and none have reported any issues.

## Bugs 

During the games creation I ran into quite a few bugs but luckily was ale to quickly spot and rectify them by frequently running my code and checking outputs in Gitpod. A few of the larger bugs that I solved are:

- The computer only having a single guess. Initially the random guess generated for the computer was in the global scope so the computer only had a single guess. I put the computers guess into a local function so it would create a new guess each round.

- Restarting the game. Initially I struggled to restart my game until I put all my code in a while loop so you can keep playing or break to quit the game.

## Languages and Technologies used

- Python: The programming language for the project is Python.

- Python random library: random.randint was used to generate random integer which were used for ship placement and computer guesses.

- GitHub: GitHub was used to store the projects code after being pushed from Git.

Gitpod: Gitpod was used to write, commit and push my code.

Heroku: Used to deploy my code.

## Deployment

The Code Institute Mock Terminal for Heroku was used to deploy my project and I took the following steps.

Steps for deployment:

Create a new Heroku app.
Set the buildpack in the setting to "heroku/python" and "heroku/nodejs".
In the "Deploy" menu, GitHub was chosen for "Deployment method".
Connect and choose the repository in the "App connected to GitHub".
Choose either "Automatic deployment" so every later push will deploy a new version of this app.

