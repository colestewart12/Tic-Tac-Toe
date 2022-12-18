board = ["-", "-", "-"], ["-", "-","-"], ["-", "-", "-"]
p1 = input("Player 1 pick your character: ")
p2 = input("Player 2 pick your character: ")
winGame = False

#Function that displays the game board
def display_board():
  print(board[0][0] + ' | '  + board[0][1] + ' | ' + board[0][2])
  print("----------")
  print(board[1][0] + ' | '  + board[1][1] + ' | ' + board[1][2])
  print("----------")
  print(board[2][0] + ' | '  + board[2][1] + ' | ' + board[2][2])

#Checks if anyone has won due to a horizontal connection
def check_rows():
  for i in range(3):
    tracker = 0
    if board[i][0] == "-":
      continue
    for j in range(1,3):
      if board[i][j] == board[i][0]:
        tracker = tracker + 1
    if tracker == 2:
      global winGame
      winGame = True

#Checks if anyone has won due to a vertical connection
def check_columns():
  for j in range(3):
    tracker = 0
    if board[j][0] == "-":
      continue
    for i in range(1,3):
      if board[j][i] == board[j][0]:
        tracker = tracker + 1
    if tracker == 2:
      global winGame
      winGame = True

#Checks if anyone has won due to a diagonal connection
def check_diagonal1():
  tracker = 0
  if board[0][0] != "-":
    for i in range(1,3):
      if board[i][i] == board[0][0]:
        tracker = tracker + 1
    if tracker == 2:
      global winGame
      winGame = True

#Checks if anyone has won due to a diagonal connection
def check_diagonal2():
  tracker = 0;
  if board[0][0] != "-":
    for i in range(1,3):
      if board[i][2-i] == board[0][0]:
        tracker = tracker + 1
    if tracker == 2:
      global winGame
      winGame = True

#Keeps track of which player's turn it is
ctr = 2

#Display the empty board
display_board()

#While method that loops over each players turn until someone wins
while winGame == False:
  #Updates the board for player 1's turn
  if ctr % 2 == 0:
    print("Player 1's turn")
  else:
    print("Player 2's turn")
  row = input("Choose a row(left-to-right 0-2): ")
  row = int(row)
  column = input("Choose a column(up-to-down 0-2): ")
  column = int(column)
  if ctr % 2 == 0:
    if board[row][column] == '-':
      board[row][column] = p1
    else:
      print("This spot has already been filled")
      row = input("Choose a row(left-to-right 0-2): ")
      row = int(row)
      column = input("Choose a column(up-to-down 0-2): ")
      column = int(column)
      board[row][column] = p1
  else:
    #Updates the board for player 2's turn
    if board[row][column] == '-':
      board[row][column] = p2
    else:
      print("This spot has already been filled")
      row = input("Choose a row(left-to-right 0-2): ")
      row = int(row)
      column = input("Choose a column(up-to-down 0-2): ")
      column = int(column)
      board[row][column] = p2
    
  #Checks the methods to see if there has been a winner
  check_rows()
  check_columns()
  check_diagonal1()
  check_diagonal2()
  ctr = ctr+1
  display_board()
  
  #Checks to look for ties
  if(ctr == 11):
    winGame = True;

#Game Results
if ctr == 11:
  print("It's a Tie!")
elif ctr % 2 == 0:
  print("Player 2 Wins!")
else:
  print("Player 1 Wins!")
