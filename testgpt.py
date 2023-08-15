import math

OPERATORS = {
    '+': (1, lambda x, y: x + y),
    '-': (1, lambda x, y: x - y),
    '*': (2, lambda x, y: x * y),
    '/': (2, lambda x, y: x / y),
    '^': (3, lambda x, y: x ** y),
}

def evaluate_expression(expression):
    postfix = infix_to_postfix(expression)
    result = evaluate_postfix(postfix)
    return result

# def infix_to_postfix(expression):
#     postfix = []
#     operator_stack = []
#     for token in expression:
#         if token.isdigit():
#             postfix.append(float(token))
#         elif token in OPERATORS:
#             while operator_stack and operator_stack[-1] != '(' and OPERATORS[token][0] <= OPERATORS[operator_stack[-1]][0]:
#                 postfix.append(operator_stack.pop())
#             operator_stack.append(token)
#         elif token == '(':
#             operator_stack.append(token)
#         elif token == ')':
#             while operator_stack and operator_stack[-1] != '(':
#                 postfix.append(operator_stack.pop())
#             if operator_stack and operator_stack[-1] == '(':
#                 operator_stack.pop()
#     while operator_stack:
#         postfix.append(operator_stack.pop())
#     return postfix



def evaluate_postfix(postfix):
    print(postfix)
    operand_stack = []
    for token in postfix:
        if isinstance(token, float):
            operand_stack.append(token)
        elif token in OPERATORS:
            op2 = operand_stack.pop()
            op1 = operand_stack.pop()
            result = OPERATORS[token][1](op1, op2)
            print(op2)
            print(op1)
            print(result)
            operand_stack.append(result)
    return operand_stack[0] if operand_stack else None


# def infix_to_postfix(expression):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

    postfix = []
    operator_stack = []

    def has_higher_precedence(op1, op2):
        return precedence[op1] >= precedence[op2]

    for token in expression:
        if token.isdigit():
            postfix.append(token)
        elif token in precedence:
            while (
                operator_stack and
                operator_stack[-1] != "(" and
                has_higher_precedence(operator_stack[-1], token)
            ):
                postfix.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            while operator_stack and operator_stack[-1] != "(":
                postfix.append(operator_stack.pop())
            if operator_stack and operator_stack[-1] == "(":
                operator_stack.pop()

    while operator_stack:
        postfix.append(operator_stack.pop())

    return postfix


def infix_to_postfix(expression):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

    postfix = []
    operator_stack = []

    def has_higher_precedence(op1, op2):
        return precedence[op1] >= precedence[op2]

    i = 0
    while i < len(expression):
        token = expression[i]

        if token.isdigit():
            postfix.append(token)
        elif token in precedence:
            while (
                operator_stack and
                operator_stack[-1] != "(" and
                has_higher_precedence(operator_stack[-1], token)
            ):
                postfix.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            while operator_stack and operator_stack[-1] != "(":
                postfix.append(operator_stack.pop())
            if operator_stack and operator_stack[-1] == "(":
                operator_stack.pop()

        i += 1

    while operator_stack:
        postfix.append(operator_stack.pop())

    return postfix

print(evaluate_expression("(2)(3)"))