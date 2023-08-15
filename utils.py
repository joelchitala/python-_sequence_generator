


from array import array
from enum import Enum
import math
from operator import le
from pickle import FALSE, TRUE
from pickletools import opcodes
from re import A
from unittest import result

class OPCODES(Enum):
    EVAL = "EVAL"
    BRKOP = "BRKOP"
    BRKCL = "BRKCL"
    PWR = "PWR"
    DIV = "DIV"
    MUL = "MUL"
    SUB = "SUB"
    ADD = "ADD"
    @classmethod
    def getOpcodes(cls):
        return [x for x in cls]
    
    @classmethod
    def isOpcode(cls,opcode):
        return [x for x in cls].__contains__(opcode)


OPERANDS = ["+","-","*","/","^","(",")"]

def calcPrecidence(decomposed):
    array = []
    index = 0
    for opcode in decomposed:
        match opcode:
            case OPCODES.EVAL:
                array.append({"index":index,"group":0,"OPCODE":opcode})
            case OPCODES.BRKOP:
                array.append({"index":index,"group":1,"OPCODE":opcode})
            case OPCODES.BRKOP:
                array.append({"index":index,"group":1,"OPCODE":opcode})
            case OPCODES.PWR:
                array.append({"index":index,"group":2,"OPCODE":opcode})
            case OPCODES.DIV:
                array.append({"index":index,"group":3,"OPCODE":opcode})
            case OPCODES.MUL:
                array.append({"index":index,"group":3,"OPCODE":opcode})
            case OPCODES.ADD:
                array.append({"index":index,"group":4,"OPCODE":opcode})
            case OPCODES.SUB:
                array.append({"index":index,"group":4,"OPCODE":opcode})
        index += 1
    return array

def getPrecidenceOpcode(opcode):
    match opcode:
        case OPCODES.EVAL:
            return({"group":0,"OPCODE":opcode})
        case OPCODES.BRKOP:
            return({"group":1,"OPCODE":opcode})
        case OPCODES.BRKOP:
            return({"group":1,"OPCODE":opcode})
        case OPCODES.PWR:
            return({"group":2,"OPCODE":opcode})
        case OPCODES.DIV:
            return({"group":3,"OPCODE":opcode})
        case OPCODES.MUL:
            return({"group":3,"OPCODE":opcode})
        case OPCODES.ADD:
            return({"group":4,"OPCODE":opcode})
        case OPCODES.SUB:
            return({"group":4,"OPCODE":opcode})
    return None

def getPrecidenceIndex(array,index):
    for x in array:
        if x["index"] == index:
            return x
    return None

def isSorted(array):
    index = 0
    for x in array:
        if index + 1 != len(array):
            if x > array[index+1]:
                return False
        index += 1
    return True

def sorter(array,reverse=False,distinct=False):
    sorted_array = []

    recurse = 1
    while(recurse > 0):
        temp_array = []
        index = 0
        if len(array) >= 1:
            if len(sorted_array) == 0:
                for element in array:
                    if len(temp_array) > 0:
                        if getLastValue(temp_array) > element:
                            num = temp_array.pop()
                            temp_array.append(element)
                            temp_array.append(num)
                        elif getLastValue(temp_array) < element:
                            temp_array.append(element)
                    else:
                        temp_array.append(element)
                    index += 1
                
                if isSorted(temp_array) == False:
                    recurse = 2
                sorted_array = temp_array
            else:
                temp_array.append(sorted_array[0])
                for element in sorted_array:
                    if getLastValue(temp_array) > element:
                        num = temp_array.pop()
                        temp_array.append(element)
                        temp_array.append(num)
                    elif getLastValue(temp_array) < element:
                        temp_array.append(element)
                    index += 1
            
        if isSorted(temp_array) == False:
            recurse = 2
        sorted_array = temp_array

        recurse -= 1

    distinct_array = []
    if distinct:
        for element in sorted_array:
            if distinct_array.__contains__(element) == False:
                distinct_array.append(element)
        sorted_array = distinct_array

    reverse_array = []
    if reverse:
        index = 1
        for element in sorted_array:
            reverse_array.append(sorted_array[len(sorted_array)-index])
            index += 1
        sorted_array = reverse_array
    return sorted_array

