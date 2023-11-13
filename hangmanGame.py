import random as r
# Prints out the blanks/correct guesses of word
def word_print(word_length):
    for num in range(len(word_length)):
        if num == len(word_length) - 1:
            print(word_length[num])
        else:
            print(word_length[num], end=" ")
# Sets up the word to be used
words = ["baseball", "football", "soccer", "basketball", "volleyball", "hockey"]
word_choice_int = r.randint(0, len(words) - 1)
word_choice = words[word_choice_int]
word_choice_list = []
for letter in word_choice:
    word_choice_list.append(letter)

# Sets up the blank spaces for the word
length = len(words[word_choice_int])
word_length = []
for i in range(length):
    word_length.append("_")
word_print(word_length)

# User guesses check against word
guesses_left = 3
total_guesses = 0
guess_list = []
while guesses_left != 0:
    print("You have " + str(guesses_left) + " guesses left")
    guess = input("Type in your letter guess: ")
    total_guesses += 1
    guess = guess.lower()
    guess_check = False
    duplicate_letters = 0
    guess_duplicate = False
    guess_list.append(guess)
    if total_guesses >= 2:
        for letter in guess_list:
            if guess == letter:
                duplicate_letters += 1
            if duplicate_letters == 2:
                print("You've already guessed that letter. Try a different one.")
                guess_duplicate = True
                guess_list.pop()
    if guess_duplicate == False:
        for i in range(len(word_choice_list)):
            if guess == word_choice_list[i]:
                word_length[i] = guess
                guess_check = True
        if guess_check == True:
            print("Great job the letter \"" + guess + "\" is in the word")
        else:
            guesses_left -= 1
            print("Sorry the letter \"" + guess + "\" is not in the word.")
        if word_length == word_choice_list:
            print("You Win! The word is " + word_choice)
            break
        if guesses_left == 0:
            print("Sorry you lose. The word is " + word_choice)
            break
        word_print(word_length)