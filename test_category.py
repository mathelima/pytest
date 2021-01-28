from category import Category

name = "Eletrodomésticos"
description = "Categoria de eletrodomésticos"


def test_should_create_category() -> None:
    category = Category(name, description)
    assert isinstance(category, Category)
    assert category.name == name
    assert isinstance(category.name, str)
    assert category.description == description
    assert isinstance(category.description, str)


def test_validate_name_type() -> None:
    try:
        category = Category(1, description)
    except Exception as e:
        assert isinstance(e, TypeError)


def test_validate_nullable_name():
    try:
        category = Category('', description)
    except Exception as e:
        assert isinstance(e, ValueError)


def test_validate_description_type() -> None:
    try:
        category = Category(name, 1)
    except Exception as e:
        assert isinstance(e, TypeError)
