import handheld as hh


def main():
    with open("input.txt", "r") as file:
        instructions = [hh.Instruction(line) for line in file.read().splitlines()]
    p = hh.Program(instructions)
    status, message = p.run()
    print(message)


if __name__ == "__main__":
    main()
