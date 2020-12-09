lookback = 25


def main():
    with open("input.txt", "r") as file:
        input = [int(line) for line in file.read().splitlines()]
    # find the first invalid number (part 1)
    # invalid number is invn, at index invi
    invi = 0
    for i in range(lookback, len(input)):
        if not isValid(input[i], input[i-lookback:i]):
            print("Pt 1:", input[i])
            invi = i
    invn = input[invi]
    # find starting index (i) and ending index (j) of range that sums to invn
    i, j = findSum(invn, input[:invi])
    if i is None:
        i, j = findSum(invn, input[invi+1:])
        i += invn+1
        j += invn+1
    # given i and j, find the minimum and maximum value in that range
    minval = min(input[i:j+1])
    maxval = max(input[i:j+1])
    print(minval, maxval, minval+maxval)


def findSum(n, lst):
    imin = 0
    imax = 0
    total = lst[0]
    while imin < len(lst):
        if total == n:
            # found!
            return imin, imax
        elif total > n:
            # current sum too big. Step min-index and update sum
            total -= lst[imin]
            imin += 1
        else:
            # current sum too small. Step max-index and update sum
            imax += 1
            total += lst[imax]
    return None, None


def isValid(n, lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i]+lst[j] == n:
                return True
    return False


if __name__ == "__main__":
    main()
