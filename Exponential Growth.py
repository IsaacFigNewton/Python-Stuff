import math
x = 1
while (x**2)<=10000:
    if x>=2:
        print (round(x**2))
        x = x + 0.001
    else:
        print (x**2)
        x = x + 0.001
    
input("""This is just an example of the power of... something,
try and guess what the function looks like!""")
