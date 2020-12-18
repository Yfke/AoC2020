import time


class Seat():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []
        self.occupied = False
        self.nextOccupied = False

    def occupiedNeighbors(self):
        return len([n for n in self.neighbors if n.occupied])

    def toString(self):
        if self.occupied:
            return "#"
        else:
            return "L"


def main():
    start_time = time.time()
    with open("input.txt", "r") as file:
        input = file.read().splitlines()
    seats = [[None for _ in range(len(input[0]))] for _ in range(len(input))]
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == "L":
                seats[y][x] = Seat(x, y)
    for row in seats:
        for seat in row:
            if seat is not None:
                neighbors = []
                # find visible seats
                # up:
                for step in range(1, seat.y + 1):
                    other = seats[seat.y - step][seat.x]
                    if other is not None:
                        neighbors.append(other)
                        break
                # up left:
                for step in range(1, min(seat.y + 1, seat.x + 1)):
                    other = seats[seat.y - step][seat.x - step]
                    if other is not None:
                        neighbors.append(other)
                        break
                # up right:
                for step in range(1, min(seat.y + 1, len(row) - seat.x)):
                    other = seats[seat.y - step][seat.x + step]
                    if other is not None:
                        neighbors.append(other)
                        break
                # left:
                for step in range(1, seat.x + 1):
                    other = seats[seat.y][seat.x - step]
                    if other is not None:
                        neighbors.append(other)
                        break
                # right:
                for step in range(1, len(row) - seat.x):
                    other = seats[seat.y][seat.x + step]
                    if other is not None:
                        neighbors.append(other)
                        break
                # down:
                for step in range(1, len(seats) - seat.y):
                    other = seats[seat.y + step][seat.x]
                    if other is not None:
                        neighbors.append(other)
                        break
                # down left:
                for step in range(1, min(len(seats) - seat.y, seat.x + 1)):
                    other = seats[seat.y + step][seat.x - step]
                    if other is not None:
                        neighbors.append(other)
                        break
                # up right:
                for step in range(1, min(len(seats) - seat.y, len(row) - seat.x)):
                    other = seats[seat.y + step][seat.x + step]
                    if other is not None:
                        neighbors.append(other)
                        break
                seat.neighbors = neighbors
    while simulate(seats):
        print("step")
    # for round in range(10):
    #     printSeats(seats)
    #     simulate(seats)
    #     print()
    answer = 0
    for row in seats:
        answer += len([s for s in row if s is not None and s.occupied])
    print(answer)
    print(time.time() - start_time)


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
                if(seat.occupiedNeighbors() >= 5):
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
