import argparse
import sys, os
import importlib

def getClass(module, _class):
    module = importlib.import_module(module)
    _class = getattr(module, _class)
    return _class

parser = argparse.ArgumentParser(description='Esolangs Interpreter by C67', formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=30))
parser.add_argument("-l", "--lang", dest = "lang", help = "choose language")
parser.add_argument("-f", "--file", dest = "file", help = "interpret code from file")
parser.add_argument("-i", "--inline", dest = "code", help = "interpret code directly")
parser.add_argument("-e", "--example", action = "store_true", dest = "example", help = "run example")
parser.add_argument("--list-languages", action = "store_true", dest = "ll", help = "show supported languages")

args = parser.parse_args()
code = ""
supportedLang = [dI for dI in os.listdir('languages\.') if os.path.isdir(os.path.join('languages\.',dI))]

if args.ll:
    print("Supported Languages: ")
    supportedLang = [dI for dI in os.listdir('languages\.') if os.path.isdir(os.path.join('languages\.',dI))]
    for lang in supportedLang:
        print(" -", lang)
        
elif args.lang == None:
    sys.exit("Please specify your language!")
    
elif args.lang:
    if args.lang not in supportedLang:
        sys.exit("Language not suppported!")
        
    print("Selected language: " + args.lang)

    _dir = "languages" + '/' + args.lang
    sys.path.append(_dir)

    lang = __import__(args.lang)
    
    if args.example:
        try:
            print(" - HelloWorld program from: languages\\" + args.lang + "\\HelloWorld" + lang.extension + '\n')
            with open("languages\\" + args.lang + "\\HelloWorld" + lang.extension) as FILE:
                code = FILE.read()
            print(" - Input: \n", code, '\n')
        except:
            sys.exit("Error running example!")
            
    elif args.code:
        code = args.code
        
    elif args.file:
        try:
            with open(args.file) as FILE:
                code = FILE.read()
        except:
            sys.exit("Error opening file!")
        print(' - Code from: ' + args.file)

    print(" - Output:")
    obj = getClass(args.lang, args.lang)(code)
    obj.interpret()

