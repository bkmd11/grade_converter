import unittest
import unittest.mock

import grade_calculator


class TestMain(unittest.TestCase):
    def test_main_quits(self):
        with unittest.mock.patch('builtins.input', return_value='q'):
            result = grade_calculator.main()
            self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
