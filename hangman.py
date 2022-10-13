import string
import requests
from random import choice
from PyDictionary import PyDictionary


word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
words = ""
letters_db = []  # global list to save each acceptable letter in order to avoid their repetition
win = 0
lose = 0


def get_words():
    response = requests.get(word_site)
    global words
    words = response.content.splitlines()
    response.close()


def get_meaning(r_w):
    req = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{r_w}")
    try:
        print(req.text.split("definition")[2].split('"')[2])
        print(req.text.split("definition")[3].split('"')[2])
    except IndexError:
        dc = PyDictionary()
        print(str(dc.meaning(r_w)).split("'")[3])
    finally:
        req.close()


def menu():
    while True:
        decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
        if decision == "play":
            random_word = str(choice(words)).split("'")[1]
            get_meaning(random_word)
            attempts = 8
            main(random_word, attempts)
            letters_db.clear()  # clean the list to be able to play the next game
        elif decision == "results":
            print(f"You won: {win} times.\nYou lost: {lose} times.")
        elif decision == "exit":
            break
        else:
            continue


def letter_replacement(u, rw, w):
    num_of_occurrences_of_a_letter_in_a_word = rw.count(u)
    w = list(w)
    index = 0
    while num_of_occurrences_of_a_letter_in_a_word > 0:
        index = rw.index(u, index)
        w[index] = rw[index]
        num_of_occurrences_of_a_letter_in_a_word -= 1
        index += 1
    return ''.join(w)


def check_the_input(w):
    while True:
        print("\n" + w)
        us_input = input("Input a letter: ")
        if len(us_input) > 1 or us_input in string.whitespace:
            print("Please, input a single letter.")
            continue
        elif us_input in string.ascii_uppercase or us_input in string.punctuation or us_input in string.digits:
            print("Please, enter a lowercase letter from the English alphabet.")
            continue
        elif us_input in letters_db:
            print("You've already guessed this letter.")
            continue
        else:
            letters_db.append(us_input)
            break
    return us_input


def main(r_w, a):
    word = '-' * len(r_w)
    while a > 0:
        user_input = check_the_input(word)
        if user_input in r_w:
            word = letter_replacement(user_input, r_w, word)
            if word == r_w:
                print(f"You guessed the word {word}!\nYou survived!")
                global win # write the results to the global variable
                win += 1
                break
            else:
                continue
        else:
            print("That letter doesn't appear in the word.")
        a -= 1
        if a == 0:
            print(f"\nYou lost!\nYou didn't guessed the word {r_w}")
            global lose  # write the results to the global variable
            lose += 1


if __name__ == '__main__':
    print("H A N G M A N")
    get_words()
    menu()


