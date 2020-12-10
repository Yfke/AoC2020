# cleaner solution without recursion, only dynamic programming


def main():
    global ways, input
    with open("input.txt", "r") as file:
        input = [int(line) for line in file.read().splitlines()]
    input.append(0)
    input.sort()
    ways = [0 for i in range(len(input))]
    ways[len(input) - 1] = 1
    for i in reversed(range(len(input))):
        for j in [i+1, i+2, i+3]:
            if j < len(input) and input[j] - input[i] <= 3:
                ways[i] += ways[j]
    print(ways[0])


if __name__ == "__main__":
    main()
