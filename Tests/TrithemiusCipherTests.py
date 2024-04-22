import unittest
from cipher import TrithemiusCipher


class TestTrithemiusCipher(unittest.TestCase):
    def setUp(self):
        self.trithemius = TrithemiusCipher()

    def test_linear_ab_eng_encrypt(self):
        A = 5; B = 3
        language = "english"
        operation = "encrypt"
        result = self.trithemius.linear_ab("Hello World!", A, B, language, operation)
        self.assertEqual(result, "kmyckabzgfc!")

    def test_linear_ab_eng_decrypt(self):
        A = 5; B = 3
        language = "english"
        operation = "decrypt"
        result = self.trithemius.linear_ab("kmyckabzgfc!", A, B, language, operation)
        self.assertEqual(result, "hello world!")

    def test_linear_ab_ua_encrypt(self):
        A = 4; B = 7
        language = "ukrainian"
        operation = "encrypt"
        result = self.trithemius.linear_ab("Привіт світ!", A, B, language, operation)
        self.assertEqual(result, "цюхсальтєрб!")

    def test_linear_ab_ua_decrypt(self):
        A = 4; B = 7
        language = "ukrainian"
        operation = "decrypt"
        result = self.trithemius.linear_ab("цюхсальтєрб!", A, B, language, operation)
        self.assertEqual(result, "привіт світ!")

    def test_non_linear_abc_eng_encrypt(self):
        A = 2; B = 5; C = 4
        language = "english"
        operation = "encrypt"
        result = self.trithemius.non_linear_abc("Hello World!", A, B, C, language, operation)
        self.assertEqual(result, "lpgvqyuqago!")

    def test_non_linear_abc_eng_decrypt(self):
        A = 2; B = 5; C = 4
        language = "english"
        operation = "decrypt"
        result = self.trithemius.non_linear_abc("lpgvqyuqago!", A, B, C, language, operation)
        self.assertEqual(result, "hello world!")

    def test_non_linear_abc_ua_encrypt(self):
        A = 1; B = 7; C = 6
        language = "ukrainian"
        operation = "encrypt"
        result = self.trithemius.non_linear_abc("Привіт світ!", A, B, C, language, operation)
        self.assertEqual(result, "хааґчрлуцхш!")

    def test_non_linear_abc_ua_decrypt(self):
        A = 1; B = 7; C = 6
        language = "ukrainian"
        operation = "decrypt"
        result = self.trithemius.non_linear_abc("хааґчрлуцхш!", A, B, C, language, operation)
        self.assertEqual(result, "привіт світ!")

    def test_password_eng_encrypt(self):
        password = "prikol"
        language = "english"
        operation = "encrypt"
        result = self.trithemius.password("Hello World!", password, language, operation)
        self.assertEqual(result, "xwuwcllf ws!")

    def test_password_eng_decrypt(self):
        password = "prikol"
        language = "english"
        operation = "decrypt"
        result = self.trithemius.password("xwuwcllf ws!", password, language, operation)
        self.assertEqual(result, "hello world!")

    def test_password_ua_encrypt(self):
        password = "треш"
        language = "ukrainian"
        operation = "encrypt"
        result = self.trithemius.password("Привіт світ!", password, language, operation)
        self.assertEqual(result, "жєнюаземхящ!")

    def test_password_ua_decrypt(self):
        password = "треш"
        language = "ukrainian"
        operation = "decrypt"
        result = self.trithemius.password("жєнюаземхящ!", password, language, operation)
        self.assertEqual(result, "привіт світ!")


if __name__ == '__main__':
    unittest.main()
