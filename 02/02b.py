import re


def main():
    with open("input.txt", "r") as file:
        input = [parse(line) for line in file.read().splitlines()]
    total = 0
    for (p1, p2, c, str) in input:
        if (str[p1-1] == c) != (str[p2-1] == c):
            total += 1
    print(total)


def parse(string):
    parts = re.split('[- :]', string)
    return (int(parts[0]), int(parts[1]), parts[2], parts[4])


if __name__ == "__main__":
    main()
