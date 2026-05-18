import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_circle_area():
    # choice=1, radius=5 -> area = pi*25 = 78.54
    content = open('result1.txt').read()
    print(content)
    regex_test([r'78\.5[0-9]'], content)


@pytest.mark.T2
def test_rectangle_area():
    # choice=2, length=4, width=6 -> area = 24.00
    content = open('result2.txt').read()
    print(content)
    regex_test([r'24\.0[0-9]'], content)


@pytest.mark.T3
def test_triangle_area():
    # choice=3, base=3, height=8 -> area = 12.00
    content = open('result3.txt').read()
    print(content)
    regex_test([r'12\.0[0-9]'], content)


@pytest.mark.T4
def test_invalid_input():
    # choice=0 -> Wrong number
    content = open('result4.txt').read()
    print(content)
    regex_test([r'[Ww]rong'], content)
