import re


def main():
    with open("input.txt", "r") as file:
        input = [parse(line) for line in file.read().splitlines()]
    total = 0
    for (min, max, c, str) in input:
        n = str.count(c)
        if min <= n and n <= max:
            total += 1
    print(total)


def parse(string):
    parts = re.split('[- :]', string)
    return (int(parts[0]), int(parts[1]), parts[2], parts[4])


if __name__ == "__main__":
    main()
