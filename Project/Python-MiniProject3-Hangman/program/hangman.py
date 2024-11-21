import random, os, json


class hangman:
    def __init__(self) -> None:
        with open("words.txt", "r") as file:
            self.words = file.read().splitlines()
        
        if os.path.isfile("ranking.json"):
            with open("ranking.json", "r") as file:
                self.ranking = json.load(file)
        else:
            self.ranking = list()

    def __del__(self):
        if self.ranking:
            with open("ranking.json", "w") as file:
                json.dump(self.ranking, file)

    def game(self):
        word = random.choice(self.words)
        word = word.lower()
        guessed = "_" * len(word)
        guessed = list(guessed)
        lstguessed = []
        
        tries = 6
        while tries > 0:
            print("\nCurrent word: ", " ".join(guessed))
            lstguessed.sort()
            print("Guessed letters: ", " ".join(lstguessed))
            print(f"Incorrect guesses remaining: {tries}")
            letter = input("Guess a letter: ").lower()

            if not letter.isalpha() or len(letter) != 1:
                print("Invalid input. Please enter a single letter.")
            elif letter in lstguessed:
                letter = ""
                print("Already guessed!!")
            elif letter not in word:
                tries -= 1
                print(f"Sorry, '{letter}' is not in the word.")
                lstguessed.append(letter)
            else:
                print(f"Good job! '{letter}' is in the word.")
                lstguessed.append(letter)
                for i in range(len(word)):
                    if letter == word[i]:
                        guessed[i] = letter

            if "_" not in guessed:
                print(f"Congratulations! You guessed the word!: {word}\n")

                if input("Do you want to save your score? (yes/no): ").lower() == "yes":
                    name = input("Please enter your name: ")
                    self.ranking.append({"name": name, "tries": tries})
                    self.ranking = sorted(self.ranking, key=lambda k: k["tries"], reverse=True)
                    self.ranking = self.ranking[:5]

                    print("\nTop 5 ranking:")
                    for i, player in enumerate(self.ranking):
                        print(f"{i+1}. {player['name']} with {player['tries']} tries left.")
                break
        else:
            print(f"You ran out of tries. The word was {word}\n")

    def start(self):
        print("Welcome to Hangman!")
        while True:
            self.game()
            if input("\nDo you want to play again? (yes/no): ").lower() != "yes":
                break


def main():
    game = hangman()
    game.start()

if __name__ == "__main__":
    main()
        