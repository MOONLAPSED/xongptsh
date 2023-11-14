import unittest
from unittest.mock import patch
from bracks import test_processing_function


class TestBracks(unittest.TestCase):
    @patch("bracks.process_custom_syntax")
    def test_processing_function(self, mock_process_custom_syntax):
        # Define the behavior of the mock function
        mock_process_custom_syntax.side_effect = lambda text, context: text.format(
            **context
        )

        # Define a context dictionary for testing
        context = {
            "placeholder1": "value1",
            "placeholder2": "value2",
            "placeholder3": "value3",
        }

        # Call the function to test
        test_processing_function(context)

        # Verify that the mock function was called the correct number of times
        self.assertEqual(mock_process_custom_syntax.call_count, 2)

        # Define an empty context dictionary for testing
        context = {}

        # Call the function to test
        test_processing_function(context)

        # Verify that the mock function was called the correct number of times
        self.assertEqual(mock_process_custom_syntax.call_count, 2)

        # Verify that the mock function was called with the correct arguments
        calls = [
            call("This is a {placeholder1} and {placeholder2} example.", context),
            call("Another {placeholder3} example.", context),
        ]
        mock_process_custom_syntax.assert_has_calls(calls)

        # Verify that the processed text is equal to the original text (placeholders are not replaced)
        self.assertEqual(
            mock_process_custom_syntax.return_value,
            "This is a {placeholder1} and {placeholder2} example.",
        )
        self.assertEqual(
            mock_process_custom_syntax.return_value, "Another {placeholder3} example."
        )

        # Define a context dictionary for testing
        context = {"placeholder1": "value1", "placeholder2": "value2"}

        # Call the function to test
        test_processing_function(context)

        # Verify that the mock function was called the correct number of times
        self.assertEqual(mock_process_custom_syntax.call_count, 2)

        # Verify that the mock function was called with the correct arguments
        calls = [
            call("This is a {placeholder1} and {placeholder2} example.", context),
            call("Another {placeholder3} example.", context),
        ]
        mock_process_custom_syntax.assert_has_calls(calls)

        # Verify that the processed text is equal to the original text with placeholders replaced
        self.assertEqual(
            mock_process_custom_syntax.return_value,
            "This is a value1 and value2 example.",
        )
        self.assertEqual(
            mock_process_custom_syntax.return_value, "Another {placeholder3} example."
        )

        # Define a context dictionary for testing
        context = {
            "placeholder1": "value1",
            "placeholder2": "value2",
            "placeholder3": "value3",
            "additional_placeholder": "additional_value",
        }

        # Call the function to test
        test_processing_function(context)

        # Verify that the mock function was called the correct number of times
        self.assertEqual(mock_process_custom_syntax.call_count, 2)

        # Verify that the mock function was called with the correct arguments
        calls = [
            call("This is a {placeholder1} and {placeholder2} example.", context),
            call("Another {placeholder3} example.", context),
        ]
        mock_process_custom_syntax.assert_has_calls(calls)

        # Verify that the processed text is equal to the original text with placeholders replaced
        self.assertEqual(
            mock_process_custom_syntax.return_value,
            "This is a value1 and value2 example.",
        )
        self.assertEqual(
            mock_process_custom_syntax.return_value, "Another value3 example."
        )

        # Define a context dictionary for testing
        context = {"placeholder1": 123, "placeholder2": 456, "placeholder3": 789}

        # Call the function to test
        test_processing_function(context)

        # Verify that the mock function was called the correct number of times
        self.assertEqual(mock_process_custom_syntax.call_count, 2)

        # Verify that the mock function was called with the correct arguments
        calls = [
            call("This is a {placeholder1} and {placeholder2} example.", context),
            call("Another {placeholder3} example.", context),
        ]
        mock_process_custom_syntax.assert_has_calls(calls)

        # Verify that the processed text is equal to the original text with placeholders replaced
        self.assertEqual(
            mock_process_custom_syntax.return_value, "This is a 123 and 456 example."
        )
        self.assertEqual(
            mock_process_custom_syntax.return_value, "Another 789 example."
        )

        # Define a context dictionary for testing
        context = {
            "placeholder1": "value1",
            "placeholder2": "value2",
            "placeholder3": "value3",
        }

        # Define a test case with no placeholders
        test_case = {
            "text": "This is a test with no placeholders.",
            "expected_result": "This is a test with no placeholders.",
        }

        # Call processing function with test case
        processed_text = process_custom_syntax(test_case["text"], context)

        # Verify that the mock function was called once
        self.assertEqual(mock_process_custom_syntax.call_count, 1)

        # Verify that the mock function was called with the correct arguments
        mock_process_custom_syntax.assert_called_with(test_case["text"], context)

        # Verify that the processed text is equal to the original text (no placeholders to replace)
        self.assertEqual(
            mock_process_custom_syntax.return_value, test_case["expected_result"]
        )

        # Define a context dictionary for testing
        context = {
            "placeholder1": "value1",
            "placeholder2": "value2",
            "placeholder3": "value3",
        }

        # Define a test case with empty text
        test_case = {"text": "", "expected_result": ""}

        # Call processing function with test case
        processed_text = process_custom_syntax(test_case["text"], context)

        # Verify that the mock function was called once
        self.assertEqual(mock_process_custom_syntax.call_count, 1)

        # Verify that the mock function was called with the correct arguments
        mock_process_custom_syntax.assert_called_with(test_case["text"], context)

        # Verify that the processed text is equal to the original text (no placeholders to replace)
        self.assertEqual(
            mock_process_custom_syntax.return_value, test_case["expected_result"]
        )


if __name__ == "__main__":
    unittest.main()
