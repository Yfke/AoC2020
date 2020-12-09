import enum


class Type(enum.Enum):
    NOTYPE = auto()
    NOP = auto()
    ACC = auto()
    JUMP = auto()


class Status(enum.Enum):
    IDLE = auto()
    RUNNING = auto()
    LOOP = auto()
    DONE = auto()
    ERROR = auto()


class Instruction:
    def __init__(self, s):
        # Parse the string into an instruction:
        self.type = Type.NOTYPE
        self.number = 0
        self.parse(s)
        # Initially, the instruction is not yet executed
        self.executed = False

    def parse(self, s):
        typestring, numberstring = s.split(" ")[0:2]
        self.number = int(numberstring)
        if(typestring == "nop"):
            self.type = Type.NOP
        elif(typestring == "acc"):
            self.type = Type.ACC
        elif(typestring == "jmp"):
            self.type = Type.JUMP


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
        if inst.type == Type.ACC:
            self.accumulator += inst.number
            self.pointer += 1
        if inst.type == Type.JUMP:
            self.pointer += inst.number
        inst.executed = True

    def run(self):
        self.status = Status.RUNNING
        while(self.status == Status.RUNNING):
            self.step()
        return self.status, self.message
