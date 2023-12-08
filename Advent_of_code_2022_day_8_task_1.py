#Makes 2D grid of the lists
def count_visible_trees(grid):
    rows = len(grid)
    cols = len(grid[0])

    #Function to check if a tree at position (i, j) is visible 
    def is_visible(i, j):
        height = grid[i][j]

        # For every tree that is not >= in height returns True, 
        # else it breaks out of the loop
        # Check top
        for x in range(i):
            if grid[x][j] >= height:
                break
        else:
            return True

        # Check bottom
        for x in range(i + 1, rows):
            if grid[x][j] >= height:
                break
        else:
            return True

        # Check left
        for y in range(j):
            if grid[i][y] >= height:
                break
        else:
            return True

        # Check right
        for y in range(j + 1, cols):
            if grid[i][y] >= height:
                break
        else:
            return True

        # If a taller tree is found returns a False
        return False 

    visible_count = 0

    # Iterates over all trees adds a +1 for every True, and returns the count
    for i in range(rows):
        for j in range(cols):
            if is_visible(i, j):
                visible_count += 1

    return visible_count

# Reads the text file, turns the rows into lists, 
# and uses map to iterate thru each element
file_path = "forest.txt"
with open(file_path, "r") as file:
    tree_grid = [list(map(int, line.strip())) for line in file]

# Prints number of visible trees
result = count_visible_trees(tree_grid)
print("Total visible trees:", result)