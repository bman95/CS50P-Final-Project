# Coin Grab Game

### Video Demo: https://youtu.be/RfDzAEzTVls

### Description:

"Coin Grab" is a captivating logic game developed in Python, designed to challenge your strategic thinking against a machine opponent. The game begins with a specified number of coins, typically 15, and players take turns to grab between one and three coins from the pile. The objective is to avoid being the player who takes the last coin, as doing so results in a loss. This simple yet intriguing game requires careful planning and foresight to outsmart the machine and emerge victorious.

## Project Files

The project consists of a single Python script, `project.py`, which contains the entire game logic and implementation. Below is a detailed explanation of the script and its components:

### project.py

- **Imports:**
    - `random`: Used to randomly decide the starting player and, if necessary, the number of coins the machine will take.
    - `time`: Utilized to create a pause, simulating the machine "thinking" for added effect.
- **ANSI Escape Sequences:**
    - These sequences are used to add color to the text printed in the terminal, enhancing the user experience.
- **Functions:**
    - `main()`:
        - Prints the game introduction and instructions.
        - Prompts the user to enter the starting number of coins.
        - Initiates the game by calling `coin_game(coins)` with the specified number of coins.
    - `player_takes_coins()`:
        - Prompts the user to take between one and three coins.
        - Validates the input and returns the number of coins taken.
    - `take_coin(coins_to_take)`:
        - Checks if the number of coins taken is within the valid range (1-3).
        - Returns the number of coins taken or an error message if the input is invalid.
    - `computer_takes_coins(coins)`:
        - Simulates the computer "thinking" by printing dots with delays.
        - Uses a basic strategy to determine the number of coins to take, aiming to avoid losing.
        - Returns the number of coins the machine takes.
    - `wining_situation(current_player)`:
        - Determines and returns the winning situation message based on the current player (human or machine).
    - `coin_game(coins)`:
        - Decides who starts the game (human or machine) and announces it.
        - Contains the main game loop where players alternately take coins until none remain.
        - Announces the result of the game based on who took the last coin.

## Design Choices

1. **User Interaction:**
    - The game interacts with the user via the terminal, utilizing ANSI escape sequences to provide colored text feedback. This enhances the gaming experience and makes the output more engaging.
2. **Game Strategy:**
    - The computer uses a basic strategy to decide the number of coins to take. The strategy aims to leave a number of coins such that the remaining coins modulo 4 equals zero, placing the human player in a disadvantageous position. If this is not possible, the computer takes a random number of coins (1-3).
3. **Random Start:**
    - To keep the game fair and unpredictable, the starting player is chosen randomly at the beginning of each game.
4. **Error Handling:**
    - The game includes robust error handling for user inputs, ensuring that only valid numbers of coins (1-3) are taken and prompting the user to correct any invalid inputs.
5. **User Experience:**
    - To make the machine's actions feel more realistic, a brief pause is introduced to simulate "thinking time" before the machine takes its turn.

## Conclusion

"Coin Grab" is a straightforward yet engaging game that combines elements of strategy and luck. By coding this game in Python and using terminal-based interaction, the project demonstrates the application of basic programming concepts, user input handling, and simple AI strategies. The colorful output and strategic gameplay make it an enjoyable challenge for players.

Feel free to clone the repository, experiment with different starting numbers of coins, and refine the strategy to improve the game's AI. Have fun playing "Coin Grab" and may the best strategist win!
