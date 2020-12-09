
def main():
    with open("input.txt", "r") as file:
        input = [[set(line) for line in group.splitlines()]
                 for group in file.read().split("\n\n")]
    total = 0
    for group in input:
        u = set().union(*group)
        total += len(u)
    print(total)


if __name__ == "__main__":
    main()
