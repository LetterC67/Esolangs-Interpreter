# Esolangs Interpreter
An interpreter for Esoteric programming language (Esolang) :brain: :computer:

Esoteric programming languages are really different from programming languages which you use everyday such as C/C++, Python, JS, etc. "They are designed to test the boundaries of computer programming design" (Wikipedia). Some of them are joke :smiley: and their syntax drive me crazy :grinning:

By the way, using these Esolangs to make something is a good way to challenge yourself. Have fun! (Actually not really fun, unreadable code :unamused:)

## Getting started :running:
- These steps will show you how to run the interpreter on your own system
- Esolangs' syntax [here](syntax.md)
- Detailed information about Esolang from [Esolang Wiki](https://esolangs.org/wiki/Main_Page) and [Wikipedia](https://en.wikipedia.org/wiki/Esoteric_programming_language)
### Structure :dna:
```
Esolangs-interpreter/
├── main.py
├── syntax.md
└── languages/
      ├── esolang1
      |     ├── esolang1.py
      |     ├── syntax.md
      |     └── HelloWorld.extension1
      ├── esolang2
      |     ├── esolang1.py
      |     ├── syntax.md
      |     └── HelloWorld.extension2
      ...
      └── esolangN
            ├── esolangN.py
            ├── syntax.md
            └── HelloWorld.extensionN
 ```
 - Inside ```esolangX.py``` file:
   + A string contains extension of HelloWorld file (aka extensionX)
   + A class named ```esolangX```
 - Each language has its own syntax, can be found in its folder
 - ```syntax.md``` contains directory to all esolangs' syntax
 
### Prerequisites :wrench:
- A computer with Python 3.
- No additional package required!
### Usage :gear:
- Open Command Prompt at the interpreter's directory
  - Command: ```main.py [-h] [-l LANG] [-f FILE] [-i CODE] [-e] [--list-languages]```
    + ```--help``` and ```-h```: Show help message
    + ```--list languages```: Display supported languages
    + ```-l``` and ```--lang```: Choose language (Case sensitive!)
    + ```-f``` and ```--file```: Directory to source file
    + ```-i``` and ```--inline```: Interpret code directly
    + ```-e``` and ```--example```: Run example code (from the HelloWorld file)
  - Example:
    + ```main.py -l brainfuck -e```: Run the example Hello World code written in brainfuck
    + ```main.py -l CodeFuck -i="."""Goodbye!""""```: Print "Goodbye" in Codefuck. The original code is ```."Goodbye"``` but you must put it in 3 double-quotes to pass it as an argument. So it becomes: ```."""Goodbye"""```
    + ```main.py -l ABC -f dir\to\file.txt```: Open file at ```dir\to\file``` and interpret
- In Python:
```python
import foo # foo.py (for example) file can be found in languages\foo\

bar = foo.language("YOUR_CODE")
bar.interpret() #start interpreting
```
## Author :pencil2:
- Hoang Le (LetterC67 or LetterC)
