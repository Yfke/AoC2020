gold = "shiny gold"


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()
    bags = {}
    resolved = {}
    for line in input:
        colour, dict = parse(line)
        bags[colour] = dict
    print(contents(gold, bags))


def contents(colour, bags):
    if len(bags[colour]) == 0:
        return 0
    total = 0
    for colour2, amount in bags[colour].items():
        total += amount + amount * contents(colour2, bags)
    return total


def parse(s):
    temp = s.split(" bags contain ")
    colour = temp[0]
    contents = temp[1].split(", ")
    cdict = {}
    if contents[0] == "no other bags.":
        return colour, cdict
    for description in contents:
        words = description.split()
        number = int(words[0])
        innercolour = words[1] + " " + words[2]
        cdict[innercolour] = number
    return colour, cdict


if __name__ == "__main__":
    main()
