import random

def create_matrix(rows,columns):
    matrix=[]
    ships = []
    
    # Randomly get ships position, without repeating them
    while len(ships) < 5:
        position = random.randint(0, rows * columns - 1)
        
        if ships.count(position) == 0:
            ships.append(position)
                
    count = 0     

    # Create the matrix, if the inner index is in the ships positions list, then inset a ship            
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
    # Ce can iterate through the board's matrix. Since we print by row, we  append 
    # all the elements by row in a list, and print the row.
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
    
    print("\n")


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
    
    
def get_input(attempts):    
    attempt_row_string = input("Next row to shoot? ")
    attempt_column_string = input("Next column to shoot? ")
    
    # Check if the attempt is a positive integer
    if not (attempt_row_string.isdigit() and attempt_column_string.isdigit()):
        print("\n", "Input isn't valid", "\n")   
        return "error"
        
    attempt_row = int(attempt_row_string)
    attempt_column = int(attempt_column_string)

    # Check if the integer is within range
    if not (1 <= attempt_row <= 8 and 1 <= attempt_column <= 8):
        print("\n", "Shoot out of bounds. Try again", "\n")   
        return "error"
    
    # Check if the attempt is duplicated
    if [attempt_row, attempt_column] in attempts:
        print("\n", "You already shot there", "\n")
        return "error"
    
    return attempt_row, attempt_column


def main():
    # Print instructions
    print("Welcome to the Battleship Game!")
    print("How to play?")
    print("You need to guess where the battleships are in the board")
    print("First choose the row, then the column.")
    print("You have 10 turns to guess where the battleships are.")
    print("If you don't guess where all the battleships are, you lose.")
    print("Have a Good battle and bring the victory home, Good Luck!") 

    
    # Run game until user wants to stop
    while True:
        turn = 0
        board = create_matrix(8,8)
        ships_found = 0
        attempts = []
        
        # Run each game for 10 turns    
        while turn < 10:
            print("\n", f"TURN {turn + 1}", "\n")
            display_board(board)
            next_attempt = get_input(attempts)
            
            # If there is an error, restart turn
            if next_attempt == "error":
                continue
            
            # When there isn't an error, the function returns the position as a tuple
            attempt_row,attempt_column = next_attempt
    
            # If there isn't a ship, change the number in the matrix from 0 to 2
            if board[attempt_row - 1][attempt_column - 1] == 0:
                print("You missed!")
                board[attempt_row - 1][attempt_column - 1] = 2
    
            # If there is a ship, change the number in the matrix from 1 to 3
            if board[attempt_row - 1][attempt_column - 1] == 1:
                print("You hit a ship!")
                board[attempt_row - 1][attempt_column - 1] = 3
                ships_found +=1
            
            attempts.append([attempt_row, attempt_column])
            
            
            turn += 1
            
        # Display board showing where are the ships
        print('\033[1m'+"This were the ships placements"+'\033[1m')
        display_board(board, True)   

        # Tells how they did in the game, with a percentage and if they won
        if ships_found == 5:
            print("Congratulations! You won!")
        elif 1 <= ships_found < 5:
            print(f"Hey you fought well, you found {ships_found} ships, meaning you have an accuracy of {ships_found * 20}%.")
        else:
            print("You lost the battle")

        # Takes an input and this will allow the user to dicide if they want to keep playing
        continue_value = input("Do you want to play again? [Y/n]: ")
        if continue_value.lower() == "y":
            continue
        else:
            print("Thanks for playing the game")
            break
            
main()