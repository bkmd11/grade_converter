import unittest
import unittest.mock
import sys

from io import StringIO

import grade_calculator


class TestMain(unittest.TestCase):
    def test_main_quits(self):
        with unittest.mock.patch('builtins.input', return_value='q'):
            result = grade_calculator.main()
            self.assertIsNone(result)

    def test_main_takes_input(self):
        result = StringIO()
        sys.stdout = result
        with unittest.mock.patch('builtins.input', side_effect=['3.5', '4.1', 'spam', 'q']):
            grade_calculator.main()

            self.assertEqual(result.getvalue(),
                             '92.0 - copied to clipboard\nDOK grade out of range\nMust be a number!\n')


if __name__ == '__main__':
    unittest.main()
