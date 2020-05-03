from math import floor

extension = '.b'

class boolfuck():
    def __init__(self, code):
        self.code = code
        self.data = [0]
        self.pointer = 0
        self.bitOut = ''
        self.bitInp = 0
        self.input = ''

    def interpret(self):
        if ',' in self.code:
            self.input = input('Input (you can leave it blank): ')
            
        self.input = ''.join([self.input[index : index + 8][::-1] for index in range(0, len(self.input), 8)])
        
        self._interpret(0, len(self.code))

        missing = ''
        if len(self.bitOut) % 8:
            missing = self.bitOut[floor(len(self.bitOut) / 8) * 8 : len(self.bitOut)][::-1]

        self.bitOut = [self.bitOut[index : index + 8][::-1] for index in range(0, floor(len(self.bitOut) / 8) * 8, 8)]
        for byte in self.bitOut:
            print(chr(int(byte, 2)), end = '')

        if missing:
            print(chr(int(missing, 2)), end = '') 

    def _interpret(self, startPos, endPos):
        index = startPos
        while index < endPos:
            char = self.code[index]
            if char == '+':
                self.data[self.pointer] ^= 1
                
            elif char == '>':
                self.pointer += 1
                if self.pointer == len(self.data):
                    self.data.append(0)
                
            elif char == '<':
                self.pointer -= 1
                if self.pointer == -1:
                    self.data.insert(0, 0)
                    self.pointer = 0
                
            elif char == ';':
                self.bitOut += str(self.data[self.pointer])
                    
            elif char == ',':
                if self.bitInp >= len(self.input):
                    self.data[self.pointer] = 0
                else:
                    self.data[self.pointer] = int(self.input[self.bitInp])
                self.bitInp += 1
                
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
