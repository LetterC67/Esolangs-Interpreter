# Boolfuck

## About
- Boolfuck is an esoteric programming language based on Brainfuck, but operating only on bits. It does, however, provide input and output.

## Syntax
```
+	Flips the value of the bit under the pointer.
,	Reads a bit from the input stream, storing it under the pointer. The end-user types information using characters, though. Bytes are read in little-endian order—the first bit read from the character a, for instance, is 1, followed by 0, 0, 0, 0, 1, 1, and finally 0. If the end-of-file has been reached, outputs a zero to the bit under the pointer.
;	Outputs the bit under the pointer to the output stream. The bits get output in little-endian order, the same order in which they would be input. If the total number of bits output is not a multiple of eight at the end of the program, the last character of output gets padded with zeros on the more significant end.
<	This moves the pointer left by one bit.
>	This moves the pointer right by one bit.
[	If the value under the pointer is zero, jumps forward, just past the matching ] character.
]	Jumps back to the matching [ character.
```
- Little Endian, Output & Input
  + Input:
  ``` 
  The interpreter will ask for input if a comma is found, no space allowed:
    Input (you can leave it blank): 10100101010101001001 
  
  
  Input stream
      0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  ...
    | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | ...
                                  ^ comma (,) will read a bit from the input stream and write it to the tape
                                  
    After reading 1 byte, it will move to next byte
      0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  ...
    | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | ...
                                                                  ^ move to here
                                                                
  Tape
      0   1   2   3   4   5   6   7   ...
    | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | ...
                                  ^ Write here from the right to the left
                                  
    After a byte has been written, the pointer will move to next byte
      0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  ...
    | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ...
                                                                  ^ move to here
   
  ```
  + Output:
  ```
  Tape
    0   1   2   3   4   5   6   7   ...
  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ...
                                ^
                                dot (.) command will write from the right to the left
  Output stream
    0   1   2   3   4   5   6   7   ...
  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | ...
  ```

## Example
- Hello, world!
```
;;;+;+;;+;+;
+;+;+;+;;+;;+;
;;+;;+;+;;+;
;;+;;+;+;;+;
+;;;;+;+;;+;
;;+;;+;+;+;;
;;;;;+;+;;
+;;;+;+;;;+;
+;;;;+;+;;+;
;+;+;;+;;;+;
;;+;;+;+;;+;
;;+;+;;+;;+;
+;+;;;;+;+;;
;+;+;+;
```

## Reference:
- https://esolangs.org/wiki/Boolfuck
- http://samuelhughes.com/boof/
