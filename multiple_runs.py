import pyraminx as Pyraminx
import Tree
import solver
import gc
import time

for depth in range(3, 20):
    #clear memory
    gc.collect()

    for particular_run in range(5):
        
        filename = str(depth) + "_Depth_particular_run_number_" + str(particular_run) + ".txt"
        gc.collect()
        
        pyraminx = Pyraminx.pyraminx()
        pyraminx.auto_randomize(depth)

        node_to_solve = Tree.node(pyraminx, 0)
        start_time = time.time()
        Solver = solver.solver(node_to_solve)

        f = open(filename, "w")
        stringToWrite = ""

        f.write("number of nodes expanded: " + str(Solver.bigCount) + "\n")
        f.write("number of moves: " + str(len(Solver.path)-2)+"\n") 

        for i in reversed(Solver.path):
            f.write(i + "\n")
        f.close()
        elapsed = time.time() - start_time
        print("Depth: " + str(depth) + ", " + "Run: " + str(particular_run) + ", " + str(elapsed) + "\n")
        






