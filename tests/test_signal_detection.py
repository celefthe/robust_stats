import unittest
from robust_stats.signal_detection import signal_detection


class TestSignalDetection(unittest.TestCase):
    def setUp(self):
        self.calculated = signal_detection(20, 20, 18, 14)
        self.expected = {
            'beta': 0.5047513946658048,
            'c': -0.90297603912632052,
            'c_prime': -1.1925969537299699,
            'correct_rejections': 6,
            'd_prime': 0.7571510528365597,
            'misses': 2,
            'z_false': 0.52440051270804067,
            'z_hits': 1.2815515655446004
        }

    def test_d_prime(self):
        self.compare('d_prime')

    def test_c(self):
        self.compare('c')

    def test_c_prime(self):
        self.compare('c_prime')

    def test_correct_rejections(self):
        self.compare('correct_rejections')

    def test_misses(self):
        self.compare('misses')

    def test_beta(self):
        self.compare('beta')

    def test_z_false(self):
        self.compare('z_false')

    def test_z_hits(self):
        self.compare('z_hits')

    def compare(self, value):
        """
        Compare expected value with calculated values
        """
        return self.assertAlmostEqual(
            self.calculated[value],
            self.expected[value],
            places=4
        )


if __name__ == '__main__':
    unittest.main()
