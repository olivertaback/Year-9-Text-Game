import sys
import time
from colorama import init
init(strip=not sys.stdout.isatty())
import termcolor
#def printMsg(string):
 #   
  #      for i in string:
        
        # printing each character of the message
   #             sys.stdout.write(i)
          
        # adding time delay of half second
    #            time.sleep(1.00)
#printMsg("Hello")
#for char in "hello, world.":
#    print(char, end='')
   # sys.stdout.flush()
   # time.sleep(0.1)
text = ""
def coloring(text):
    print(termcolor.colored(text, 'blue', attrs = ['bold']))
    print("\n")
l = ["1", "2", "3", "4"]
for x in range(len(l)):
    coloring(l[x])
