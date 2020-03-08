import unittest
import grade_calculator


class TestGradeRange(unittest.TestCase):
    def test_pd_upper_limit(self):
        result = grade_calculator.grade_converter(4)
        self.assertEqual(result, 100)

    def test_pd_lower_limit(self):
        result = grade_calculator.grade_converter(3.5)
        self.assertEqual(result, 92)

    def test_p_upper_limit(self):
        result = grade_calculator.grade_converter(3.4)
        self.assertEqual(result, 91)

    def test_p_lower_limit(self):
        result = grade_calculator.grade_converter(2.5)
        self.assertEqual(result, 76)

    def test_bp_upper_limit(self):
        result = grade_calculator.grade_converter(2.4)
        self.assertEqual(result, 75)

    def test_bp_lower_limit(self):
        result = grade_calculator.grade_converter(2)
        self.assertEqual(result, 66)

    def test_i_upper_limit(self):
        result = grade_calculator.grade_converter(1.9)
        self.assertEqual(result, 65)

    def test_i_lower_limit(self):
        result = grade_calculator.grade_converter(1.5)
        self.assertEqual(result, 55)

    def test_n_upper_limit(self):
        result = grade_calculator.grade_converter(1.4)
        self.assertEqual(result, 54)

    def test_n_lower_limit(self):
        result = grade_calculator.grade_converter(0)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
