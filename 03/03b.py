
def main():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    with open("input.txt", "r") as file:
        input = file.read().splitlines()
    product = 1
    for (xdiff, ydiff) in slopes:
        print(xdiff, ydiff)
        x = 0
        trees = 0
        for y in range(0, len(input), ydiff):
            if input[y][x] == '#':
                trees += 1
            x += xdiff
            x %= len(input[0])
        print(trees)
        product *= trees
    print(product)


if __name__ == "__main__":
    main()
