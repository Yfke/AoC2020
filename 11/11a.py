class Seat():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []
        self.occupied = False
        self.nextOccupied = False

    def occupiedNeighbors(self):
        return len([n for n in self.neighbors if n.occupied])

    # for debugging:
    def toString(self):
        if self.occupied:
            return "#"
        else:
            return "L"


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()
    # initialize a floor without any seats, then read in the input
    seats = [[None for _ in range(len(input[0]))] for _ in range(len(input))]
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == "L":
                seats[y][x] = Seat(x, y)
    # connect the seats to their neighbors (eight spots around them)
    for row in seats:
        for seat in row:
            if seat is not None:
                validys = [y for y in [seat.y-1, seat.y, seat.y+1]
                           if (y >= 0 and y < len(seats))]
                validxs = [x for x in [seat.x-1, seat.x, seat.x+1]
                           if x >= 0 and x < len(row)]
                neighbors = [seats[y][x] for y in validys for x in validxs
                             if (seats[y][x] is not None and
                                 not (x == seat.x and y == seat.y))]
                seat.neighbors = neighbors
    # simulate the updates
    while simulate(seats):
        print("step")
    answer = 0
    for row in seats:
        answer += len([s for s in row if s is not None and s.occupied])
    print(answer)


def printSeats(seats):
    for row in seats:
        line = ""
        for seat in row:
            if seat is None:
                line += "."
            else:
                line += seat.toString()
        print(line)


def simulate(seats):
    changed = False
    for row in seats:
        for seat in row:
            if seat is None:
                continue
            if seat.occupied:
                if(seat.occupiedNeighbors() >= 4):
                    # seat becomes empty
                    seat.nextOccupied = False
                    changed = True
            else:
                if(seat.occupiedNeighbors() == 0):
                    # seat becomes occupied
                    seat.nextOccupied = True
                    changed = True
    for row in seats:
        for seat in row:
            if seat is not None:
                seat.occupied = seat.nextOccupied
    return changed


if __name__ == "__main__":
    main()
