import unittest
from cipher import CaesarCipher


class TestCaesarCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = CaesarCipher()

    def test_eng_code(self):
        result = self.cipher.eng_code("HELLO", 3)
        self.assertEqual(result, "khoor")

    def test_eng_code_decrypt(self):
        result = self.cipher.eng_code_decrypt("KHOOR", 3)
        self.assertEqual(result, "hello")

    def test_ua_code(self):
        result = self.cipher.ua_code("ПРИВІТ", 5)
        self.assertEqual(result, "фхлємч")

    def test_ua_code_decrypt(self):
        result = self.cipher.ua_code_decrypt("ааа гг нг ка", 10)
        self.assertEqual(result, "фффуччуєчуґф")

    def test_eng_encrypt(self):
        result = self.cipher.eng_encrypt("aaa bb c/d", 5)
        self.assertEqual(result, "fffeggeh/i")

    def test_eng_decrypt(self):
        result = self.cipher.eng_decrypt("korop", 6)
        self.assertEqual(result, "eilij")

    def test_ua_encrypt(self):
        result = self.cipher.ua_encrypt("Слава Україні!", 24)
        self.assertEqual(result, "ідфцфуйґифвєб!")

    def test_ua_decrypt(self):
        result = self.cipher.ua_decrypt("Шьж’ксщемзйчфйффдехшхжншщхеєжхеайчймеьцхзфхзєлйфьефнуехшхжьецхїєкеїхешьж’ксщєефєїєффдеєїуофошщчєщнзфхпецхштьинецхзфнрецєсйщеїхсьуйфщозеьецєцйчхзхуьеєжхе нючхзхуье(ьемєшщхшьфсьеЇод)езнитдїо,ефйхжяоїфняеїтдехщчнуєффдеєїуофошщчєщнзфхпецхштьин", 7)
        self.assertEqual(result, "суб’єкт звернення особисто або через уповноважену ним особу подає до суб’єкта надання адміністративної послуги повний пакет документів у паперовому або цифровому (у застосунку дія) вигляді, необхідних для отримання адміністративної послуги")


if __name__ == '__main__':
    unittest.main()
