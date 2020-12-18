from enum import Enum, auto


class Type(Enum):
    ATOM = auto()
    MULT = auto()
    SUM = auto()


class Expression():
    def __init__(self, s):
        if "+" not in s and "*" not in s:
            # this expression is just a number
            self.type = Type.ATOM
            self.value = int(s)
        else:
            self.type, self.lhs, self.rhs = parse(s)

    def evaluate(self):
        if self.type == Type.ATOM:
            return self.value
        elif self.type == Type.MULT:
            return self.lhs.evaluate() * self.rhs.evaluate()
        elif self.type == Type.SUM:
            return self.lhs.evaluate() + self.rhs.evaluate()


def parse(s):
    # find left-most operator outside of bracketing:
    depth = 0
    for i in reversed(range(len(s))):
        if s[i] == ")":
            depth += 1
            lhsAtomic = False
        elif s[i] == "(":
            depth -= 1
        elif s[i] == "*" and depth == 0:
            # first operator is multiplication
            return Type.MULT, Expression(s[:i-1]), Expression(s[i+2:])
        elif s[i] == "+" and depth == 0:
            # first operator is sum
            return Type.SUM, Expression(s[:i-1]), Expression(s[i+2:])
    # if end is reached, strip outer brackets, try again
    return parse(s[1:-1])


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()
    answer = 0
    for line in input:
        exp = Expression(line)
        answer += exp.evaluate()
    print(answer)


if __name__ == "__main__":
    main()
