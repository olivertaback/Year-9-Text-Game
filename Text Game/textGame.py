import random
import time
import termcolor
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint 
from pyfiglet import figlet_format

def printMsg(string):
    
        for i in string:
        
                print(i, end='')
                sys.stdout.flush()
                time.sleep(0.05)

text = ""
def coloring(text):
    printMsg(termcolor.colored(text, 'blue', attrs = ['bold']))
    print("\n")

def listColor(text):
        printMsg(termcolor.colored(text, 'green', attrs = ['bold']))
        print("\n")
animal = ""
score = 0
def playing():
        global score
        actInput = input()
        if "outside" in actInput.lower():
                text = animal + " is happy playing outside!"
                coloring(text)
                score += 1
        elif "feeding" in actInput.lower():
                text = animal + " loves his yummy food!"
                coloring(text)
                score += 3
        elif "hugging" in actInput.lower():
                text = animal + " loves your hugs!"
                coloring(text)
                score += 2
        elif "inside" in actInput.lower():
                text = animal + " is happy playing outside!"
                coloring(text)
                score += 2
        elif "toys" in actInput.lower():
                text = "You're having lots of fun playing with toys!"
                coloring(text)
                score -= 1
        elif "family" in actInput.lower():
                text = animal + " is happy playing with your whole family!"
                coloring(text)
                score += 3
        elif "bathe" in actInput.lower():
                text = animal + " is popping all the bubbles in the bath!"
                coloring(text)
                score += 3
        else:
                text = "I don't understand that word, please re-enter the word."
                coloring(text)
                playing()


cprint(figlet_format('NO HELP WANTED', font='starwars'),
       'blue', 'on_white', attrs=['bold'])

cprint(figlet_format('by oliver taback', font='starwars'),
       'blue', 'on_white', attrs=['bold'])

coloring("Hello! Welcome to my game. I hope you have fun!")
# User Animal Input
coloring("Please select the animal you would like to play with. The animals are Gerry the Gerbil, Larry the Lizard, and Terry the Turtle.")
animal = input()
trueStatement = True
while trueStatement == True:
        if "gerry" in animal.lower():
                text = "You have selected Gerry the Gerbil."
                coloring(text)
                animal = "Gerry"
                trueStatement = False
        elif "larry" in animal.lower():
                text = "You have selected Larry the Lizard."
                coloring(text)
                animal = "Larry"
                trueStatement = False
        elif "terry" in animal.lower():
                text = "You have selected Terry the Turtle."
                coloring(text)
                animal = "Terry"
                trueStatement = False
        else:
                text = "I don't recognize that animal. Please try again."
                coloring(text)
                animal = input() 

acts = ["Playing OUTSIDE with " + animal, "FEEDING " + animal, "HUGGING " + animal, "Playing INSIDE with " + animal, "Play on your own with TOYS", "Play with FAMILY and " + animal, "BATHE " + animal + " with family",]
day = 1
loopIndex = 1
while day <= 7:
        time.sleep(1.00)
        text = cprint(figlet_format("It's day " +  str(day), font='starwars'),
       'blue', 'on_white', attrs=['bold'])
        text = "" + animal + " is very excited to see you."
        coloring(text)
        text = "Let's play!"
        coloring(text)
        choice = random.sample(acts, 3)
        text = ("The activities are:")
        coloring(text)
        for x in range(len(choice)):
                listColor(choice[x])
        text = "Please select an activity (please use the CAPITALIZED words to select the actvity)!"
        coloring(text)
        playing()
        day += 1
text = (animal + " had a lot of fun playing with you during the week." + animal + " had a happiness score of " + str(score) + " which is an amazing. The max happiness score is 21.")
coloring(text)