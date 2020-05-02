from random import randint

extension = '.bf'

class brainfuck():
    def __init__(self, code):
        self.code = code
        self.pointer = 0
        self.data = [0]
        self.brackets = ["[","]"]
        self.syntax = {
            "+": lambda obj: obj.increase(),
            "-": lambda obj: obj.decrease(),
            ">": lambda obj: obj.next(),
            "<": lambda obj: obj.previous(),
            ".": lambda obj: obj.out(),
            ",": lambda obj: obj.inp(),
        }
        self.size = 256

    def interpret(self):
        self._interpret(0, len(self.code))
        
    def _interpret(self, startPos, endPos):
        index = startPos
        while index < endPos:
            if self.code[index] == self.brackets[0]:
                index = self.openBracket(index, endPos)
            try:
                self.syntax[self.code[index]](self)
            except:
                pass
            index += 1

    def increase(self):
        self.data[self.pointer] += 1
        self.data[self.pointer] %= self.size

    def decrease(self):
        self.data[self.pointer] -= 1
        self.data[self.pointer] %= self.size
        
    def next(self):
        self.pointer += 1
        if self.pointer == len(self.data):
            self.data.append(0)
        
    def previous(self):
        self.pointer -= 1
        if self.pointer == -1:
            self.data.insert(0, 0)

    def out(self):
        print(chr(self.data[self.pointer]), end = "")

    def inp(self):
        self.data[self.pointer] = ord(input()[0])

    def openBracket(self, index, end):
        count, _index = 1, index + 1
        try:
            while count:
                if self.code[_index] == self.brackets[0]:
                    count += 1
                elif self.code[_index] == self.brackets[1]:
                    count -= 1
                _index += 1
        except IndexError:
            print("Warning: Unexpected end!")
            
        while self.data[self.pointer]:
            self._interpret(index + 1, _index - 1)
            
        return _index
