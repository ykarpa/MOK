import unittest
from cipher import Key_Exchange_DH


class TestDiffieHellman(unittest.TestCase):
    def setUp(self):
        self.dh = Key_Exchange_DH()

    def test_generate_key_pair(self):
        p = 23; g = 5
        private_key = 4
        public_key, private_key = self.dh.generate_key_pair(p, g, private_key)
        self.assertEqual(public_key, 4)

    def test_exchange_keys(self):
        p = 23
        public_key, private_key = 10, 4
        s = self.dh.exchange_keys(p, public_key, private_key)
        self.assertEqual(s, 18)


if __name__ == '__main__':
    unittest.main()
