import random


def guessing_game():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 10 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")

    secret_number = random.randint(1, 10)

    attempts = 0

    while True:
        if attempts == 3:
            print('You lose!')
            break

        guess = input("What's your guess between 1 and 10?\n>> ")

        if guess.lower() == 'exit':
            print("Goodbye!")
            break

        if not guess.isdigit():
            print("That's not a number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            if attempts == 1:
                print("Congratulations! You got it on your first try!")
            else:
                print(f"Congratulations, you've got it!")
                print(f"You won in {attempts} attempts!")
            break


def rock_paper_scissors():
    print("You have to choice between rock paper or scissors by typing its number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")

    pointsplayer = 0
    pointspc = 0

    while True:
        if pointsplayer == 3:
            print('Congratulations, you won!')
            break
        elif pointspc == 3:
            print('You lost!')
            break

        print("\nSelect your choice:")
        print("1: Rock")
        print("2: Paper")
        print("3: Scissors")

        pc_choice = random.randint(1, 3)

        player = input("Type your choice:\n>> ")

        if player.lower() == 'exit':
            print("Goodbye!")
            break

        if not player.isdigit():
            print("That's not a number.")
            continue

        player = int(player)

        print(f'Pc selected {pc_choice}')

        if player < 1 or player > 3:
            print('Select a number between 1 and 3!')
        elif player == 1 and pc_choice == 3:
            print('Round won! +1 point')
            pointsplayer += 1
        elif player == 2 and pc_choice == 1:
            print('Round won! +1 point')
            pointsplayer += 1
        elif player == 3 and pc_choice == 2:
            print('Round won! +1 point')
            pointsplayer += 1
        elif player == pc_choice:
            print('Draw!')
        else:
            print('Round lost! Pc gained 1 point.')
            pointspc += 1


def hanged():
    with open('palabras.txt', 'r') as file:
        words = [line.strip() for line in file.readlines()
                 if 3 <= len(line.strip()) <= 7]

    secret_word = random.choice(words).lower()
    word_length = len(secret_word)
    attempts = word_length * 2
    guessed_word = ['_'] * word_length
    guessed_letters = []

    print("Welcome to The Hanged game!")
    print(f"The word has {word_length} letters.")
    print("You have", attempts, "attempts.")

    while attempts > 0:
        print("\nCurrent word: " + ' '.join(guessed_word))
        guess = input("Guess a letter:\n>> ").lower()

        if guess == 'exit':
            print("Goodbye!")
            break

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            for idx, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[idx] = guess
        else:
            print(f"Sorry, the letter '{guess}' is not in the word.")
            attempts -= 1

        if '_' not in guessed_word:
            print("\nCongratulations, you guessed the word:", secret_word)
            break

        print(f"Attempts left: {attempts}")

    if attempts == 0:
        print(f"\nGame over! The word was: {secret_word}")


def print_menu():
    print("\nList of available options:")
    print("1: Guess the number")
    print("2: Rock paper scissors")
    print("3: The Hanged")
    print("4: Quit")


def main():
    print("Welcome to the Python Gameroom!")

    while True:
        print_menu()
        choice = input("Please select an option: ")

        if choice == "1":
            guessing_game()
        elif choice == "2":
            rock_paper_scissors()
        elif choice == "3":
            hanged()
        elif choice == "4":
            print("Exiting the gameroom. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
