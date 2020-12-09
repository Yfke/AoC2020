lookback = 25


def main():
    with open("input.txt", "r") as file:
        input = [int(line) for line in file.read().splitlines()]
    for i in range(lookback, len(input)):
        if not isValid(input[i], input[i-lookback:i]):
            print(input[i])


def isValid(n, lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i]+lst[j] == n:
                return True
    return False


if __name__ == "__main__":
    main()
