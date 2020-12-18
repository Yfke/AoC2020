
def main():
    with open("input.txt", "r") as file:
        input = [parse(line) for line in file.read().splitlines()]
    x, y = 0, 0  # ship location
    wx, wy = 10, 1  # waypoint location (east, north)
    direction = 0  # that's east

    for (instruction, amount) in input:
        if(instruction == 'N'):
            wx, wy = moveNorth(wx, wy, amount)
        elif(instruction == 'S'):
            wx, wy = moveSouth(wx, wy, amount)
        elif(instruction == 'E'):
            wx, wy = moveEast(wx, wy, amount)
        elif(instruction == 'W'):
            wx, wy = moveWest(wx, wy, amount)
        elif(instruction == "L"):
            times = amount // 90
            for _ in range(times):
                wx, wy = rotateLeft(wx, wy)
        elif(instruction == "R"):
            times = amount // 90
            for _ in range(times):
                wx, wy = rotateRight(wx, wy)
        elif(instruction == "F"):
            x += wx*amount
            y += wy*amount
    print(x, y)
    print(abs(x) + abs(y))


def rotateLeft(wx, wy):
    return -1*wy, wx


def rotateRight(wx, wy):
    return wy, -1*wx


def moveNorth(wx, wy, amount):
    return wx, wy + amount


def moveSouth(wx, wy, amount):
    return wx, wy - amount


def moveEast(wx, wy, amount):
    return wx + amount, wy


def moveWest(wx, wy, amount):
    return wx - amount, wy


def parse(s):
    return (s[0], int(s[1:]))


if __name__ == "__main__":
    main()