def look_back(array,index):
    if len(array) > 0:
        return array[index-1]
    else:
        return None

def look_forward(array,index):
    if index+1 != len(array):
        return array[index+1]
    else:
        return None

def remove_element(array,index):
    arr = []
    idx = 0
    for x in array:
        if index != idx:
            arr.append(x)
        idx += 1
    return arr

def remove_elements(array,indexes):
    arr = []
    idx = 0
    for x in array:
        if indexes.__contains__(idx) == False:
            arr.append(x)
        idx += 1
    return arr

def execute(num_1,opcode,num_2):
    result = 0
    match opcode:
        case OPCODES.PWR:
            if num_1 >= 0:
                result = math.pow(num_1,num_2)

        case OPCODES.MUL:
            result = num_1 * num_2
        case OPCODES.DIV:
            result = num_1 / num_2
        case OPCODES.ADD:
            result = num_1 + num_2
        case OPCODES.SUB:
            result = num_1 - num_2
    return result

def remove_spaces(string):
    formatted_str = ""
    for token in string:
        if(token != " "):
            formatted_str += token
    return formatted_str

def getLastValue (array):
    if(len(array) > 0):
        return array[len(array)-1]
    else:
        return None

def isEven(number):
    if number%2 == 0:
        return True
    else:
        return False


def parser(string,evaluate = False,term = 1):
    formatted_str = remove_spaces(string)
    formatted_str_len = len(formatted_str)
    parsed_array = []
    index = 0
    num_str = ""
    for token in formatted_str:
        match index:
            case 0:
                if(token == "("):
                    parsed_array.append(OPCODES.BRKOP)
                if(token == "-"):
                        parsed_array.append(OPCODES.SUB)
                if(token == "+"):
                    parsed_array.append(OPCODES.ADD)
                if(token == "n"):
                    if(evaluate):
                        parsed_array.append(term)
                    else:
                        parsed_array.append("n")
                    
                if(token != "n") and (OPERANDS.__contains__(token) == False):
                    num_str += token
            case _:
                if(OPERANDS.__contains__(token)):
                    if(num_str != ""):
                        if evaluate:
                            parsed_array.append(float(num_str))
                        else:
                            parsed_array.append(num_str)
                    num_str = ""
                    if(token == "("):
                        if OPERANDS.__contains__(formatted_str[index-1]) == False:
                            parsed_array.append(OPCODES.MUL)
                        parsed_array.append(OPCODES.BRKOP)

                    if(token == ")"):
                        parsed_array.append(OPCODES.BRKCL)
                        if(index+1 != formatted_str_len):
                            if (OPERANDS.__contains__(formatted_str[index+1]) == False):
                                parsed_array.append(OPCODES.MUL)
                            if formatted_str[index+1] == "(":
                                parsed_array.append(OPCODES.MUL)
                    if(token == "^"):
                        if OPCODES.getOpcodes().__contains__(getLastValue(parsed_array)):
                            parsed_array.pop()
                        parsed_array.append(OPCODES.PWR)

                    if(token == "/"):
                        if OPCODES.getOpcodes().__contains__(getLastValue(parsed_array)):
                            parsed_array.pop()
                        parsed_array.append(OPCODES.DIV)

                    if(token == "*"):
                        if OPCODES.getOpcodes().__contains__(getLastValue(parsed_array)):
                            if getLastValue(parsed_array) != OPCODES.BRKCL:
                                parsed_array.pop()
                        parsed_array.append(OPCODES.MUL)

                    if(token == "-"):
                        if getLastValue(parsed_array) == OPCODES.SUB:
                            parsed_array.pop()
                            if OPCODES.getOpcodes().__contains__(getLastValue(parsed_array)) == False:
                                parsed_array.append(OPCODES.ADD)
                            if getLastValue(parsed_array) == OPCODES.BRKCL:
                                parsed_array.append(OPCODES.ADD)
                        elif getLastValue(parsed_array) == OPCODES.ADD:
                            parsed_array.pop()
                            if OPCODES.getOpcodes().__contains__(getLastValue(parsed_array)) == False:
                                parsed_array.append(OPCODES.SUB)
                            if getLastValue(parsed_array) == OPCODES.BRKCL:
                                parsed_array.append(OPCODES.SUB)
                        else:
                            parsed_array.append(OPCODES.SUB)

                    if(token == "+"):
                        if OPCODES.getOpcodes().__contains__(getLastValue(parsed_array)) == False:
                            parsed_array.append(OPCODES.ADD)
                        if getLastValue(parsed_array) == OPCODES.BRKCL:
                            parsed_array.append(OPCODES.ADD)
                    
                if(token != "n") and (OPERANDS.__contains__(token) == False):
                    num_str += token
                if(token == "n"):
                    if(num_str != ""):
                        parsed_array.append(float(num_str))
                    num_str = ""
                    if(OPERANDS.__contains__(formatted_str[index-1]) == False):
                        parsed_array.append(OPCODES.MUL)
                    if(evaluate):
                        parsed_array.append(term)
                    else:
                        parsed_array.append("n")
        index += 1

    if(num_str != ""):
        if evaluate:
            parsed_array.append(float(num_str))
        else:
            parsed_array.append(num_str)
        num_str = ""

    print(parsed_array)
    return parsed_array


