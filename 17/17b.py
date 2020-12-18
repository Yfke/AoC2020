import copy


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()
    grid = [[[[True if c == '#' else False for c in line] for line in input]]]
    printGrid(grid)
    for _ in range(6):
        grid = expandGrid(grid)
        #printGrid(grid)
        grid, no = stepGrid(grid)
        #printGrid(grid)
        print(no)


def stepGrid(grid):
    xrange = len(grid[0][0][0])
    yrange = len(grid[0][0])
    zrange = len(grid[0])
    wrange = len(grid)
    numberActive = 0
    # initialize new grid (empty)
    newgrid = [[[[False] * xrange for _ in range(yrange)]
               for _ in range(zrange)] for _ in range(wrange)]
    # activate nodes in new grid, based on rules applied to old grid
    for w in range(wrange):
        for z in range(zrange):
            for y in range(yrange):
                for x in range(xrange):
                    #print(x, y, z)
                    #print(grid[z][y][x])
                    neighbors = [(xn, yn, zn, wn) for xn in [x-1, x, x+1]
                                 for yn in [y-1, y, y+1]
                                 for zn in [z-1, z, z+1]
                                 for wn in [w-1, w, w+1]
                                 if 0 <= yn < yrange if 0 <= xn < xrange
                                 if 0 <= zn < zrange if 0 <= wn < wrange
                                 if not (xn == x and yn == y and zn == z and wn == w)]
                    #print(neighbors)
                    #neighbors3 = [grid[wn][zn][yn][xn] for (xn, yn, zn, wn) in neighbors]
                    #print(neighbors3)
                    neighbors2 = [0 for (xn, yn, zn, wn) in neighbors if grid[wn][zn][yn][xn]]
                    #print(neighbors2)
                    activeNeighbors = len(neighbors2)
                    if activeNeighbors == 2 and grid[w][z][y][x]:
                        # remain active
                        newgrid[w][z][y][x] = True
                        numberActive += 1
                    elif activeNeighbors == 3:
                        # remain or become active
                        newgrid[w][z][y][x] = True
                        numberActive += 1
    return newgrid, numberActive


def expandGrid(grid):
    xrange = len(grid[0][0][0])
    yrange = len(grid[0][0])
    zrange = len(grid[0])
    wrange = len(grid)
    # initialize new, larger grid (empty)
    newgrid = [[[[False] * (xrange + 2) for _ in range(yrange + 2)]
               for _ in range(zrange + 2)] for _ in range(wrange + 2)]
    # copy old grid into new grid
    for w in range(wrange):
        for z in range(zrange):
            for y in range(yrange):
                for x in range(xrange):
                    newgrid[w+1][z+1][y+1][x+1] = grid[w][z][y][x]
    return newgrid


def printGrid(grid):
    for space in grid:
        for plane in space:
            for line in plane:
                s = ""
                for bool in line:
                    if bool:
                        s += "#"
                    else:
                        s += "."
                print(s)
            print()
        print("\n\n")


if __name__ == "__main__":
    main()
