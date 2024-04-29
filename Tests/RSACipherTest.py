import unittest
from cipher import RSACipher


class TestRSACipher(unittest.TestCase):
    def setUp(self):
        self.rsa = RSACipher()

    def test_rsa_encrypt(self):
        public_key = (3, 9173503)
        text = "111111"
        self.assertEqual(self.rsa.rsa_encrypt(public_key, text), 4051753)

    def test_rsa_decrypt(self):
        private_key = (6111579, 9173503)
        ciphertext = 4051753
        self.assertEqual(self.rsa.rsa_decrypt(private_key, ciphertext), "111111")


if __name__ == '__main__':
    unittest.main()
