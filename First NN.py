import math
import random

inp1 = random.randint(0,100)
inp2 = random.randint(0,100)
w1 = float(random.randint(0,100)/100)
w2 = float(random.randint(0,100)/100)

#-4 is optimal, the lower, the more accurate after a longer time.
step = -(10**-4)

i = input("How many iterations would you like to run?")
i = int(i)

#def sigmoid(x):
#    return 1/(1 + math.exp(-x))

#def NN(inp1, inp2, w1, w2, b):

def Cost(proutput, out):
    error = proutput-out
    cost = (error)**2
    return cost

def num_slope(x, proutput):
    h = 0.0000000000000000001
    #The classic formula for finding the derivative of a number. ((f(x+h)-f(x))/h)
    #In this case, that number(x) is the output, and the other number is the projected output
    return (Cost(proutput, x+h)-Cost(proutput, x))/h

#This is the part where I got stuck for so long, because I was confused as to how to find the partial derivatives for each parameter.
#The partial derivatives for the cost with respect to each parameter

def pdw1(inp1, inp2, w1, w2, proutput):
    #fix this using the chain rule
    return (2*(out - proutput)*inp1)

def pdw2(inp1, inp2, w1, w2, proutput):
    #fix this using the chain rule
    return (2*(out - proutput)*inp2)

def pdb(inp1, inp2, w1, w2, proutput):
    #fix this using the chain rule
    return (2*(out - proutput)*1)

n = 0
while(n <= i):
    n = n+1
    inp1 = random.randint(0,100)
    inp2 = random.randint(0,100)
    proutput = (inp1+inp2)/2
    #The NN will get the answers correct once w1 & w2 are both 0.5
    out = inp1*w1 + inp2*w2# + b
    error = proutput-out
    w1 = w1 + step*pdw1(inp1, inp2, w1, w2, proutput)
    w2 = w2 + step*pdw2(inp1, inp2, w1, w2, proutput)
    #Updating the output given its distance from the goal
    
    #Enter code
    print("Input 1: ", inp1)
    print("Input 2: ", inp2)
    print("Weight 1: ", w1)
    print("Weight 2: ", w2)
    print("Bias: None")
    print("Projected Output: ", proutput)
    print("Actual Output: ", out)
    print("Difference: ", error)
    print(" ")
    print(" ")


#1 new attempt for every increase in version by 0.01 increment
#Version 1.36
