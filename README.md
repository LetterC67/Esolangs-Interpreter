# Esolangs-Interpreter
An interpreter for Esoretic programming language (Esolang) :brain:

# Getting started
- These steps will show you how to run the interpreter on your own system
- More information about Esolang from [Esolang Wiki](https://esolangs.org/wiki/Main_Page) and [Wikipedia](https://en.wikipedia.org/wiki/Esoteric_programming_language)
## Structure:
```
Esolangs-interpreter/
├── main.py
└── languages/
      ├── esolang1
      |     ├── esolang1.py
      |     └── HelloWorld.extension1
      ├── esolang2
      |     ├── esolang1.py
      |     └── HelloWorld.extension2
      ...
      └── esolangN
            ├── esolangN.py
            └── HelloWorld.extensionN
 ```
 - Inside esolangX.py file:
   + A string contains extension of HelloWorld file (aka extensionX)
   + A class named ```esolangX```
 
## Presiquites:
- A computer with Python 3.
- No additional package required!
## Usage:
- Open Command Prompt at the interpreter's directory
  - Command: ```main.py [-h] [-l LANG] [-f FILE] [-i CODE] [-e] [--list-languages]```
    + ```--help``` and ```-h```: Show help message
    + ```--list languages```: Display supported languages
    + ```-l``` and ```--lang```: Choose language (Case sensitive!)
    + ```-f``` and ```--file```: Directory to source file
    + ```-i``` and ```--inline```: Interpret code directly
    + ```-e``` and ```--example```: Run example code (from the HelloWorld file)
  - Example:
    + ```main.py -l boolfuck -e```: Run Hello World code written in brainfuck
    + ```main.py -l CodeFuck -i="."""Goodbye!""""```: Print "Goodbye" in Codefuck. The original code is ```."Goodbye"``` but you must put it in 3 double-quotes to pass it as an argument. So it becomes: ```."""Goodbye"""```
    + ```main.py -l ABC -f dir\to\file.txt```: Open file at ```dir\to\file``` and interpret
- In Python:
```python
import language # language.py (for example) file can be found in languages\language\

foo = language.language("YOUR_CODE")
foo.interpret() #start interpreting
```
## Author:
- Hoang Le (LetterC67 or LetterC)
