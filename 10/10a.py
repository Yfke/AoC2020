
def main():
    with open("input.txt", "r") as file:
        input = [int(line) for line in file.read().splitlines()]
    input.sort()
    # keep track of distribution, the last jump (to device) is already included
    distribution = [0, 0, 1]
    current = 0
    for val in input:
        distribution[val - current - 1] += 1
        current = val
    print(distribution[0], distribution[2], distribution[0]*distribution[2])


if __name__ == "__main__":
    main()
