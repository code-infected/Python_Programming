

#1.Draw a Game board

# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).Ask the user what size game board they want to draw, anddraw it for them to the screen using Python’sprintstatement.Hint: use functions.



def horizontal_line ( size ):
    return " ---" * size + " \n"

def vertical_lines ( size ):
    return "|   " * size + "|\n"

def gameboard ( size ):
    board = """"""
    for i in range(size):
        board += horizontal_line(size)
        board += vertical_lines(size)
    board += horizontal_line(size)
    return board

if __name__ == "__main__":
    size = int(input("What size game board do You want? "))
    print(gameboard(size))