import operator

PRECEDENCE = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

OPERATION = {"*": operator.mul, "/": operator.truediv, "-": operator.sub, "+": operator.add}

CHARACTERS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITS = set("0123456789")
LEFT_PAREN = "("
RIGHT_PAREN = ")"


def to_postfix(infix_expression):
    operation_stack = []
    postfix = []
    tokens = infix_expression.split()

    for token in tokens:
        if token in CHARACTERS or token in DIGITS:
            postfix.append(token)
        elif token == LEFT_PAREN:
            operation_stack.append(token)
        elif token == RIGHT_PAREN:
            top_token = operation_stack.pop()
            while top_token != LEFT_PAREN:
                postfix.append(top_token)
                top_token = operation_stack.pop()
        else:
            while operation_stack and (PRECEDENCE[operation_stack[-1]] >= PRECEDENCE[token]):
                postfix.append(operation_stack.pop())
            operation_stack.append(token)

    while operation_stack:
        postfix.append(operation_stack.pop())
    return " ".join(postfix)


def evaluate_postfix(postfix_expression):
    operand_stack = []

    for token in postfix_expression.split():
        if token in DIGITS:
            operand_stack.append(int(token))
        else:
            b = operand_stack.pop()
            a = operand_stack.pop()
            result = OPERATION[token](a, b)
            operand_stack.append(result)
    return operand_stack.pop()
