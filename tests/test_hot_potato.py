from src.hot_potato import hot_potato


def test():
    names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    result = hot_potato(names, 9)
    assert result == "David"
