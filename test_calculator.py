import calculator
import sys
import pytest


def test_add(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "2", "3", "add"])
    assert calculator.calculate(2, 3, "add") == 5
# Add more functional tests for subtract, multiply, and divide


def test_substract(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "5", "4", "subtract"])
    assert calculator.calculate(5, 4, "subtract") == 1


def test_divide(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "24", "4", "divide"])
    assert calculator.calculate(24, 4, "divide") == 6


def test_multiply(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "12", "2", "multiply"])
    assert calculator.calculate(12, 2, "divide") == 6


def test_terminal_output(capsys):
    print(f"Result: {calculator.calculate(10, 2, 'multiply')}")
    captured = capsys.readouterr()
    assert captured.out == "Result: 20\n"


def test_argument_passing(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["calculator.py", "6", "2", "divide"])
    calculator.main()
    captured = capsys.readouterr()
    assert captured.out == "Result: 3.0\n"


def test_dividing_zero(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["calculator.py", "3", "0", "divide"])

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.calculate(3, 0, "divide")
