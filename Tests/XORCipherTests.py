import unittest
from cipher import GammaCipher


class TestGammaCipher(unittest.TestCase):
    def setUp(self):
        self.gamma_cipher = GammaCipher()

    def test_generate_key(self):
        text = "Hello"
        key = self.gamma_cipher.generate_key(text)
        self.assertEqual(len(key), len(text))

    def test_eng_g_encrypt(self):
        gamma = "˓ϢϠ͚ZΖǊÏ΀Ñǀ"
        ciphertext = self.gamma_cipher.g_encrypt("Hello World!", gamma)
        self.assertEqual(ciphertext, "ʛ·Ό̶5ζÁƥ½Ϭµǡ")

    def test_eng_g_decrypt(self):
        gamma = "˓ϢϠ͚ZΖǊÏ΀Ñǀ"
        ciphertext = self.gamma_cipher.g_encrypt("ʛ·Ό̶5ζÁƥ½Ϭµǡ", gamma)
        self.assertEqual(ciphertext, "Hello World!")

    def test_ua_g_encrypt(self):
        gamma = "ğ˹ͭȢͩ̑Ƀ΀Ǯ̑Č"
        ciphertext = self.gamma_cipher.g_encrypt("Привіт Світ!", gamma)
        self.assertEqual(ciphertext, "Ԁڹݕؐܿݓɣޡל݇Ӊĭ")

    def test_ua_g_decrypt(self):
        gamma = "ğ˹ͭȢͩ̑Ƀ΀Ǯ̑Č"
        ciphertext = self.gamma_cipher.g_encrypt("Ԁڹݕؐܿݓɣޡל݇Ӊĭ", gamma)
        self.assertEqual(ciphertext, "Привіт Світ!")

    def test_encrypt_decrypt_empty_string(self):
        plaintext = ""
        gamma = "ϞĖ4ʈ"
        ciphertext = self.gamma_cipher.g_encrypt(plaintext, gamma)
        decrypted_text = self.gamma_cipher.g_decrypt(ciphertext, gamma)
        self.assertEqual(plaintext, decrypted_text)


if __name__ == '__main__':
    unittest.main()
