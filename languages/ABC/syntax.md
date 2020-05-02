# ABC Esolang

## Syntax
```
a - Increment the accumulator
b - Decrement the accumulator
c - Output the accumulator

d - Invert accumulator
r - Set accumulator to a random number between 0 and accumulator
n - Set accumulator to 0

$ - Toggle ASCII output mode.  When on, the c instruction prints the accumulator as an ASCII character.
l - Loop back to the beginning of the program.  Accumulator and ASCII mode does not reset.
; - Debug.  Prints out accumulator as a number and ascii character.
Unknown instructions are treated as NOPs.
```
## Example
- Simulate a dice throw:
```
aaaaarac
```
- Random phone number generator: 
```
ac

naaaaaaaaradc
naaaaaaaaarc
naaaaaaaaarc

naaaaaaaaradc
naaaaaaaaarc
naaaaaaaaarc

naaaaaaaaradc
naaaaaaaaarc
naaaaaaaaarc
naaaaaaaaarc
```

## Reference: https://esolangs.org/wiki/ABC
