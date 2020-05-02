from random import randint

extension = '.abc'

class ABC():
    def __init__(self, code):
        self.code = code
        self.accumulator = 0
        self.mode = False

    def interpret(self):
        index = 0
        while index < len(self.code):
            char = self.code[index]
            if char == 'a':
                self.accumulator += 1
            elif char == 'b':
                self.accumulator -= 1
            elif char == 'c':
                if self.mode:
                    print(chr(self.accumulator), end = '')
                else:
                    print(self.accumulator, end = '')
            elif char == 'd':
                self.accumulator *= -1
            elif char == 'r':
                self.accumulator = randint(0,abs(self.accumulator)) * [-1,1][self.accumulator < 0]
            elif char == 'n':
                self.accumulator = 0
            elif char == '$':
                self.mode = not self.mode
            elif char == ';':
                print(self.accumulator,' ', chr(self.accumulator), end = '')
            elif char == 'l':
                index = -1
            index += 1
