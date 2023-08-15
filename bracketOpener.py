from unittest import skip
import utils

def bracket_traversal(equation):
    parsed_array = utils.parser(equation)
    decomposed_array = utils.decomposer(parsed_array)
    multiplex_array = []

    print(decomposed_array)
    

        
    return multiplex_array
   



def multiplexer(equation):
    multiplex_array = bracket_traversal(equation)
    print(multiplex_array)

multiplexer("n(n+x)")
