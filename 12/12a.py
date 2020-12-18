
def main():
    with open("input.txt", "r") as file:
        input = [parse(line) for line in file.read().splitlines()]
    x, y = 0, 0
    direction = 0 # that's east

    for (instruction, amount) in input:
        if(instruction == 'N'):
            x, y = moveNorth(x, y, amount)
        elif(instruction == 'S'):
            x, y = moveSouth(x, y, amount)
        elif(instruction == 'E'):
            x, y = moveEast(x, y, amount)
        elif(instruction == 'W'):
            x, y = moveWest(x, y, amount)
        elif(instruction == "L"):
            direction += amount
            direction %= 360
        elif(instruction == "R"):
            direction -= amount
            direction %= 360
        elif(instruction == "F"):
            if direction == 0:
                x, y = moveEast(x, y, amount)
            elif direction == 90:
                x, y = moveNorth(x, y, amount)
            elif direction == 180:
                x, y = moveWest(x, y, amount)
            elif direction == 270:
                x, y = moveSouth(x, y, amount)
    print(x, y)
    print(abs(x) + abs(y))


def moveNorth(x, y, amount):
    return x, y + amount


def moveSouth(x, y, amount):
    return x, y - amount


def moveEast(x, y, amount):
    return x + amount, y


def moveWest(x, y, amount):
    return x - amount, y


def parse(s):
    return (s[0], int(s[1:]))


if __name__ == "__main__":
    main()
