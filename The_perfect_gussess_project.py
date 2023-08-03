#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
randomNumber = random.randint(1,100)
userGuess = None
guesses = 0

while (userGuess != randomNumber):
    userGuess = int(input("Enter your Number: "))
    guesses += 1
    if (userGuess == randomNumber):
        print("you guessed the right Number")
    else:
        if(userGuess > randomNumber):
            print("you guessed the wrong number ! please guess the smaller number")
        else:
            print("you guessed the wrong number ! please guess the greater number")
print(f"you guessed the number in {guesses} guesses")

with open("highscore.txt","r") as f:
    highscore = int(f.read())
    
if(guesses<highscore):
    print("you have broken the record!")
    with open("highscore.txt","w") as f:
        f.write(str(guesses))


# In[ ]:




