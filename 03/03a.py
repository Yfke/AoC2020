
def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()
    x = 0
    trees = 0
    for y in range(len(input)):
        if input[y][x] == '#':
            trees += 1
        x += 3
        x %= len(input[0])
    print(trees)


if __name__ == "__main__":
    main()
