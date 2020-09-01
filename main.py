import pyraminx as Pyraminx
import sys

pyraminx = Pyraminx.pyraminx()

programActive = True

print("Welcome, Pyraminx program initialized")
print("Standard input notation accepts the following inputs:")
print ("U       L       R       B")
print ("U'      L'      R'      B'")
print ("u       l       r       b")
print ("u'      l'      r'      b'")
print("the larger commands may also be $w for wide")
print(" for example, Uw is U wide, Uw' is U' wide")

while(programActive):
    pyraminx.display_faces()
    
    print("1. randomize pyraminx")
    print("2. exit")
    print("3. reset")
    print("The program is now listening for standard notation input")
    
    userInput: str = input()

    if userInput == "3":
        
        newPyraminx = Pyraminx.pyraminx()

        del(pyraminx)
        pyraminx = newPyraminx
        del(newPyraminx)
    if userInput == "2":
        exit()
    if userInput == "1":
        pyraminx.randomize()
    else:
        pyraminx.match_input(userInput)
    