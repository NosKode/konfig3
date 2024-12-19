import argparse
import json
import re

# Error class for syntax issues
class SyntaxError(Exception):
    pass

def evaluate_postfix(expression):
    """
    Evaluates a postfix mathematical expression.
    Example: "1 2 +" -> 3
    """
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token == '+':
            if len(stack) < 2:
                raise SyntaxError("Invalid postfix expression")
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        else:
            raise SyntaxError(f"Unsupported token in postfix expression: {token}")

    if len(stack) != 1:
        raise SyntaxError("Invalid postfix expression")

    return stack[0]

def process_array(key, array):
    """
    Processes arrays into their computed values and returns a postfix expression or result.
    """
    if all(isinstance(x, (int, float)) for x in array):
        # Replace array with a computed value using postfix calculation
        expression = " ".join(map(str, array)) + " +" * (len(array) - 1)
        result = evaluate_postfix(expression)
        return f"@( {key} {expression} )", result
    else:
        raise SyntaxError(f"Invalid array for key '{key}': {array}")

def process_value(key, value):
    """
    Processes values into the custom configuration format.
    """
    if isinstance(value, list):
        # Convert array to a postfix calculation and compute its value
        postfix_expression, computed_value = process_array(key, value)
        return computed_value
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, str) and re.fullmatch(r"[A-Z]+", value):
        return value
    else:
        raise SyntaxError(f"Invalid value type for key '{key}': {value}")

def parse_json_to_config(json_data):
    """
    Converts JSON data into the custom configuration language format.
    """
    result = []

    for key, value in json_data.items():
        if re.fullmatch(r"[A-Z_]+", key):
            processed_value = process_value(key, value)
            result.append(f"var {key} {processed_value};")
        else:
            raise SyntaxError(f"Invalid key name: {key}")

    return "\n".join(result)

def main():
    parser = argparse.ArgumentParser(description="JSON to custom config language converter.")
    parser.add_argument("--input", required=True, help="Path to the input JSON file.")
    parser.add_argument("--output", required=True, help="Path to the output configuration file.")

    args = parser.parse_args()

    try:
        # Read JSON input
        with open(args.input, "r", encoding="utf-8") as f:
            json_data = json.load(f)

        # Convert JSON to custom config language
        config_data = parse_json_to_config(json_data)

        # Write to output file
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(config_data)

        print("Conversion successful.")
    except (json.JSONDecodeError, SyntaxError) as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
