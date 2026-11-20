# from file_name import class_name
import pytest

from employee import Employee


def test_give_default_raise(employee):

    # store the expected for later
    expected_annual = employee.annual + 5000
    # change the local var of annual in employee
    employee.give_raise()
    assert employee.annual == expected_annual


def test_give_custom_raise(employee):
    custom_raise = 10_000

    expected_annual = employee.annual + custom_raise
    employee.give_raise(custom_raise)

    assert employee.annual == expected_annual


@pytest.fixture
def employee():
    return Employee("Armand", "Soto", 60_000)


if __name__ == "__main__":
    test_give_default_raise()
