# Idea: dynamic programming, use recursive computation but store any computed
# subanswers in an array "ways"


def main():
    global ways, input
    with open("input.txt", "r") as file:
        input = [int(line) for line in file.read().splitlines()]
    input.append(0)
    input.sort()
    # Initially, ways does not contain any intermediate answers
    ways = [None for i in range(len(input))]
    # Start recursive computation
    print(numberOfWays(0))


def numberOfWays(i):  # i is array index
    if i == len(input) - 1:
        # end of input array reached: there is exactly one possible sequence
        return 1
    if ways[i] is not None:
        # we already computed this value
        return ways[i]
    total = 0
    # look ahead in array, only compare to values that differ by at most 3
    for [j in [i+1, i+2, i+3] if j < len(input) and input[j] - input[i] <= 3]:
        total += numberOfWays(j)
    ways[i] = total
    return total


if __name__ == "__main__":
    main()
