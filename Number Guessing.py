import random
secret = random.randint(1,99)
guess = 0
tries = 5
print ("AHOY! I be the dread Pirate Blackbeard, no, not what ye be thinkin', I ain't the famed pirate Black Beard, I be the lesser-known one.")
print ("I have a secret number, if ye guess it correct by the 6th try, ye scurvy dog shall live, but if not, ye shall walk the plank!")
while guess != secret and tries >= 0:
    guess = int(input("What'll it be?"))
    if (guess-secret)>50:
        print ("Yarr! Ye aren't close in the slightest!")
    elif (guess-secret)>30:
        print ("Ye be far off!")
    elif (guess-secret)>10:
        print ("Avast, ye've almost guessed my secret!")
    elif (guess-secret)>0:
        print ("Arr, ye is closer than me first mate!")
    elif (guess-secret)<-50:
        print ("Yarr! Ye aren't close in the slightest!")
    elif (guess-secret)<-30:
        print ("Ye be far too low ye scurvy dog!")
    elif (guess-secret)<-10:
        print ("Yar get on up here!")
    elif (guess-secret)<0:
        print ("Arr, ye is closer than me negative first mate!")

        
    tries = tries - 1

    if guess == secret and tries >= -1:
        print ("Avast! Ye shall live to suck another day!")
    elif tries == -1 and guess != secret:
        print ("Sorry mate, ye shall walk the plank!")
        print ("Before you die, though, you should know the answer, it was ",secret," ye dumbass")
        
