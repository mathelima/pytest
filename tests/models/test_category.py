import sys
sys.path.append('.')
from models.category import Category
import pytest


class TestCategoryModel:
    @pytest.mark.parametrize("name, description", [
        ('N', ''),
        ('N' * 100, 'D' * 200),
        ('N' * 50, 'D' * 120)
    ])
    def test_category_instance(self, name, description):
        category = Category(name, description)
        assert isinstance(category, Category)

    def test_name_min_len(self):
        name = 'C'
        description = ''
        category = Category(name, description)
        assert category.name is name

    def test_name_not_none(self):
        with pytest.raises(TypeError):
            category = Category(None, 'Teste descricao de categoria')

    @pytest.mark.parametrize("name, description", [
        (10, 'Teste descricao de categoria'),
        (10.5, 'Teste descricao de categoria'),
        (False, 'Teste descricao de categoria')
    ])
    def test_name_not_str(self, name, description):
        with pytest.raises(TypeError):
            category = Category(name, description)

    def test_name_not_empty(self):
        with pytest.raises(ValueError):
            category = Category('', 'Teste descricao de categoria')

    def test_name_max_len(self):
        with pytest.raises(ValueError):
            category = Category('Teste Categoria' * 51, 'Teste descricao de categoria')

    def test_description_min_len(self):
        name = 'C'
        description = ''
        category = Category(name, description)
        assert category.description is description

    def test_description_not_none(self):
        with pytest.raises(TypeError):
            category = Category('Teste Categoria', None)

    def test_description_not_str(self):
        with pytest.raises(TypeError):
            category = Category('Teste Categoria', 10)

    def test_description_len(self):
        with pytest.raises(ValueError):
            category = Category('Teste Categoria', 'c' * 256)
