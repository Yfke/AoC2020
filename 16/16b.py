import re
import copy


class Ticket():
    def __init__(self, s):
        self.numbers = [int(n) for n in s.split(",")]
        self.isValid = True


class Rule():
    def __init__(self, s, ticketlength):
        [self.name, range1, range2] = re.split(": | or ", s)
        [self.min1, self.max1] = [int(n) for n in range1.split("-")]
        [self.min2, self.max2] = [int(n) for n in range2.split("-")]
        self.possibilities = set(range(ticketlength))
        self.position = None

    def coversNumber(self, n):
        return (self.min1 <= n <= self.max1) or (self.min2 <= n <= self.max2)


def main():
    # Parse the input, create Ticket/Rule objects
    with open("input.txt", "r") as file:
        input = file.read().split("\n\n")
    myticket = Ticket(input[1].splitlines()[1])
    others = [Ticket(s) for s in input[2].splitlines()[1:]]
    noOfFields = len(myticket.numbers)
    rules = [Rule(line, noOfFields) for line in input[0].splitlines()]

    # pt 1
    # Create a set of all valid numbers
    validNos = set([])
    for rule in rules:
        validNos.update(range(rule.min1, rule.max1 + 1))
        validNos.update(range(rule.min2, rule.max2 + 1))
    answer = 0
    for ticket in others:
        # Check if all numbers in this ticket are valid
        for n in ticket.numbers:
            if n not in validNos:
                # this number is in none of the ranges, the ticket is invalid
                answer += n
                ticket.isValid = False

    # pt 2
    tickets = [t for t in others if t.isValid]
    tickets.append(myticket)

    # filter out the rule/position combinations that are impossible
    for ticket in tickets:
        for i in range(len(ticket.numbers)):
            for rule in rules:
                if not rule.coversNumber(ticket.numbers[i]):
                    rule.possibilities.remove(i)

    # fix rule/position combinations by repeated elimination
    done = False
    while not done:
        done = True
        for rule in rules:
            if len(rule.possibilities) == 1:
                rule.position = rule.possibilities.pop()
                for other in rules:
                    other.possibilities.discard(rule.position)
                done = False

    answer = 1
    for rule in rules:
        if rule.name[0:9] == "departure":
            answer *= myticket.numbers[rule.position]
    print(answer)


if __name__ == "__main__":
    main()
