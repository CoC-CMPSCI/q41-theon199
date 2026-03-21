import pytest
import re

def regex_test(expected, lines):
    i = 0 ; match = 0
    for token in expected:
        for j in range(i, len(lines)):
            res = re.search(token, lines[j])
            if res is not None:
                i = j + 1
                match += 1
                break
        else:
            print(f'\033[91m Not Found: {token} \033[0m')
            assert False, f'Expect: {expected}'
    else:
        print(f'\033[91m match count: {match} \033[0m')
        assert match == len(expected), f'Expect: {expected}'


@pytest.mark.T1
def test_circle_area():
    # choice=1, radius=5 -> area = pi*25 = 78.54
    with open('result1.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'78\.5[0-9]'], lines)


@pytest.mark.T2
def test_rectangle_area():
    # choice=2, length=4, width=6 -> area = 24.00
    with open('result2.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'24\.0[0-9]'], lines)


@pytest.mark.T3
def test_triangle_area():
    # choice=3, base=3, height=8 -> area = 12.00
    with open('result3.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'12\.0[0-9]'], lines)


@pytest.mark.T4
def test_invalid_input():
    # choice=0 -> Wrong number
    with open('result4.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'[Ww]rong'], lines)
