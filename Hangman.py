# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 22:05:55 2025

@author: ahmed amr ahmed khalil
"""
import random
#step1
words = [
    "apple", "camel", "cherry", "banana", "grape", "peach", "orange", "lemon", "mango", "papaya",
    "zebra", "giraffe", "lion", "tiger", "panda", "koala", "monkey", "rabbit", "otter", "rhino",
    "chair", "table", "pillow", "blanket", "mirror", "window", "curtain", "sofa", "candle", "lamp",
    "cloud", "storm", "wind", "rain", "snow", "fog", "sunny", "breeze", "thunder", "lightning",
    "train", "plane", "boat", "truck", "car", "bus", "bicycle", "scooter", "subway", "rocket",
    "doctor", "nurse", "teacher", "student", "lawyer", "chef", "baker", "painter", "farmer", "police",
    "happy", "sad", "angry", "brave", "scared", "funny", "quiet", "loud", "kind", "silly",
    "write", "read", "build", "draw", "run", "jump", "swim", "drive", "sleep", "cook",
    "planet", "comet", "star", "galaxy", "nebula", "earth", "moon", "venus", "mars", "jupiter",
    "sugar", "flour", "butter", "salt", "bread", "cheese", "pasta", "pizza", "salad", "cookie",
    "house", "garden", "fence", "garage", "rooftop", "porch", "door", "floor", "stairs", "attic"
]

#choose a random word
chosen_word = random.choice(words)
#create placeholder with number of strings
display =["_"]*len(chosen_word)

dash=""
for i in range(0,len(chosen_word)):
    dash = dash + "_ "

game_over=False
lives = 6

hangman_stages = [
    """ 
     +---+
     |   |
         |
         |
         |
         |
    =======""",
    """ 
     +---+
     |   |
     O   |
         |
         |
         |
    =======""",
    """ 
     +---+
     |   |
     O   |
     |   |
         |
         |
    =======""",
    """ 
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======""",
    """ 
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =======""",
    """ 
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =======""",
    """ 
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ======="""
]
index = 0


print("word to guess: ",dash)
while(not game_over):
    #prompt a letter from user

    #any upper_case must be turned to lower_case
    guessed_letter = input("Enter a letter: ").lower() #this function makes capital small
    flag= False
    #check if letter is in chosen word           
    for i in range (0,len(chosen_word)):
        if(guessed_letter == chosen_word[i]):
            display[i] = guessed_letter
            flag = True
            
    if(flag == False):
        lives -=1
        index +=1
        print("you lost a life")
        print(f"you have {lives} lives left")
        
    if("_" not in display or lives == 0):
        game_over = True
        print(hangman_stages[index])
        
    if(lives != 0):
        print("The word: ","".join(display))  
        print(hangman_stages[index])
    print("####################################################################")    

if(lives <= 0):
    print("You got hanged")
else:
    print("Congratulations! You won")
