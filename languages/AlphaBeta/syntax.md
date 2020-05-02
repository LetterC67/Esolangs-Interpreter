# AlphaBeta

## About
- AlphaBeta was created by User:Voxel in early 2009 in an attempt to make a language that was easy to write, and had many instructions. The language was also made as an experiment and a test of skills.

## Syntax
- AlphaBeta uses 5 registers as a way to store memory, 2 are changeable and each holds an integer, 1 is a result register and cannot be changed, 1 is used for looping and the other is used for memory ( like brainfuck's > and < ). There is no way of comments. Also, AlphaBeta has 1 kb of ram.

- There are 52 instructions:
```
a     adds 1 to register 1
b     subtracts 1 from register 1
c     adds 10 to register 1
d     subtracts 10 from register 1
e     adds 100 to register 1
f     subtracts 100 from register 1
g     adds 1 to register 2
h     subtracts 1 from register 2
i     adds 10 to register 2
j     subtracts 10 from register 2
k     adds 100 to register 2
l     subtracts 100 from register 2
m     sets register 3 to the logical not of register 1
n     sets register 3 to the logical not of register 2
o     logical ands register 1 and register 2 and sets register 3 to the result
p     logical ors register 1 and register 2 and sets register 3 to the result
q     logical xors register 1 and register 2 and sets register 3 to the result
r     adds register 1 and register 2 and sets register 3 to the result
s     subtracts register 1 and register 2 and sets register 3 to the result
t     multiplies register 1 and register 2 and sets register 3 to the result
u     divides register 1 and register 2 and sets register 3 to the result
v     mods register 1 and register 2 and sets register 3 to the result
w     register 3 to register 1 to the power of register 2
x     clears register 1
y     clears register 2
z     clears register 3
A     sets register 2 to the value of register 1
B     sets register 1 to the value of register 2
C     sets register 3 to the value of register 1
D     sets register 3 to the value of register 2
E     sets register 1 to the value of register 3
F     sets register 2 to the value of register 3
G     sets register 1 to the memory at the memory pointer
H     sets register 2 to the memory at the memory pointer
I     sets the memory at the memory pointer to the value of register 3
J     input a value from the keyboard and store it in register 1
K     input a value from the keyboard and store it in register 2
L     outputs a character to the screen
M     outputs a number to the screen
N     if register 1 equals register 2, goto the position at the position register
O     if register 1 does not equal register 2, goto the position at the position register
P     if register 1 is bigger than or equals register 2, goto the position at the position register
Q     if register 1 is smaller than or equals register 2, goto the position at the position register
R     if register 3 equals 0, goto the position at the position register
```
The memory pointer and the position pointer are 2 different things, but you change them through 1 register. ( The Z command switches between them.)
```
S     adds 1 to the register
T     subtracts 1 to the register
U     adds 10 to the register
V     subtracts 10 to the register
W     adds 100 to the register
X     subtracts 100 to the register
Y     sets the register to 0
Z     switches in-between modes ( starts on memory pointer )
```

## Example
 - Hello World! program
 ```
cccCISccccCIScccCIYx
SGSHaaCLgDLihhhDLDLgggDL
TTGaaCL
SGccbbbCLDLgggDLjggggDLSHDL
TTGaaaCL
```
- 99 bottles of beer program
```
ebZCMyiiiggDLkjjjhhhhDLigggDLgggggDLLjggDLjgggDLi
ggggDLyiiiggDLykigDLjgDLyiiiggDLykhhDLgggDLLigggD
LyiiiggDLykigDLhDLyiiiggDLykiihhhhDLjhhDLhhhDLyii
iggDLykiihDLjjhhDLigDLLyiiiiggggDLyiDLCMyiiiggDLk
jjjhhhhDLigggDLgggggDLLjggDLjgggDLiggggDLyiiiggDL
ykigDLjgDLyiiiggDLykhhDLgggDLLigggDLyiiiiggggDLyi
DLykjjggggDLigggDLiDLjggggDLyiiiggDLykigDLhDLjgDL
yiiiggDLykDLigDLihhDLjgDLyiiiiggggDLjhhDLykiggDLy  
khhhDLiihhDLLyiiiggDLykgggggDLigDLyiiiggDLykhhhDL
iihhhDLhhhDLihhhhDLykiDLjDLyiiiiggggDLyiDLbCMyiii 
ggDLkjjjhhhhDLigggDLgggggDLLjggDLjgggDLiggggDLyii
iggDLykigDLjgDLyiiiggDLykhhDLgggDLLigggDLyiiiggDL
ykigDLhDLyiiiggDLykiihhhhDLjhhDLhhhDLyiiiggDLykii
hDLjjhhDLigDLLyiiiiihhhhDLyiDLLYSSyO
```

## Reference: https://esolangs.org/wiki/AlphaBeta
