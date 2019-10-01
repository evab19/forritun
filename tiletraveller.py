
#grid is a list of the lists of direction available
grid = [
    #each line is it's specific list
    [["e", "s"], ["w", "e"], ["w", "s"]], #this is grid(0)
    [["n", "e", "s"], ["w", "s"], ["n", "s"]], #this is grid(1)
    [["n"], ["n"], ["n"]] #this is grid(2)
]

#this way we can call grid[x][y] to get the directions
#grid[0][0] would return ["e", "s"]

def updateDirection(direction, position):
    """This function takes in the direction the user puts in and updates the current position """
    if (direction == "n"):
        position[1] -= 1
    elif (direction == "s"):
        position[1] += 1
    elif (direction == "w"):
        position[0] -= 1
    elif (direction == "e"):
        position[0] += 1
    return position

position = [0,2]

def current_options(availableDirections):
    """This function returns the directions available at each location """"
    directions = ""
    if availableDirections == ["n"]:
        directions = "(N)orth"
    elif availableDirections == ["n", "e", "s"]:
        directions = "(N)orth or (S)outh or (E)ast"
    elif availableDirections == ["w", "s"]:
        directions = "(W)est or (S)outh"
    elif availableDirections == ["n", "s"]:
        directions = "(N)orth or (S)outh"
    elif availableDirections == ["e", "s"]:
        directions = "(E)ast or (S)outh"
    elif availableDirections == ["w", "e"]:
        directions = "(W)est or (E)ast"  
    return directions


while position[0] != 2 or position[1] != 2:
    availableDirections = grid[position[1]][position[0]]
    
    print("You can move to:", current_options(availableDirections))    
    
    direction = str.lower(input("Where you go: "))
    
    if direction in availableDirections:
        position = updateDirection(direction, position)

    else:
        print("The fuck u doin")
        

print("Victory!")
