import pytest
import time
from Pytesting.code import learningtest as test1
print(time.time())

def testadd():
    assert test1.add(1,2) == 3

