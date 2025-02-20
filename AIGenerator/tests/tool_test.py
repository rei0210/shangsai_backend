import os
import unittest
import json

import django

from AIGenerator.tools import parse_question

# Import the function from your module

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shangsai_backend.settings")  # 替换 'myproject' 为你的 Django 项目名
django.setup()

class TestMCQParser(unittest.TestCase):

    def test_valid_mcq(self):
        """Test a valid multiple-choice question format."""
        mcq_text = '''How do you feel about the course?
                      A) Excellent
                      B) Good
                      C) Average
                      D) other(please specify)'''

        expected_output = {
            "question_id":0,
            "text": "How do you feel about the course?",
            "choices": [
                {"choice_id": "A", "text": "Excellent", "need_fill": False},
                {"choice_id": "B", "text": "Good", "need_fill": False},
                {"choice_id": "C", "text": "Average", "need_fill": False},
                {"choice_id": "D", "text": "other(please specify)", "need_fill": True}
            ]
        }

        # Run the function and convert output JSON string to a Python dictionary
        print(parse_question(mcq_text))
        self.assertEqual(expected_output, parse_question(mcq_text))
        result = json.loads(parse_question(mcq_text))

        # Compare expected and actual output
        self.assertEqual(result, expected_output)

    # def test_missing_choices(self):
    #     """Test when no choices are provided."""
    #     mcq_text = '"How do you feel about the course?"'  # Only question, no choices
    #
    #     with self.assertRaises(ValueError):  # Expecting a ValueError
    #         parse_question(mcq_text)
    #
    # def test_invalid_format(self):
    #     """Test an incorrectly formatted question."""
    #     mcq_text = '''"How do you feel about the course?"
    #                   "1) Great"
    #                   "2) Not Bad"
    #                   "3) Terrible"'''  # Choices should be A), B), etc.
    #
    #     with self.assertRaises(ValueError):  # Expecting a ValueError
    #         parse_question(mcq_text)
    #
    # def test_extra_whitespace(self):
    #     """Test handling of extra spaces and newline characters."""
    #     mcq_text = ''' "How do you feel about the course?"
    #                    "A)  Excellent   "
    #                    "B)  Good  "
    #                    "C)   Average"
    #                    "D) other(please specify)  " '''
    #
    #     expected_output = {
    #         "question_text": "How do you feel about the course?",
    #         "choices": [
    #             {"choice_id": "A", "text": "Excellent", "is_other": False},
    #             {"choice_id": "B", "text": "Good", "is_other": False},
    #             {"choice_id": "C", "text": "Average", "is_other": False},
    #             {"choice_id": "D", "text": "other(please specify)", "is_other": True}
    #         ]
    #     }
    #
    #     result = json.loads(parse_question(mcq_text))
    #     self.assertEqual(result, expected_output)


# if __name__ == "__main__":
#     unittest.main()
