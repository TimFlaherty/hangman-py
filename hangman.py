#!/usr/local/bin/python3
import sys
import re
import random

#Declare variables for game start/stop, number of tries, and letters guessed
game = 0
tries = 0
guesses = []

#Define ASCII
longblank = '-----------------------------------------------------------'
hangman0 = ' _________     \n|         |    \n|              \n|              \n|              \n|              \n|              \n'
hangman1 = ' _________     \n|         |    \n|         0    \n|         |    \n|              \n|              \n|              \n'
hangman2 = ' _________     \n|         |    \n|         0    \n|        /|    \n|              \n|              \n|              \n'
hangman3 = ' _________     \n|         |    \n|         0    \n|        /|\\  \n|              \n|              \n|              \n'
hangman4 = ' _________     \n|         |    \n|         0    \n|        /|\\  \n|        /     \n|              \n|              \n'
hangman5 = ' _________     \n|         |    \n|         0    \n|        /|\\  \n|        / \\  \n|              \n|              \n'

#Open dictionary and select random word; declare list of word letters
dictionary = open ( 'dictionary' )
words = dictionary.read().split('\n')
word = random.choice(words)
length = len(word)
wordletters = list(word)

#Create list of blank spaces
wordspaces = ['_'] * length

#Display instructions
print('------------\nHangman v1.0\n------------\nEnter a letter for your guess; guess the word to win.\nType "end" to stop the game at any time.')

#Initialize game loop
while(game != 1) & (tries != 5):
	hangman = ''.join('hangman' + str(tries))
	print(eval(hangman))
	print('Your word: ' + ''.join(wordspaces))
	print('Your guesses: ' + ''.join(guesses))
	print('Enter your guess:')
#Grab user input and assign variable
	letter = input()
#Define cases
	#End game
	if (letter == 'end'):
		game = 1
		print('Your word: ' + word)
		print('----------\nGame Over!\n----------')
	#If word is guessed, player wins
	elif(letter == word):
		print('Your word: ' + word)
		print('--------\nYou Win!\n--------')
		game = 1
	#Input validation
	elif(len(letter) != 1) | (letter in guesses):
		print(longblank + '\n>>> Please enter a single unique letter for your guess. <<<\n' + longblank)	
	#If letter is in word, iterate through letters and replace blanks
	elif(letter in word):
		guesses += letter
		count = 0
		while (count <= (length-1)):
			if(wordletters[count] == letter):
				wordspaces[count] = letter
				count += 1
			else:
				count += 1
		#If all letters are guessed, player wins
		if (wordspaces == wordletters):
			print('Your word: ' + word)
			print('--------\nYou Win!\n--------')
			game = 1
	#Increment tries if wrong
	else:
		guesses += letter
		print(letter,'is not in your word.')
		tries += 1

#Game Over
if (tries == 5):
	print(hangman5)
	print('Your word: ' + word)
	print('----------\nGame Over!\n----------')
