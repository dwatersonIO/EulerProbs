'''
Make 10x10 grid of to contain single letter each square
From a list containing 10 words display those words in grid
    Use randon x, y starting point
    Use random N, S, E, W, NE, NW, SW, SE direction for word
Fill in the empty squares with random letter

TO DO
Get random starting x y
Get random vectors
Fill from list
Fill up empty spaces
Instead of list import words from txt file

'''
import random
import time


word_grid = {}
for row in range(10):
    for col in range(10):
        word_grid[(row,col)] = "-"


ACTUAL_GRID_SIZE=10
GRID_SIZE=ACTUAL_GRID_SIZE-1 #  grid in list so starts from 0 not 1

'''
To check if Word will fit inside the grid boundaries
'''
def fits_grid(word,start_row,start_col,vect_row,vect_col):
    ending_row = start_row + ((len(word)-1) * vect_row)  # Chk on which row will word end
    ending_col = start_col + ((len(word)-1) * vect_col)  # Chk on which col will word end
    
    if (ending_row > GRID_SIZE) or (ending_row < 0 ) or (ending_col > GRID_SIZE) or (ending_col) < 0:
        return False
    else:
        return True

'''
To check if each letter of word will go in empty space or else 
if not it contains the correct letter already. If not will return False
'''
def blank_or_same(word,row,col,vect_row,vect_col):
    result = True
    for letter in range(len(word)):
        if word_grid[(row,col)] == (word[letter]) or (word_grid[(row,col)] == "-"):
            row = row + vect_row
            col = col + vect_col  
        else:
            result = False
            return result            
    return result

'''
This will write the word to the list
'''
def write_word(word,row,col,vect_row,vect_col):   
    for letter in range(len(word)):
        word_grid[(row,col)]=word[letter]
        row = row + vect_row
        col = col + vect_col  

'''
Generate the random numbers for starting position and 
also the vectors to determine direction word will go in
'''
def return_start_and_vectors():
    vector_list =[-1,0,1]
    start_row = random.randint(0,GRID_SIZE) 
    start_col = random.randint(0,GRID_SIZE)
    while 1 == True:
        vect_row = random.choice(vector_list)
        vect_col = random.choice(vector_list)
        if vect_row == 0 and vect_col == 0: # Vector cannot be 0, 0 otherwise will overwrite letters
            continue
        elif vect_row == 0 and vect_col == 1: # Dont allow words to be formed left to right
            continue
        else:
            return start_row, start_col, vect_row, vect_col

def place_word(word):
    loop_me=1
    while loop_me < 10000000:
        start_row, start_col, vect_row, vect_col=return_start_and_vectors()
        if fits_grid(word,start_row, start_col, vect_row, vect_col):
            if blank_or_same(word,start_row, start_col, vect_row, vect_col):
                print (start_row, start_col, vect_row, vect_col)
                write_word(word,start_row, start_col, vect_row, vect_col)
                print (word, loop_me)
                break
            else:
                loop_me += 1
                continue
        else:
            loop_me += 1
            continue

'''
Fill in unused squares with random letters
'''
def fill_unused():
    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for row in range(ACTUAL_GRID_SIZE):
        for col in range(ACTUAL_GRID_SIZE):
            filler=random.choice(letters)
            if word_grid[(row,col)] == "-":
                word_grid[(row,col)] = "-" # add filler when ready to use

'''
Print the grid to screen
'''
def print_grid():
    counter=0
    for key in sorted(word_grid):
        print(word_grid[key], end=" ")
        counter += 1
        if counter % (ACTUAL_GRID_SIZE) == 0:
            print()            
          

begin = time.time()
words=["LEVITE","LOYALTY","ANIMALS","UNCLEAN","NADAB","ABIHU", "AARON","CAMP","MOSES"]       
for word in words:
    place_word(word)

fill_unused()
print_grid()
print()

end = time.time()
print ("Time taken: ", end-begin)

