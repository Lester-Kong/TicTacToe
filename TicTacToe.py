def print_board(board):
    for row in board:
        print("-" * 10)
        print(" | ".join(row))
    print("-" * 10)

def tic_tac_toe():
    col_coord_dict = {
        'L' : [0],    #Left
        'l' : [0],
        'M' : [1],    #Middle
        'm' : [1],
        'R' : [2],    #Right
        'r' : [2]}
    row_coord_dict = {
        'T' : [0],    #Top
        't' : [0],
        'M' : [1],    #Middle
        'm' : [1],
        'B' : [2],    #Bottom
        'b' : [2]}
    board = [[" " for i in range(3)] for j in range(3)]
    current_player = "X"

    while(True):
        print_board(board)
        print(f"Player {current_player}, enter your desired row. Use L/l for left, M/m for middle, R/r for right.")

        while(input() not in ['L', 'l', 'M', 'm', 'R', 'r']):
            print("That selection was invalid, please pick another one.")
        
        print(f"Player {current_player}, enter your desired column. Use T/t for top, M/m for middle, B/b for bottom.")
        while(input() not in ['T', 't', 'M', 'm', 'B', 'b']):
            print("That selection was invalid, please pick another one.")

if __name__ == "__main__":
    tic_tac_toe()
    #testing