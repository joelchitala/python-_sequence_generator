
import os
import compiler

import subprocess 
def copy_to_clipborad(txt):
    cmd=txt
    return subprocess.check_call(cmd, shell=True)


text = ""
results = []
clear_opcodes = ["clear","cls"]
while text != "exit":
    print("Enter sequence or exit to exit or clear to clear the terminal or copy to copy results to clipboard")
    text = input()
    if clear_opcodes.__contains__(text.lower()):
        os.system('cls||clear')
    
    if text == "exit":
        os.system('cls||clear')
        
    if text != "exit" and clear_opcodes.__contains__(text.lower()) == False:
        print("Enter terms:")
        terms = input()
        print("Enter step size:")
        step = input()
        if not terms and not step:
            print("terms and step can not be empty")
        else:
            print("Results")
            results = compiler.sequenceCompiler().main(text,int(terms),float(step))
            print(results)
