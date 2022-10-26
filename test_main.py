import main
import pytest

# start with test-prefix before all the funciton!

# @pytest.mark.number


def test_add():
    assert main.add(7, 3) == 10
    assert main.add(8) == 10

# @pytest.mark.number


def test_product():
    assert main.product(2, 2) == 4
    assert main.product(7) == 14

# @pytest.mark.string


def test_add_strings():
    result = main.add("Hello", 'World')
    assert result == "HelloWorld"
    assert type(result) is str
    assert 'Helod' not in result
