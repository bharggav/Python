import pytest
import time
from Pytesting.code import learningtest as test1
print(time.time())

def testadd():
    assert test1.add(1,2) == 3

def testsub():
    assert test1.sub(2,1) == 1
def testmul():
    assert test1.mul(2,3) == 6
def testdiv():
    assert test1.div(6,2) == 3 # Fixed 'dev' to 'div'
def testdiv_zero():
    with pytest.raises(ValueError):
        test1.div(1,0)
