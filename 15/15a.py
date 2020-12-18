import time


test1 = [0, 3, 6]
input = [15, 12, 0, 14, 3, 1]


def main():
    start_time = time.time()
    start = input
    history = {}
    for i in range(len(start) - 1):
        history[start[i]] = i
    prev = start[-1]
    for i in range(len(start), 30000000):
        occurs = history.get(prev)
        history[prev] = i-1
        if occurs is None:
            # say zero
            prev = 0
        else:
            # say difference
            prev = i - 1 - occurs
    print(prev)
    print(time.time() - start_time)


if __name__ == "__main__":
    main()
