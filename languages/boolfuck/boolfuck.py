from math import floor

extension = '.b'

class boolfuck():
    def __init__(self, code):
        self.code = code
        self.data = [0]
        self.pointer = 0
        self.bitOut = 0
        self.bitPos = 0

    def interpret(self):
        self._interpret(0, len(self.code))

    def modifyBit(self, val, pos, _bit): 
        mask = 1 << pos
        return (val & ~mask) | ((_bit << pos) & mask) 

    def _interpret(self, startPos, endPos):
        index = startPos
        while index < endPos:
            char = self.code[index]
            if char == '+':
                self.data[self.pointer] ^= 1
                
            elif char == '>':
                self.pointer += 1
                if self.pointer == self.data.length:
                    data.append(0)
                
            elif char == '<':
                self.pointer -= 1
                if self.pointer == -1:
                    self.data.insert(0, 0)
                    self.pointer = 0
                
            elif char == ';':
                self.bitOut = self.modifyBit(self.bitOut, self.bitPos, self.data[self.pointer])
                self.bitPos += 1
                if self.bitPos == 8:
                    print(chr(self.bitOut), end = '')
                    self.bitOut = 0
                    self.bitPos = 0
                    
            elif char == ',':
                self.data[self.pointer] = int(input())
                
            elif char == '[' and self.data[self.pointer] == 0:
                count, _index = 1, index + 1
                try:
                    while count:
                        if self.code[_index] == '[':
                            count += 1
                        elif self.code[_index] == ']':
                            count -= 1
                        _index += 1
                except IndexError:
                    print("Warning: No match ]!")
                    
                index = _index - 1

            elif char == ']' and self.data[self.pointer] == 1:
                count, _index = 1, index - 1
                try:
                    while count:
                        if self.code[_index] == ']':
                            count += 1
                        elif self.code[_index] == '[':
                            count -= 1
                        _index -= 1
                except IndexError:
                    print("Warning: No match [!")

                index = _index 

                            
            index += 1
            
        if self.bitPos:
            print(chr(self.bitOut), end = '')
