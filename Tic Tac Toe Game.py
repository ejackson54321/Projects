#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    row1 = ''
    row2 = ''
    row3 = ''
    for n in board[1:4]:
        row1 = row1 + f'{n} | '
    for n in board[4:7]:
        row2 = row2 + f'{n} | '
    for n in board[7:10]:
        row3 = row3 + f'{n} | '
    print(row3)
    print("----------")
    print(row2)
    print("----------")
    print(row1)
     
        
    


# In[2]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[23]:


def player_input():
    
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    
    choice = ' '
    
    while choice != 'X' and choice != 'O':
        choice = input("Please choose X or O: ").upper()
        if choice == 'X':
        
            return ('X','O')
        else:
            return('O','X')
       
   


# In[24]:


player_input()


# In[26]:


player1_marker , player2_marker = player_input()


# In[27]:


player1_marker


# In[28]:


player2_marker


# In[5]:


def place_maker(board, marker, position):
    board[position] = marker
    return board


# In[6]:


place_maker(test_board,'$',8)
display_board(test_board)


# In[7]:


test_board


# In[8]:


diagonal1 = test_board[1] = test_board[2] == test_board[3]


# In[9]:


diagonal1


# In[10]:


def win_check(board, mark):
    row_check1 = board[1] == board[2] == board[3] == mark
    row_check2 = board[4] == board[5] == board[6] == mark
    row_check3 = board[7] == board[8] == board[9] == mark
    column_check1 = board[1] == board[4] == board[7] == mark
    column_check2 = board[2] == board[5] == board[8] == mark
    column_check3 = board[3] == board[6] == board[9] == mark
    diagonal_check1 = board[1] == board[5] == board[9] == mark
    diagonal_check2 = board[3] == board[5] == board[7] == mark
    if row_check1 or row_check2 or row_check3 or column_check1 or column_check2 or column_check3 or diagonal_check1 or diagonal_check2:
        return True
    return False


# In[11]:


win_check(test_board,'X')


# In[12]:


win_check(test_board,'O')


# In[13]:


import random

def choose_first():
    who_first = random.randint(1,2)
    if who_first == 1:
        print('Player X will go first')
        return f'Player X will go first'
    else:
        print('Player O will go first')
        return f'Player O will go first'


# In[14]:


choose_first()


# In[30]:


def space_check(board,position):
    return board[position] == ' '


# In[31]:


space_check(test_board,8)


# In[34]:


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[35]:


full_board_check(test_board)


# In[44]:


def player_choice(board):
    choice = 0
    while choice not in [1,2,3,4,5,6,7,8,9] or space_check(board,choice) == False:
        choice = int(input("Please enter a number between 1-9: "))
    return int(choice)


# In[46]:


def replay():
    choice = input("Do you want to play again? (Y/N)")
    
    return choice == 'Y'


# In[51]:


print('Welcome to Tic Tac Toe!')

game = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
p1 = player_input()
c = choose_first()
x = 1
if c == 'Player O will go first':
        x += 1
while full_board_check(game) == False:
    if win_check(game,'X') == True:
        print("IT'S OVER! Player X wins!!")
        break
    elif win_check(game,'O') == True:
        print("IT'S OVER! Player O wins!!")
        break
    else:
        n = player_choice(game)
        if x == 1:
            place_maker(game, 'X',n)
            display_board(game)
            x += 1
        elif x == 2:
            place_maker(game,'O',n)
            display_board(game)
            x -= 1
        
replay()


# In[53]:


# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to Tic Tac TOE (Instructor Version)')

while True:
    
    # PLAY THE GAME
    
    ## SET EVERYTHING UP (BOARD, WHOS FIRST, CHOOSE MARKERS X,O)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to play? y or n')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
        
    ## GAME PLAY
    
    while game_on:
        if turn == 'Player 1':
            
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_maker(the_board,player1_marker,position)
            
            # Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'Player 2'
            # Or check if there is a tie
            
            # No tie and no win? Then next player's turn
    
        else:
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_maker(the_board,player2_marker,position)
            # Check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'Player 1'
    
    
    
    
    
    if not replay():
        break
    # BREAK OUT OF THE WHILE LOOP ON replay()


# In[48]:


mylist = [' ']*5


# In[49]:


mylist


# In[ ]:




