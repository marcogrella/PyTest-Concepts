import pytest


def test_first_test_program():
    message = "Hello"
    assert message == "Hello", f"condition of {message} not passed "


@pytest.mark.smoke
def test_second_test_program():
    a = 3
    b = 7
    assert a + b == 10, f"Addition not satisfied"