import time


test1 = [0, 3, 6]
input = [15, 12, 0, 14, 3, 1]


def main():
    start_time = time.time()
    start = input
    history = [-1] * 30000000
    # initialize fixed input (but skip the last one)
    # -1 signifies "this value hasn't occurred yet"
    for i in range(len(start) - 1):
        history[start[i]] = i
    # store last fixed input into separate variable
    prev = start[-1]
    for i in range(len(start), 30000000):
        # at which index did this number occur last? (-1 = none)
        occurs = history[prev]
        # store the index for future reference
        history[prev] = i-1
        if occurs == -1:
            # say zero
            prev = 0
        else:
            # say difference
            prev = i - 1 - occurs
    print(prev)
    print(time.time() - start_time)


if __name__ == "__main__":
    main()
