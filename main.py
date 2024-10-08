import random

def create_matrix(rows,columns):
    matrix=[]
    ships = []
    
    while len(ships) < 5:
        position = random.randint(0, rows * columns - 1)
        
        if ships.count(position) == 0:
            ships.append(position)
                
    count = 0     
                
    for i in range(rows):
        rows=[]
        for j in range(columns):
            if count in ships:
                rows.append(1)
            else:
                rows.append(0)
                
            count += 1
        matrix.append(rows)
    
        
    return matrix

def display_rows(board, show_ships):
    # Then we can iterate through the board's matrix. Since we print by row, we add append all the elements by row in a list, and print the row.
    # Depending on the value on the board, we display a different element on the board.
    for row_number, row in enumerate(board):
        print_row = [str(row_number + 1)]
        
        for column_number, element in enumerate(row):  
            if show_ships:
                if element == 1 or element == 3:
                    print_row.append("s")    
                else:
                    print_row.append(".")

            else:         
                if element == 0 or element == 1 and not show_ships:
                    print_row.append(".")
                elif element == 2:
                    print_row.append("x")
                elif element == 3:
                    print_row.append("o")    
                            
        print(" | ".join(print_row))


def display_board(board, show_ships = False):
    # The first row is the leyend for the column number
    spacing_string = " " * 3
    leyend_row = ["#"]
    
    
    # We can get it by iterating on the number of columns and appending the number in the leyend_row 
    for column_number, column in enumerate(board[0]):
        leyend_row.append(str(column_number + 1))
        
        
    # And the printing it on the console with a spacing of three spaces
    print(spacing_string.join(leyend_row))    
    
    display_rows(board, show_ships)


def main():
    turn = 0
    board = create_matrix(8,8)
    print(board)
    attempts = []
    

    while  turn < 10:
        print(f"TURN {turn + 1}", "\n")
        display_board(board)
        
        attempt_row = int(input("Next row to shoot? (1 - 8) "))
        attempt_column = int(input("Next column to shoot? (1 - 8) "))
        
        if [attempt_row, attempt_column] in attempts:
            print("You already shot there")
            continue

        if board[attempt_row - 1][attempt_column - 1] == 0:
            print("You missed!")
            board[attempt_row - 1][attempt_column - 1] = 2

        
        if board[attempt_row - 1][attempt_column - 1] == 1:
            print("You hit a ship!")
            board[attempt_row - 1][attempt_column - 1] = 3   
        
        attempts.append([attempt_row, attempt_column])
        
        
        turn += 1
        
    # Display board showing where are the ships   
    display_board(board, True)   

main()