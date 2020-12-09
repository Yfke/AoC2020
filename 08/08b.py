import copy
import handheld as hh


def main():
    with open("input.txt", "r") as file:
        instructions = [hh.Instruction(line) for line in file.read().splitlines()]
    for i in range(len(instructions)):
        instruction = instructions[i]
        if(instruction.type == hh.Type.NOP):
            inst2 = copy.deepcopy(instructions)
            inst2[i].type = hh.Type.JUMP
        elif(instruction.type == hh.Type.JUMP):
            inst2 = copy.deepcopy(instructions)
            inst2[i].type = hh.Type.NOP
        p = hh.Program(inst2)
        status, message = p.run()
        if(status == hh.Status.DONE):
            print(message)


if __name__ == "__main__":
    main()
