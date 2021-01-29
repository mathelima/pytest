import sys
sys.path.append('.')
from models.category import Category
import pytest


def test_should_create_category() -> None:
    cat=Category('TEste pytest','teste teste teste teste test')
    assert isinstance(cat,Category)

def test_category_name_empty():
    with pytest.raises(ValueError):
        cat=Category('','teste teste teste teste test')

def test_category_name_len():
    with pytest.raises(ValueError):
        cat=Category('TEste pytest'*200,'teste teste teste teste test')

def test_category_name_int():
    with pytest.raises(TypeError):
        cat=Category(4,'teste teste teste teste test')        
    

def test_description_int():
    with pytest.raises(TypeError):
        cat=Category('dsdsdadasdsa',10)        

def test_description_len():
    with pytest.raises(ValueError):
        cat=Category('TEste pytest','teste teste teste teste test'*300)    
