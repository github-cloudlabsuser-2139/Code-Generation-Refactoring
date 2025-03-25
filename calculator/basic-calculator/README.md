# Basic Calculator

This is a simple calculator application that performs basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features

- Addition
- Subtraction
- Multiplication
- Division

## Installation

To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

To use the calculator, you can import the `Calculator` class from the `src/calculator.py` file and create an instance of it. Here is an example:

```python
from src.calculator import Calculator

calc = Calculator()
result = calc.add(5, 3)
print(result)  # Output: 8
```

## Running Tests

To run the unit tests for the calculator, you can use the following command:

```
pytest tests/test_calculator.py
```

Make sure you have `pytest` installed as a dependency.

## License

This project is licensed under the MIT License.