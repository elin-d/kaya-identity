import unittest

from compute import compute_kaya_identity


class TestKID(unittest.TestCase):

    def test_calc(self):
        self.assertEqual(compute_kaya_identity(1, 1, 1, 1), 1, "Should be 1")

    def test_negative_intensity(self):
        compute_kaya_identity(1, 1, 1, -1)
        compute_kaya_identity(1, 1, -1, 1)
        pass

    def test_negative_population(self):
        with self.assertRaises(ValueError):
            compute_kaya_identity(-1, 1, 1, 1)

    def test_negative_gdp(self):
        with self.assertRaises(ValueError):
            compute_kaya_identity(1, -1, 1, 1)

    def test_string_as_input(self):
        with self.assertRaises(TypeError):
            compute_kaya_identity("1", "1", "1", "1")


if __name__ == '__main__':
    unittest.main()
