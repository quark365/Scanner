# Scanner

Scanner is a Python module that allows safe evaluation of user input expressions.

## Installation

You can install the Input Evaluator module directly from GitHub using pip:

```bash
pip install git+https://github.com/quark365/Scanner.git
```

## Usage

To use the Scanner module, simply import the `Scanner` function and call it with the expression you want to evaluate:

```python
from Scanner import Scanner

result = Scanner("Enter an expression: ")
print("Result:", result)
```

The `Scanner` function prompts the user to input an expression and evaluates it safely. It returns the result of the evaluated expression.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

