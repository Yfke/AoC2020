import re


class Ticket():
    def __init__(self, s):
        self.numbers = [int(n) for n in s.split(",")]


class Rule():
    def __init__(self, s):
        [self.name, range1, range2] = re.split(": | or ", s)
        [self.min1, self.max1] = [int(n) for n in range1.split("-")]
        [self.min2, self.max2] = [int(n) for n in range2.split("-")]

    def hasNumber(self, n):
        return (self.min1 <= n <= self.max1) or (self.min2 <= n <= self.max2)


def main():
    with open("input.txt", "r") as file:
        input = file.read().split("\n\n")
    rules = [Rule(line) for line in input[0].splitlines()]
    myticket = Ticket(input[1].splitlines()[1])
    others = [Ticket(s) for s in input[2].splitlines()[1:]]

    answer = 0
    for ticket in others:
        for n in ticket.numbers:
            found = False
            for rule in rules:
                if rule.hasNumber(n):
                    found = True
                    break
            if not found:
                answer += n
    print(answer)


if __name__ == "__main__":
    main()
