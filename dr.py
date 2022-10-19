import pyttsx3

from playsound import playsound
from random import randint
from time import sleep

if __name__ == "__main__":

    # Title print
    print(" A SIMPLE DICE ROLLER ".center(75, '='))

    # Initializing objects
    engine = pyttsx3.init()
    counter = {k: 0 for k in range(2, 13)}
    turn = 0

    # Inputting names
    names = [x.lstrip().title() for x in input("Type names (separated by commas): ").split(",")]
    spoken_names = [x.upper() for x in names]

    # Turn length
    try:
        length = max(int(input("How many seconds between each roll? (default 5): ")), 5) - 5
    except ValueError:
        length = 0

    # Final prints
    print("Names are:", ", ".join(names))
    print("Roll interval is:", length + 5)
    input("ENTER when ready!")

    # Main game loop
    try:
        while True:

            # Rolling and audio
            # playsound("zelda.mp3")
            roll = randint(1, 6) + randint(1, 6)
            counter[roll] += 1

            phrase = names[turn] + "'s dice roll is " + str(roll)
            spoken_phrase = spoken_names[turn] + "s dice roll is " + str(roll)
            turn = (turn + 1) % len(names)

            print(phrase)
            engine.say(spoken_phrase)
            engine.runAndWait()

            # Waiting interval between rolls
            try:
                print("========================")
                sleep(length)
                for j in range(5, 0, -1):
                    print(j)
                    sleep(1)

            # Ctrl + C interrupt to skip to next roll
            except KeyboardInterrupt:
                print('\b\b\r')
                continue

    # Ctrl + C interrupt to end game
    except KeyboardInterrupt:
        print('\b\b\r')
        print("Game over!")
        print("Dice roll frequencies (if you're into that):")
        for i in range(2, 13):
            print(" " + str(i) if i < 10 else i, "".join(["|"] * counter[i]))
