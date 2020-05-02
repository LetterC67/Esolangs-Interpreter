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
- Little Endian
```
Before
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
                              ^
                              dot (.) command will write from right to left
After
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
```
- Note: As soon as all bits are written, the interpreter will print it!   

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
