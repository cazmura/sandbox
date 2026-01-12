from closedrange import cr

def test_closedrange1():
    assert cr(2) is not True

def test_closedrange2():
    result, text = cr(5)
    assert result is True
    assert len(text) == 3

def test_closedrange3():
    assert cr(9) is not True
