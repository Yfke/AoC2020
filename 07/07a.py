gold = "shiny gold"
bags = {}


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()
    for line in input:
        colour, dict = parse(line)
        bags[colour] = dict
    print(bags)
    answer = 0
    for colour in bags:
        if containsGold(colour) > 0:
            answer += 1
    print(answer)


def containsGold(colour):
    total = 0
    for colour2, amount in bags[colour].items():
        if colour2 == gold:
            total += amount
        else:
            total += amount * containsGold(colour2)
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
