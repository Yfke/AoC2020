import enum


class Type(enum.Enum):
    ERR = 0
    NOP = 1
    ACC = 2
    JUMP = 3


class Status(enum.Enum):
    IDLE = 1
    RUNNING = 2
    LOOP = 3
    DONE = 4
    ERROR = 5


class Instruction:
    def __init__(self, s):
        self.type, self.number = self.parse(s)
        self.executed = False

    def parse(self, s):
        s2 = s.split(" ")
        type = Type.ERR
        if(s2[0] == "nop"):
            type = Type.NOP
        elif(s2[0] == "acc"):
            type = Type.ACC
        elif(s2[0] == "jmp"):
            type = Type.JUMP
        number = int(s2[1])
        return type, number

    def setExecuted(self):
        self.executed = True
        return True


class Program:
    def __init__(self, instructions):
        self.instructions = instructions
        self.size = len(instructions)
        self.accumulator = 0
        self.pointer = 0
        self.status = Status.IDLE
        self.message = ""

    def step(self):
        if(self.pointer < 0):
            # Error in the code
            self.message = ("Pointer below zero:" + str(self.pointer))
            self.status = Status.Error
            return
        if(self.pointer >= self.size):
            # Program terminates
            self.message = ("Program is terminated. Accumulator value: "
                            + str(self.accumulator))
            self.status = Status.DONE
            return
        inst = self.instructions[self.pointer]
        if inst.executed:
            # Loop detected
            self.message = ("Loop dected at line: " + str(self.pointer)
                            + ". Accumulator value: " + str(self.accumulator))
            self.status = Status.LOOP
            return
        if inst.type == Type.NOP:
            self.pointer += 1
            return inst.setExecuted()
        if inst.type == Type.ACC:
            self.accumulator += inst.number
            self.pointer += 1
            return inst.setExecuted()
        if inst.type == Type.JUMP:
            self.pointer += inst.number
            return inst.setExecuted()

    def run(self):
        self.status = Status.RUNNING
        while(self.status == Status.RUNNING):
            self.step()
        return self.status, self.message
