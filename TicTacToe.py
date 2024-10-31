def print_board(board):
    for row in board:
        print("-" * 10)
        print(" | ".join(row))
    print("-" * 10)

def check_winner(board):
    for row in board:       #Check each row for win condition
        if(all(x == row[0] and x != " " for x in row)):
            return True
        
    col_list = []           #Check each column for win condition
    for col in range(len(board[0])): 
        for row in board:
            col_list.append(row[col])
        if(all(x == col_list[0] and x != " " for x in col_list)):
            return True
        else:
            col_list.clear()

    if(board[0][0] == board[1][1] == board[2][2] != " "):   #Check both diagonals for win condition
        return True
    elif(board[0][2] == board[1][1] == board[2][0] != " "):
        return True
        
    return False

def tic_tac_toe():
    row_coord_dict = {
        't' : 0,    #Top
        'm' : 1,    #Middle
        'b' : 2}    #Bottom
    
    col_coord_dict = {
        'l' : 0,    #Left
        'm' : 1,    #Middle
        'r' : 2}    #Right
    board = [[" " for i in range(3)] for j in range(3)]
    current_player = "X"

    while(True):
        print_board(board)

        print(f"Player {current_player}, enter your desired row. Use T/t for top, M/m for middle, B/b for bottom")
        row = input().casefold()            #Convert input to lowercase
        while(row not in ['t', 'm', 'b']):
            row = input("That selection was invalid, please pick another one.")
        row = row_coord_dict[row]
        
        print(f"Player {current_player}, enter your desired column. Use L/l for left, M/m for middle, R/r for right.")
        col = input().casefold()            #Convert input to lowercase
        while(col not in ['l', 'm', 'r']):
            col = input("That selection was invalid, please pick another one.")
        col = col_coord_dict[col]

        if(board[row][col] == " "):
            board[row][col] = current_player
        else:
            print("That spot is already taken, please choose another one.")
            continue

        if(check_winner(board)):
            print_board(board)
            print(f"Player {current_player} is the winner!")
            print("Press enter to close the program.")
            input()
            break
        if all(board[row][col] != " " for row in range(3) for col in range (3)):
            print_board(board)
            print("The game ends in a tie!")
            print("Press enter to close the program.")
            input()
            break

        if(current_player == "X"):
            current_player = "O"
        elif(current_player == "O"):
            current_player = "X"

if __name__ == "__main__":
    tic_tac_toe()
    