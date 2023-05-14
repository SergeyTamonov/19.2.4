import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
     self.calc = Calculator

    def test_adding_correctly(self):
        assert self.calc.adding(self, 2, 2) == 4

    def test_multiply_correctly(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division_correctly(self):
        assert self.calc.division(self, 27, 3) == 9

    def test_subtraction_correctly(self):
        assert self.calc.subtraction(self, 27, 3) == 24

    def teardown(self):
        print("Выполнение метода Teardown")