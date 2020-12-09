def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()
    numbers = [int(n) for n in input]
    for n in numbers:
        for m in numbers:
            rest = 2020 - n - m
            if rest in numbers:
                print(n, m, rest, n*m*rest)


if __name__ == "__main__":
    main()
