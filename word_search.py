# Author : Clara Watson
# Description : Word Search Generator
# File : word_search.py
# Date : December 7, 2018
import string
import random

# variable create a 20 by 20 grid with underscores by creating a line of 20 underscores and then looping that 20 times
grid = [[ '_' for _ in range(20) ] for _ in range(20)]
# empty list for the words that the user will input
dictionary = []
# list of the possible positions that the word can go in the wordsearch
directions = [ 'up' , 'side', 'diagnol' ]
# instructions of what the program does and what to enter
print('This program will help you generate a word search!\nEnter in 10 words that you would like to have in the word search.\nRemember your words must be no longer than 6 letters .\n')
# count is used to create the list of numbers if I had just used x then it would have started at 0 as opposed to 1
count = 1
for x in range(10):
    number = str(count) + ". "
    # this prompts the number in the list and saves what the user enters into a string
    word = input(number)
    # this takes any spaces off the word that the user enters
    word = word.strip(" ")
    # this if statement to determain if the user entered a word that had to many letters or not enough
    if len(word) > 6:
        # if they entered too many letters they will be prompted to reenter the word
        print('***Your word for #' , count, 'had too many letters, please enter a new word.***')
        # this will replace their first entry
        # this prompts the number in the list and saves what the user enters into a string to
        word = input(number)
        # this takes any spaces off the word that the user enters
        word = word.strip(" ")
    if len(word) < 1:
        # if the user did not enter enough characters then they will be promopted theo enter a better word
        print('***You did not enter a valid word, please enter a new word.***')
        # this will replace their first entry
        # this prompts the number in the list and saves what the user enters into a string to
        word = input(number)
        # this takes any spaces off the word that the user enters
        word = word.strip(" ")
    # this changes all the letters in the word that the user enters to be capital
    word = word.upper()
    # this will add the word that the user entered to the list called dictionary
    dictionary.append(word)
    # this will add one everytime the code loops and go up in order
    count = count + 1
    


def main():
    # this is a for loop that will intirate through for every word in the list dictionary
    for word in dictionary:
        # this uses the length command to determin how long the word is a return an integer
        wordLength = len(word)
        # this uses the random import to choose a random element from the global list directions
        direction = random.choice(directions)
        # if the random element selected from the list is up then then the step will be 0 1 becuase to go up and down you do not change the x axis only the y
        if direction == 'up':
            stepX = 0
            stepY = 1
        # if the random element selected from the list is side then then the step will be 1 0 becuase to go side to side you do not change the y axis only the x
        if direction == 'side':
            stepX = 1
            stepY = 0
        # if the random element selected from the list is diagnol then then the step will be 1 1 becuase both the y and x axis will move over
        if direction == 'diagnol':
            stepX = 1
            stepY = 1          
        
            
        
        # this boolean is flase and will be used to keep out while loop going
        canBePlaced = False
        # this while loop uses a boolean to keep going it will stop when the boolean becomes true
        while canBePlaced is False:
            # these first two lines use teh random import to save a rnadom integer into the varibale
            startingX = random.randint(0,20)
            startingY = random.randint(0,20)
            # theses second lines here use the starting value and add it ot the lenght of the word times the step this way when the code goes through it will konow wlike
            endingXCordOfWord = startingX + wordLength*stepX
            endingYCordOfWord = startingY + wordLength*stepY
            # if the endeing coordinate falls off the grid, then the boolean will stay false and the code will continue to loop
            if endingXCordOfWord  < 0:
                canBePlaced = False
            if endingYCordOfWord  < 0:
                canBePlaced = False
            elif endingXCordOfWord > 19:
                canBePlaced = False
            elif endingYCordOfWord > 19:
                canBePlaced = False
            # if the y and c variables are not off of the grid than it will go to the else statement
            else:
                # this loop iterates through the letters in the word this loop is already inside of two other loop that is looping through the words in the list and checking
                for i in range(wordLength):
                    # this saves the letter that the loop is on into a variable
                    character = word[i]
                    # these two lines will be responsible for placing the letter each time the loop goes through
                    newX = startingX + i*stepX
                    newY = startingY + i*stepY
                    # this if statement checks to see if there is already a letter from a different word in the space that the letter is assigned to
                    # if the space is an underscore than the code knows that it is not running into another word
                    if grid[newX][newY] == '_':
                        # therefore it will assign the character to the spot on the grid
                        grid[newX][newY] = character
                    # if there is another character already in the space then the boolean for the while statement will stay false and it will break and reloop to find a spot avalibale
                    else:
                        canBePlaced = False
                        break
                    # if the last letter in the word loops through without any issue then the boolean will change to true and the while statement will end
                    canBePlaced = True
                    
       
        # this will prompt the user to say yes or no if they would like an answer key included in the output and will save it to a variable
    yesOrNo = input("\nIf you would like an answer key in addition to your wordsearch type 'y' for yes and if not type 'n' for no.")
    # if the user inputs y then the code will print an answer key before it prints the actual wordsearch
    if yesOrNo == 'y':
        # first a title is printed
        print('\n\nAnswer Key')
        # this is a for loop that will loop 20 times for each line of the grid
        for x in range(20):
            # this will print teh underscores along with the placed words and join them together with a space
            print (' '.join(grid[x]))
        # this will skip a few lines so there is a space betweeen the key and the wordsearch
        print('\n\n')
    # this calls the function that inputs the random letters into the rest of the grid
    wordsearch()

		
def wordsearch():
    print('Word Search\n')
    # this is a for loop that will go through 20 times and be resposible for the x coordinate in each pair that will tell the random letter to be go
    for x in range(20):
        # this is a for loop that will go through 20 times and be resposible for the y coordinate in each pair that will tell the random letter to be go
        for y in range(20):
            # this if statement will check to see if there is an underscore in the spot this means that it is not being taken by an already placed word
            if grid[x][y]  == '_':
                # this uses the random input to choose a rnadom upercase letter and place it on the coordinate grid
                grid[x][y] = random.choice(string.ascii_uppercase)
# this is a for satement that will finally prin the grid out
    for x in range(20):
        # this will print teh random letters along with the placed words and join them together with a space
        print (' '.join(grid[x]))
        # this inserts the title word bank to the begining of the list of words so that they will print with a title
    dictionary.insert(0,'\nWord Bank')
    # this joints the words with a bullet point and skips to the next line
    print('\n• '.join(dictionary))

# this starts the fucntion main
if __name__ == '__main__':
    main()









