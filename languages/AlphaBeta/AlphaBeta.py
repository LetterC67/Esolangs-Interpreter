from math import floor

extension = '.ab'

class AlphaBeta:
    def __init__(self, code):
        self.reg = [0, 0, 0]
        self.data = [0] * 1024
        self.pointer = [0, 0]
        self.mode = 0
        self.code = code

    def interpret(self):
        index = 0
        while index < len(self.code):
            char = self.code[index]
            if char == 'a': self.reg[0] += 1
            elif char == 'b': self.reg[0] -= 1
            elif char == 'c': self.reg[0] += 10
            elif char == 'd': self.reg[0] -= 10
            elif char == 'e': self.reg[0] += 100
            elif char == 'f': self.reg[0] -= 100
            elif char == 'g': self.reg[1] += 1
            elif char == 'h': self.reg[1] -= 1
            elif char == 'i': self.reg[1] += 10
            elif char == 'j': self.reg[1] -= 10
            elif char == 'k': self.reg[1] += 100
            elif char == 'l': self.reg[1] -= 100
            elif char == 'm': self.reg[2] = ~self.reg[0]
            elif char == 'n': self.reg[2] = ~self.reg[1]
            elif char == 'o': self.reg[2] = self.reg[0] & self.reg[1]
            elif char == 'p': self.reg[2] = self.reg[0] | self.reg[1]
            elif char == 'q': self.reg[2] = self.reg[0] ^ self.reg[1]
            elif char == 'r': self.reg[2] = self.reg[0] + self.reg[1]
            elif char == 's': self.reg[2] = self.reg[0] - self.reg[1]
            elif char == 't': self.reg[2] = self.reg[0] * self.reg[1]
            elif char == 'u': self.reg[2] = floor(self.reg[0] / self.reg[1])
            elif char == 'v': self.reg[2] = self.reg[0] % self.reg[1]
            elif char == 'w': self.reg[2] = self.reg[1] ** self.reg[2]
            elif char == 'x': self.reg[0] = 0
            elif char == 'y': self.reg[1] = 0
            elif char == 'z': self.reg[2] = 0
            elif char == 'A': self.reg[1] = self.reg[0]
            elif char == 'B': self.reg[0] = self.reg[1]
            elif char == 'C': self.reg[2] = self.reg[0]
            elif char == 'D': self.reg[2] = self.reg[1]
            elif char == 'E': self.reg[0] = self.reg[2]
            elif char == 'F': self.reg[1] = self.reg[2]
            elif char == 'G': self.reg[0] = self.data[self.pointer[0]]
            elif char == 'H': self.reg[1] = self.data[self.pointer[0]]
            elif char == 'I': self.data[self.pointer[0]] = self.reg[2]
            elif char == 'J': self.reg[0] = ord(input()[0])
            elif char == 'K': self.reg[1] = ord(input()[0])
            elif char == 'L': print(chr(self.reg[2]), end = '')
            elif char == 'M': print(self.reg[2], end = '')
            elif char == 'N':
                if self.reg[0] == self.reg[1]:
                    index = self.data[self.pointer[1]] 
            elif char == 'O':
                if self.reg[0] != self.reg[1]:
                    index = self.data[self.pointer[1]]
            elif char == 'P':
                if self.reg[0] >= self.reg[1]:
                    index = self.data[self.pointer[1]]
            elif char == 'Q':
                if self.reg[0] <= self.reg[1]:
                    index = self.data[self.pointer[1]]
            elif char == 'R':
                if not self.reg[2]:
                    index = data[mode] - 1
            elif char == 'S': self.pointer[self.mode] += 1
            elif char == 'T': self.pointer[self.mode] -= 1
            elif char == 'U': self.pointer[self.mode] += 10
            elif char == 'V': self.pointer[self.mode] -= 10
            elif char == 'W': self.pointer[self.mode] += 100
            elif char == 'X': self.pointer[self.mode] -= 100
            elif char == 'Y': self.pointer[self.mode] = 0
            elif char == 'Z': self.mode = not self.mode
            index += 1
