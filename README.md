# 132project
Description: This is a python-built number guessing game that prompts the user to correctly guess a number between 1-100 chosen by the computer. You must do this within a limited amount of attempts. The amount of attempts vary upon difficulty level. The easy level is 25 attempts, the medium level is 15 attempts, and the hard level is 10 attempts. You can pick whichever difficulty you want, just make sure you don't run out of attempts.

INSTRUCTIONS:

    1. Run the python file to begin the game
    2. Select your game difficulty when asked("Choose game difficulty - easy, medium, or hard)
    3. Read the instructions/prompt to ensure you know how many attempts you have to guess the number correctly.
    4. Enter your first guess
    5. Read the feedback you receive after your guess("Too Low" or "Too High" or "Correct!")
    6. If your guess was correct then the game will end, but if it wasn't then use the feedback and keep guessing.
    7. After you correctly guess the number or run out of attempts, the game will finally end.

Final Report - 
Project Description:
	*This project is a number guessing game where the computer randomly selects a number between 1-100 and the player has to attempt to   guess the number. This is a single-player and terminal-based python program. After each attempt from the player, the program will provide feedback telling whether or not your guess was too high, too low, correct, or an invalid input. The game ends when the user guesses the number correctly or runs out of attempts. This game has difficulty levels as well. There is easy, medium, or hard. Each level contains a different amount of attempts to get guess the number correctly. For the easy level, the player has 25 attempts. For the medium level, the player has 15 attempts. For the hard level, the player has 10 attempts. The player is allowed to choose its difficulty level based on their preference. The amount of attempts a player takes is tracked as well, and the player will be notified how much attempts it took them to guess the number correctly.*

Approach/Logic Used:
	*I organized this program into two functions; get_difficulty() and number_guessing_game(). The get_difficulty() function is the part that prompts the user to select a difficulty level. This function uses a while loop to validate the input of the difficulty level. It makes sure the user inputs easy, medium, or hard. After player inputs a valid difficulty level, the function will assign the player a maximum number of attempts based on their selection. The number_guessing_game() function is what handles the main game logic. Firstly, it generates a random number between 1 and 100 by using random.randint(1,100). A while loop is then used to repeatedly ask the player to enter a guess until they either make the correct guess or they have reached the maximum attempts. If and elif statements are used within the loop to provide feedback(“Too Low” or “Too high” or “Correct”) to the player as they play the game.* 

Data Structures:
	*The main use of data structure within this program is a dictionary, specifically the dictionary, attempts_difficulty. This dictionary is used to map the difficulty levels to the maximum number of attempts. It maps the easy level to 25 attempts, the medium level to 15 attempts, and the hard level to 10 attempts. This simplifies the process of assigning the attempt limits based on user input, making the program more efficient.*

Challenges Faced:
	*The main challenge I faced was input validation. I was originally having trouble with making sure the game/program didn’t crash when a player enters an invalid input. I wanted to make sure my program had a response for every possible invalid answer. Luckily, I remembered the isdigit() method because at first, I was trying to figure out how to make sure the input was a number.* 

Possible Improvements:
	*There are most definitely ways to improve this project. Firstly, assisting the player even more by making sure the player’s guess is within 1-100. I already let the user know it is a number between 1-100 and tell them if their guess is too high or too low, but extra assistance would only enhance the gameplay. Another improvement would be to include replay. Being able to replay the game without having to restart the program would make the game more convenient and fun for people to play.*
	
