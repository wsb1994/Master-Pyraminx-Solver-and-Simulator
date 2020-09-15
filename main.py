import pyraminx as Pyraminx
import sys
import Tree
import solver
import copy
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
    print("4. to attempt to solve")
    print("The program is now listening for standard notation input")
    
    userInput: str = input()

    if userInput == "4":

        node = Tree.node(copy.deepcopy(pyraminx), 0)
        Solver = solver.solver(node)
        for i in Solver.path:
            print(i)

    if userInput == "3":
        
        newPyraminx = Pyraminx.pyraminx()

        del(pyraminx)
        pyraminx = newPyraminx
        del(newPyraminx)
        
    if userInput == "2":
        exit(0)
    if userInput == "1":
        pyraminx.randomize()
    else:
        pyraminx.match_input(userInput)
    