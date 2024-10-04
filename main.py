import random

def create_matrix(rows,columns):
    matrix=[]
    ships = []
    
    while len(ships) < 5:
        position = random.randint(0, rows * columns - 1)
        
        if ships.count(position) == 0:
            ships.append(position)
            
    print(ships)
    
    count = 0     
                
    for i in range(rows):
        rows=[]
        for j in range(columns):
            if ships.count(count) == 1:
                rows.append(1)
            else:
                rows.append(0)
                
            count += 1
        matrix.append(rows)
    
    
    print(matrix)
    
    return matrix

def test_matrix(matrix):
    counter = 0
    
    for rows in matrix:
        
        for element in rows:
            if element == 1:
                counter += 1
                
    print(counter)


test_matrix(create_matrix(8,8))