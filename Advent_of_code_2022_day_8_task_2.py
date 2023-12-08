# Makes 2D grid out of the nummbers
def calculate_scenic_score(grid, i, j):
    rows = len(grid)
    cols = len(grid[0])

    # Calculates the distance of a tree in every direction, adds a +1 counter,
    #and adds another +1 for a tree bigger or equal   
    def calculate_distance(i, j, direction):
        height = grid[i][j]
        distance = 0

        if direction == "up":
            for x in range(i - 1, -1, -1):
                if grid[x][j] >= height:
                    distance += 1
                    break
                distance += 1

        elif direction == "down":
            for x in range(i + 1, rows):
                if grid[x][j] >= height:
                    distance += 1
                    break
                distance += 1

        elif direction == "left":
            for y in range(j - 1, -1, -1):
                if grid[i][y] >= height:
                    distance += 1
                    break
                distance += 1

        elif direction == "right":
            for y in range(j + 1, cols):
                if grid[i][y] >= height:
                    distance += 1
                    break
                distance += 1

        return distance

    # Puts the scenic_score to 1, so that it can be multipied by distance
    scenic_score = 1

    # Calculates the scenic_score
    for direction in ["up", "down", "left", "right"]:
        distance = calculate_distance(i, j, direction)
        scenic_score *= distance 

    return scenic_score

def find_highest_scenic_score(grid):
    highest_scenic_score = 0

    # Iterates over all trees
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            scenic_score = calculate_scenic_score(grid, i, j)
            highest_scenic_score = max(highest_scenic_score, scenic_score)

    return highest_scenic_score

# Reads the text file, turns the rows into lists, and uses map to iterate thru each element
file_path = "forest.txt"
with open(file_path, "r") as file:
    tree_grid = [list(map(int, line.strip())) for line in file]

# Prints the highhest scenic score
result = find_highest_scenic_score(tree_grid)
print("Highest scenic score:", result)