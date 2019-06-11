import math
import random

#vars = number of variables tweaked through machine learning
vars = 7
step = -(10**(-vars))
iteration = 0
inp1 = random.randint(0,100)
inp2 = random.randint(0,100)

#n1 and n2 stand for node 1 and node 2, they are functions.
#This is where stuff gets cool and complicated, I'm treating n1 and n2 as separate nodes, independent of eachother.
def n1(inp1,inp2,w1,w2,w3,w4):
    n=(inp1*w1)+(inp2*w4)
    return n*2

def n2(inp1,inp2,w1,w2,w3,w4):
    n=(inp2*w2)+(inp1*w3)
    return n*10
    
#Dependent variables and functions   
#Weights 1-4 are responsible for the first half of the NN
w1 = float(random.randint(0,100)/100)
w2 = float(random.randint(0,100)/100)
w3 = float(random.randint(0,100)/100)
w4 = float(random.randint(0,100)/100)
#Weights 5-6 & b are responsible for the last half.
w5 = float(random.randint(0,100)/100)
w6 = float(random.randint(0,100)/100)
b = 0

i = input("How many iterations would you like to run?")
i = int(i)

def sigmoid(x):
    return 1/(1 + math.exp(-x))

#This is the part where I got stuck for so long, because I was confused as to how to find the partial derivatives for each parameter.
#The partial derivatives for the cost with respect to each parameter

def pdw1(out, proutput):
    return (2*(out - proutput)*inp1)

def pdw2(out, proutput):
    return (2*(out - proutput)*inp2)

def pdw3(out, proutput):
    return (2*(out - proutput)*inp1)

def pdw4(out, proutput):
    return (2*(out - proutput)*inp2)

def pdw5(out, proutput,inp1,inp2,w1,w2,w3,w4):
    return (2*(out - proutput)*n1(inp1,inp2,w1,w2,w3,w4))

def pdw6(out, proutput,inp1,inp2,w1,w2,w3,w4):
    return (2*(out - proutput)*n2(inp1,inp2,w1,w2,w3,w4))

def pdb(out, proutput):
    return (2*(out - proutput)*1)

n = 0
while(n < i):
    n = n+1
    iteration = iteration+1
    inp1 = random.randint(0,100)
    inp2 = random.randint(0,100)

    
    #This is the target equation, where the goal is set...
    proutput = ((inp1)+(inp2))/2 +100
    
    out = n1(inp1,inp2,w1,w2,w3,w4)*w5 + n2(inp1,inp2,w1,w2,w3,w4) * w6 + b
    error = proutput-out
    w1 = w1 + step*pdw1(out, proutput)
    w2 = w2 + step*pdw2(out, proutput)
    w3 = w3 + step*pdw3(out, proutput)
    w4 = w4 + step*pdw4(out, proutput)
    w5 = w5 + step*pdw5(out, proutput, inp1,inp2,w1,w2,w3,w4)
    w6 = w6 + step*pdw6(out, proutput, inp1,inp2,w1,w2,w3,w4)
    #Enter ~10x or ~100x the target bias for the best result, since the larger the #, the larger the step.
    b = b + 1000000*step*pdb(out, proutput)
    #Updating the output given its distance from the goal
    
    #Enter code
    print("Iteration Number: ", iteration)
    print("Input 1: ", inp1)
    print("Input 2: ", inp2)
    print("Weight 1: ", w1)
    print("Weight 2: ", w2)
    print("Weight 3: ", w3)
    print("Weight 4: ", w4)
    print("Hidden Node 1: ", n1(inp1,inp2,w1,w2,w3,w4))
    print("Hidden Node 1: ", n1(inp1,inp2,w1,w2,w3,w4))
    print("Weight 5: ", w5)
    print("Weight 6: ", w6)
    print("Bias: ", b)
    print("Projected Output: ", proutput)
    print("Actual Output: ", out)
    print("Difference: ", error)
    print(" ")
    print(" ")

input("Press Enter to end the program.")
