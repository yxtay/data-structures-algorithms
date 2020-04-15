node = {"val": 3, "left": None, "right": None}


def in_order(node):
    if node is not None:
        in_order(node.get("left"))
        print(node["val"])
        in_order(node.get("right"))


def pre_order(node):
    if node is not None:
        print(node["val"])
        pre_order(node.get("left"))
        pre_order(node.get("right"))


def post_order(node):
    if node is not None:
        post_order(node.get("left"))
        post_order(node.get("right"))
        print(node["val"])
