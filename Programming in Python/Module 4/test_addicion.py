import addition
import pytest

def test_add():
    assert addition.add(4,5) == 9
    
def test_sub():
    assert addition.sub(5,4) == 1