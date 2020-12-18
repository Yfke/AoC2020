import copy


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()
    grid = [[[True if c == '#' else False for c in line] for line in input]]
    printGrid(grid)
    for _ in range(6):
        grid = expandGrid(grid)
        #printGrid(grid)
        grid, no = stepGrid(grid)
        #printGrid(grid)
        print(no)


def stepGrid(grid):
    xrange = len(grid[0][0])
    yrange = len(grid[0])
    zrange = len(grid)
    numberActive = 0
    # initialize new grid (empty)
    newgrid = [[[False] * xrange for _ in range(yrange)]
               for _ in range(zrange)]
    # activate nodes in new grid, based on rules applied to old grid
    for z in range(zrange):
        for y in range(yrange):
            for x in range(xrange):
                #print(x, y, z)
                #print(grid[z][y][x])
                neighbors = [(xn, yn, zn) for xn in [x-1, x, x+1]
                             for yn in [y-1, y, y+1] for zn in [z-1, z, z+1]
                             if 0 <= yn < yrange if 0 <= xn < xrange
                             if 0 <= zn < zrange
                             if not (xn == x and yn == y and zn == z)]
                #print(neighbors)
                neighbors3 = [grid[zn][yn][xn] for (xn, yn, zn) in neighbors]
                #print(neighbors3)
                neighbors2 = [0 for (xn, yn, zn) in neighbors if grid[zn][yn][xn]]
                #print(neighbors2)
                activeNeighbors = len(neighbors2)
                if activeNeighbors == 2 and grid[z][y][x]:
                    # remain active
                    newgrid[z][y][x] = True
                    numberActive += 1
                elif activeNeighbors == 3:
                    # remain or become active
                    newgrid[z][y][x] = True
                    numberActive += 1
    return newgrid, numberActive


def expandGrid(grid):
    xrange = len(grid[0][0])
    yrange = len(grid[0])
    zrange = len(grid)
    # initialize new, larger grid (empty)
    newgrid = [[[False] * (xrange + 2) for _ in range(yrange + 2)]
               for _ in range(zrange + 2)]
    # copy old grid into new grid
    for z in range(zrange):
        for y in range(yrange):
            for x in range(xrange):
                newgrid[z+1][y+1][x+1] = grid[z][y][x]
    return newgrid


def printGrid(grid):
    for plane in grid:
        for line in plane:
            s = ""
            for bool in line:
                if bool:
                    s += "#"
                else:
                    s += "."
            print(s)
        print()


if __name__ == "__main__":
    main()
