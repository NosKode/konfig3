import unittest
from main import parse_json_to_config, SyntaxError, evaluate_postfix

class TestJsonToConfig(unittest.TestCase):
    def test_valid_simple(self):
        """Тест простого присваивания константы."""
        data = {"CONST": 100}
        result = parse_json_to_config(data)
        expected = "var CONST 100;"
        self.assertEqual(result.strip(), expected)

    def test_valid_array_to_postfix(self):
        """Тест преобразования массива в постфиксное выражение."""
        data = {"ARRAY": [1, 2, 3]}
        result = parse_json_to_config(data)
        expected = "var ARRAY @( ARRAY 1 2 3 + );"
        self.assertEqual(result.strip(), expected)

    def test_invalid_key(self):
        """Тест недопустимого имени ключа."""
        data = {"invalid": 100}
        with self.assertRaises(SyntaxError):
            parse_json_to_config(data)

    def test_invalid_value(self):
        """Тест недопустимого типа значения."""
        data = {"CONST": {"nested": 123}}
        with self.assertRaises(SyntaxError):
            parse_json_to_config(data)

    def test_evaluate_postfix_simple(self):
        """Тест вычисления простого постфиксного выражения."""
        expression = "1 2 +"
        result = evaluate_postfix(expression)
        self.assertEqual(result, 3)

    def test_evaluate_postfix_invalid(self):
        """Тест недопустимого постфиксного выражения."""
        expression = "1 +"
        with self.assertRaises(SyntaxError):
            evaluate_postfix(expression)

    def test_evaluate_postfix_unsupported_token(self):
        """Тест постфиксного выражения с неподдерживаемым токеном."""
        expression = "1 2 *"
        with self.assertRaises(SyntaxError):
            evaluate_postfix(expression)

if __name__ == "__main__":
    unittest.main()
