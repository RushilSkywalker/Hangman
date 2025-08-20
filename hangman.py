word="amazing"
ctr_attempt=0
ctr_end=0
guess=""
wrong=[]
display=[]
vowels=['a','e','i','o','u']
dots=[]
man_art={
    0: ("    ┌─────────┐",
        "    │         │",
        "    │",
        "    │",
        "    │",
        "    │",
        "    │",
        "    │",
        "    │",
        "    │",
        "──────────"),

    1: ("    ┌─────────┐",
        "    │         │",
        "    │        ┌─┐",
        "    │        └─┘",
        "    │",
        "    │",
        "    │",
        "    │",
        "    │",
        "    │",
        "──────────"),

    2: ("    ┌─────────┐",
        "    │         │",
        "    │        ┌─┐",
        "    │        └─┘",
        "    │         │ ",
        "    │         │ ",
        "    │",
        "    │",
        "    │",
        "    │",
        "──────────"),

    3: ("    ┌─────────┐"
        "    │         │",
        "    │        ┌─┐",
        "    │        └─┘",
        "    │         │ ",
        "    │         │ ",
        "    │        ┌",
        "    │        │",
        "    │",
        "    │",
        "──────────"),

    4: ("    ┌─────────┐",
        "    │         │",
        "    │        ┌─┐",
        "    │        └─┘",
        "    │         │ ",
        "    │         │ ",
        "    │        ┌─┐",
        "    │        │ │",
        "    │",
        "    │",
        "──────────"),

    5: ("    ┌─────────┐",
        "    │         │",
        "    │        ┌─┐",
        "    │        └─┘",
        "    │      ───│ ",
        "    │         │ ",
        "    │        ┌─┐",
        "    │        │ │",
        "    │",
        "    │",
        "──────────"),

    6: ("    ┌─────────┐",
        "    │         │",
        "    │        ┌─┐",
        "    │        └─┘",
        "    │      ───│───",
        "    │         │ ",
        "    │        ┌─┐",
        "    │        │ │",
        "    │",
        "    │",
        "──────────")
}

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

for item in display:
    print(item, end=" ")
print()

for item in dots:
    print(item, end=" ")
print()    

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
    
    for item in display:
        print(item, end=" ")
    print()
    
    if not "_" in display:
        print("Congratulations! You guessed the word!")
        break
    else:
        for item in dots:
            print(item, end=" ")
        print()

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