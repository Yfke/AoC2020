import re


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()
    print(max([codeToNumber(s) for s in input]))


def codeToNumber(s):
    return int(re.sub("F|L", "0", re.sub("B|R", "1", s)), 2)


if __name__ == "__main__":
    main()
