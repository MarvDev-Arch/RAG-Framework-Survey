from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception:
        return "Invalid calculation"

result = calculator.invoke({"expression": "25 * 4"})

print("Calculator Tool Test")
print("Input: 25 * 4")
print("Result:", result)