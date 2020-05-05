extension = '.df'

class deadfish():
    def __init__(self, code):
        self.code = code
        self.acc = 0

    def interpret(self):
        for char in self.code:
            if self.acc == 256 or self.acc < 0:
                self.acc = 0
            if char == 'i':
                self.acc += 1
            elif char == 'd':
                self.acc -= 1
            elif char == 's':
                self.acc *= self.acc
            elif char == 'o':
                print(self.acc, end = '')