def decomposer(parsed):
    decompose_array = []
    recurse = 1
    index = 0
    idx = 0

    while(recurse > 0):
        temp_array = []
        temp_array_1 = []
        temp_array_2 = []
        brackets = 0
        if len(decompose_array) == 0:
            for opcode in parsed:
                if brackets == 0:
                    if len(temp_array) > 0:
                        index += 1
                        recurse += 1
                        temp_array_1.append(OPCODES.EVAL)
                        temp_array_1.append(index)
                        temp_array_2.append(temp_array)
                        temp_array = []
                    if opcode != OPCODES.BRKOP and OPCODES.BRKCL:
                        temp_array_1.append(opcode)

                if opcode == OPCODES.BRKCL:
                    brackets -= 1

                if brackets > 0:
                    temp_array.append(opcode)
                
                if opcode == OPCODES.BRKOP:
                    brackets += 1
            if len(temp_array) > 0:
                temp_array_2.append(temp_array)
                temp_array = []
                temp_array_1.append(OPCODES.EVAL)
                index += 1
                recurse += 1
                temp_array_1.append(index)
        
            decompose_array.append(temp_array_1)
            temp_array_1 = []

            for arr in temp_array_2:
                if len(arr) > 0:
                    decompose_array.append(arr)
        else:
            temp_array = []
            temp_array_1 = []
            temp_array_2 = []
            brackets = 0
            for opcode in decompose_array[idx]:
                if brackets == 0:
                    if len(temp_array) > 0:
                        index += 1
                        recurse += 1
                        temp_array_1.append(OPCODES.EVAL)
                        temp_array_1.append(index)
                        temp_array_2.append(temp_array)
                        temp_array = []
                    if opcode != OPCODES.BRKOP and OPCODES.BRKCL:
                        temp_array_1.append(opcode)

                if opcode == OPCODES.BRKCL:
                    brackets -= 1

                if brackets > 0:
                    temp_array.append(opcode)
                
                if opcode == OPCODES.BRKOP:
                    brackets += 1
            
            if len(temp_array) > 0:
                temp_array_2.append(temp_array)
                temp_array = []
                temp_array_1.append(OPCODES.EVAL)
                index += 1
                recurse += 1
                temp_array_1.append(index)
            
            decompose_array[idx] = temp_array_1
            temp_array_1 = []

            for arr in temp_array_2:
                if len(arr) > 0:
                    decompose_array.append(arr)
            
        
        idx += 1
        recurse -= 1

    return decompose_array