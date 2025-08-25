from drawing import man_art
import requests
import sys

def get_word():
    url="https://random-word-api.herokuapp.com/word"
    response=requests.get(url)
    if response.status_code==200:
        for word in response.json():
            return word
    else:
        print("Word not imported")
        sys.exit(0)

word=get_word()
ctr_attempt=0
ctr_end=0
guess=""
wrong=[]
display=[]
vowels=['a','e','i','o','u']
dots=[]

def printer(num):
    for line in man_art.get(num):
        print(line)

for x in range(len(word)):
    display.append("_")

for character in word:
    if character in vowels:
        dots.append("*")
    else:
        dots.append(" ")

def print_current():
    for item in display:
        print(item, end=" ")
    print()
def print_vowel_position():
    for item in dots:
        print(item, end=" ")
    print()

print_current()
print_vowel_position()
printer(0)

while True:
    ctr_replace=0
    ctr_attempt+=1

    guess=input(f"Guess {ctr_attempt}: ")
    
    if word.find(guess)<0:
        wrong.append(guess)
        ctr_end+=1
    else:
        for character in word:
            if guess == character:
                display[ctr_replace]=guess.upper()
            ctr_replace+=1
    
    print_current()
    
    if not "_" in display:
        print("Congratulations! You guessed the word!")
        break
    else:
        print_vowel_position()

    print("Wrong Letters: ", end="")
    for letter in wrong:
        print(letter.upper(), end=" ")
    print()
    printer(ctr_end)
    print()

    if ctr_end==6:
        print("You LOSE!")
        print(f"The word was {word.upper()}")
        break
