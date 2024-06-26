import random
import time

# ANSI escape sequences for colors to print colored text in the terminal
RESET = '\033[0m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'


def main():
    # Print the game introduction and instructions
    print(f'''
    {MAGENTA}"Coin Grab" is a logic game developed in Python, without a graphical interface, where two players compete not
    to be the last one to take the final coin. It starts with a fixed amount of coins, typically 15. On each turn,
    players can take from one to three coins. The player who takes the last coin loses. Challenge your strategy and
    logic to ensure you don't end up with the final coin!

    This time you will play against the machine.
    Can you beat it?
    ''')

    # Prompt the user to enter the starting number of coins
    while True:
        try:
            coins = int(
                input(f'{MAGENTA}How many coins do you want to start the game with? {RESET}'))
            if coins > 0:
                break
            else:
                print(f'{RED}Please enter a positive number of coins.')
        except ValueError:
            print(f'{RED}Invalid input! Please enter a valid number of coins.')

    # Start the game with the given number of coins
    coin_game(coins)


def player_takes_coins():
    # Loop until the player enters a valid number of coins to take
    while True:
        try:
            coins_to_take = int(
                input(f'{GREEN}How many coins do you take? (1-3): {RESET}'))

            # Validate and return the number of coins taken
            return take_coin(coins_to_take)

        except ValueError:
            print(f'{RED}Invalid input! Please enter a number between 1 and 3.\n')


def take_coin(coins_to_take):
    # Check if the number of coins taken is within the valid range
    if 1 <= coins_to_take <= 3:
        return coins_to_take
    else:
        raise ValueError


def computer_takes_coins(coins):
    # Simulate the computer "thinking" by printing dots with delays
    print(f"{CYAN}The machine is thinking", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(RESET)

    # Compute the number of coins for the computer to take using a basic strategy
    algorithm = (coins - 1) % 4
    coins_to_take = algorithm or random.randint(1, 3)
    print(f'{CYAN}The machine takes {coins_to_take} coins.')
    return coins_to_take


def wining_situation(current_player):
    # Determine and return the winning situation message based on the current player
    if current_player == 2:
        return f'\n{RED}YOU LOSE! You took the last coin.{RESET}\n'
    else:
        return f'\n{GREEN}YOU WIN! The machine took the last coin.{RESET}\n'


def coin_game(coins):
    # Decide and print who starts the game
    print(f"{YELLOW}\nDeciding who starts the game", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print('')

    current_player = random.choice([1, 2])
    if current_player == 1:
        print(f"{GREEN}YOU start the game!")
    else:
        print(f"{CYAN}The machine starts the game!")

    # Main game loop
    while coins > 0:
        # Print the current state of the game
        print(f'\n{WHITE}Coins remaining: {coins}')

        if current_player == 1:
            # Human player's turn
            coins_taken = player_takes_coins()
        else:
            # Computer's turn
            coins_taken = computer_takes_coins(coins)

        # Update the number of coins
        coins -= coins_taken

        # Alternating between human player and computer
        current_player = 3 - current_player

    print(f'\n{WHITE}Coins remaining: 0')

    # Print the result of the game
    print(wining_situation(current_player))


if __name__ == '__main__':
    main()
