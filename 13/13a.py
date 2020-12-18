
def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()
    mytime = int(input[0])
    ids = [int(s) for s in input[1].split(",") if s != "x"]
    waittimes = [(id, timeUntilNext(id, mytime)) for id in ids]
    mybus = min(waittimes, key=lambda pair: pair[1])
    print(mybus)
    print(mybus[0]*mybus[1])


def timeUntilNext(id, mytime):
    timeSinceDepart = mytime % id
    return id - timeSinceDepart


if __name__ == "__main__":
    main()
