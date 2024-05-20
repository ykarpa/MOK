import unittest

from cipher import KnapsackCipher


class TestKnapsackCipher(unittest.TestCase):
    def test_n_getter_setter(self):
        cipher = KnapsackCipher()
        cipher.n = 50
        expected = 50
        actual = cipher.n
        self.assertEqual(expected, actual)

    def test_m_getter_setter(self):
        cipher = KnapsackCipher()
        cipher.m = 50
        expected = 50
        actual = cipher.m
        self.assertEqual(expected, actual)

    def test_encrypt_decrypt(self):
        cipher = KnapsackCipher()
        cipher.private_key = [1, 2, 3]
        expected = [1, 2, 3]
        actual = cipher.private_key
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
