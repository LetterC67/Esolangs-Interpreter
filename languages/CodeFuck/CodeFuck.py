extension = '.cf'

class CodeFuck():
    def __init__(self, code):
        self.code = code
        self.data = [0] * 1024
        self.pointer = 0
        self.function = []
        self.VAR = 0

    def getNum(self, _from, default):
        index = _from
        num = ''
        
        if self.code[index] == '$':
            return self.VAR
        
        while index < len(self.code):
            if '9' >= self.code[index] >= '0':
                num += self.code[index]
            else:
                break
            index += 1
        if num == '':
            return default
        return int(num)
    
    def interpret(self):
        self._interpret(0, len(self.code))

    def close(self, index, _open, end):
        count, _index = 1, index + 1
        if type(_open) == str:
            _open = [_open]
        try:
            while count:
                if self.code[_index] in _open:
                    count += 1
                elif self.code[_index] == end:
                    count -= 1
                _index += 1
        except IndexError:
            print("Warning: Unexpected end!")
            return
        return _index

    def endElse(self, start):
        index = start
        while index < len(self.code):
            if self.code[index] in ['#', ')', '}']:
                if index == len(self.code) - 1:
                    return len(self.code) - 1
                elif self.code[index + 1] not in ['&','|']:
                    return index + 1
            index += 1
                
    
    def _interpret(self, startPos, endPos):
        index = startPos
        while index < endPos:
            char = self.code[index]
            if char == '>':
                self.pointer += self.getNum(index + 1, 1)
                
            elif char == '<':
                self.pointer -= self.getNum(index + 1, 1)
                
            elif char == '+':
                self.data[self.pointer] += self.getNum(index + 1, 1)
                
            elif char == '-':
                self.data[self.pointer] -= self.getNum(index + 1, 1)
                
            elif char == '.':
                if index + 1 != len(self.code) and self.code[index + 1] == '"':
                    end = index + 2
                    while self.code[end] != '"':
                        end += 1
                    print(self.code[index + 2 : end], end = '')
                    index = end + 1
                    continue
                num = self.getNum(index + 1, 1)
                for i in range(num):
                    print(chr(self.data[self.pointer]), end = '')
                
            elif char == ';':
                print(self.data[self.pointer], end = '')
                
            elif char == ',':
                inp = input()
                if inp != '':
                    self.data[self.pointer] = ord(inp[0])
                else:
                    print("Invalid input!!")
                
            elif char == ':':
                inp = input()
                if inp != '':
                    self.data[self.pointer] = int(inp)
                else:
                    print("Invalid input!!")
                
            elif char == 'f':
                _index = index + 1
                while self.code[_index] != 'f':
                    _index += 1
                self.function.append([index + 1, _index])
                index = _index
                
            elif char == 'F':
                funcName = self.getNum(index + 1, 0)
                self._interpret(self.function[funcName - 1][0], self.function[funcName - 1][1])
                
            elif char == '[':
                num = self.getNum(index + 1, 0)
                _index = self.close(index, '[', ']')
                    
                while self.data[self.pointer] != num:
                    self._interpret(index + 1, _index - 1)

                index = _index - 1
                
            elif char == '/':
                num = self.getNum(index + 1, 0)
                _index = self.close(index, '/', '\\')

                while self.data[self.pointer] == num:
                    self._interpret(index + 1, _index - 1)

                index = _index - 1
                
            elif char == '(':
                num = self.getNum(index + 1, 0)
                _index = self.close(index, '(', ')')

                if self.data[self.pointer] == num:
                    self._interpret(index + 1, _index - 1)
                    _index = self.endElse(_index)

                index = _index - 1

            elif char == '{':
                num = self.getNum(index + 1, 0)
                _index = self.close(index, '{', '}')

                if self.data[self.pointer] != num:
                    self._interpret(index + 1, _index - 1)
                    _index = self.endElse(_index)

                index = _index - 1
                
            elif char == '!':
                num = self.getNum(index + 1, 0)
                _index = self.close(index, ['(','?'], '#')

                if self.data[self.pointer] > num:
                    self._interpret(index + 1, _index - 1)
                    _index = self.endElse(_index)

                index = _index - 1
                
            elif char == '?':
                num = self.getNum(index + 1, 0)
                _index = self.close(index, ['!','?'], '#')

                if self.data[self.pointer] < num:
                    self._interpret(index + 1, _index - 1)
                    _index = self.endElse(_index)

                index = _index - 1

            elif char == '&':
                num = self.getNum(index + 1, 0)
                _index = self.close(index, ['!','?'], '#')
                self._interpret(index + 1, _index - 1)
                index = _index - 1

            elif char == '_':
                self.VAR = self.data[self.pointer]
                
            index += 1
