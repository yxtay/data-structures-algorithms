import operator

OPERATORS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
LEFT_PAREN = "("
RIGHT_PAREN = ")"


def build_parse_tree(expression):
    tree = {}
    stack = [tree]
    node = tree
    for token in expression:
        if token == LEFT_PAREN:
            node["left"] = {}
            stack.append(node)
            node = node["left"]
        elif token == RIGHT_PAREN:
            node = stack.pop()
        elif token in OPERATORS:
            node["val"] = token
            node["right"] = {}
            stack.append(node)
            node = node["right"]
        else:
            node["val"] = int(token)
            parent = stack.pop()
            node = parent
    return tree


def evaluate(tree):
    try:
        operate = OPERATORS[tree["val"]]
        return operate(evaluate(tree["left"]), evaluate(tree["right"]))
    except KeyError:
        # no left or no right, so is a leaf - our base case
        return tree["val"]


def construct_expression(parse_tree):
    if parse_tree is None:
        return ""

    left = construct_expression(parse_tree.get("left"))
    right = construct_expression(parse_tree.get("right"))
    val = parse_tree["val"]

    if left and right:
        return "({}{}{})".format(left, val, right)

    return val
