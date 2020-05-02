# CodeFuck 
## About
- CodeFuck is a variant of BrainFuck.
- It avoids repetitions and adds new operators
- 1024 cells

## Syntax:
```
> Move to next cell
< Move to previous cell
+ Increase the value of current cell
- Increase the value of current cell
. Output ASCII
; Output Integer
, Input ASCII
: Input Integer
f create function
F	run function
[	While != 0
/	While == 0
(	If == 0
{	If != 0
!	If > 0
?	If < 0
| with ( { ! ? : Else If ...
&	Else
] \ ) } # : Close condition block
_	Load VAR
$	VAR value
%your comment%	Comment
```
#### Add number to some operators:
- ```+``` operator increase the current cell by 1. ```+n``` (n is a number). Example: ```+6```
- ``` - [ / { ! ? ``` are similar. Example: ```(3``` (If current cell == 3), ```[8``` (While current cell != 8)

#### Block:
- There are some small changes.
- ```[ / ( {``` end with ```] \ ) }```
- ```? !``` end with ```#```
- Comparsion:
  + C Code:
  ```
  if (*cell==0) {
      putchar(*cell);
  } else if (*cell>0) {
      putchar(*cell);
  } else if (*cell<0) {
      putchar(*cell);
  }
  ```
  + Original Code:
  ```
  (
    .
  |!
    .
  |?
    .
  )
  ```
  + New code:
  ```
  (
    .
  )|!
    .
  #|?
    .
  #
  ```
- New code syntax is a little bit longer but it is easier to use and read

#### Output
- ```. ;``` can be used to print ASCII and Interger value of current cell
- You can also write ```."Text"``` to print "Text" to your screnn!

#### Function:
- To declare a function: ```f1```, ```f2```. There must be a number after ```f```. Numbers must be used in ascending order from 1.
- A function declaration ended by ```f```
- Run function: ```Fn``` (n is a number)
- Example:
```
f1
    +65. %Add 65 to the current cell and print ASCII
f
F1
```
- Output: ```A```

#### Temporary value (VAR):
- ```_``` set VAR to current cell's value
- ```$``` load VAR's value, can be used as a number. Example: ```+$```

## Example: 
- Add 2 numbers:
```
."  ":_>
." +":+$
." =";
```
- Output:
```
  3
+ 4
= 7

## Reference: https://esolangs.org/wiki/CodeFuck
