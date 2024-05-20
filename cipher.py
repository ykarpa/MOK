import random
from math import gcd


class CaesarCipher:
    ENG_LETTERS = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    UA_LETTERS = " АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"

    @staticmethod
    def shift_text(text, k, letters):
        letter_qty = len(letters)
        result = ""

        for char in text:

            index = letters.find(char.upper())
            if index < 0:
                result += char
            else:
                code_index = (index + k) % letter_qty
                result += letters[code_index].lower()

        return result

    def eng_code(self, text, k):
        return self.shift_text(text, k, self.ENG_LETTERS)

    def eng_code_decrypt(self, text, k):
        return self.shift_text(text, -k, self.ENG_LETTERS)

    def ua_code(self, text, k):
        return self.shift_text(text, k, self.UA_LETTERS)

    def ua_code_decrypt(self, text, k):
        return self.shift_text(text, -k, self.UA_LETTERS)

    def eng_encrypt(self, plain_message, key):
        return self.eng_code(plain_message, key)

    def eng_decrypt(self, encrypted_message, key):
        return self.eng_code_decrypt(encrypted_message, key)

    def ua_encrypt(self, plain_message, key):
        return self.ua_code(plain_message, key)

    def ua_decrypt(self, encrypted_message, key):
        return self.ua_code_decrypt(encrypted_message, key)


class TrithemiusCipher:
    ENG_LETTERS = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    UKR_LETTERS = " АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"

    def linear_ab(self, text, A, B, language, operation):
        if language == "english":
            alphabet = self.ENG_LETTERS
        else:
            alphabet = self.UKR_LETTERS

        length = len(alphabet)
        to_return = ""

        for i in range(len(text)):
            if text[i].upper() in alphabet:
                pos_lower = alphabet.index(text[i].upper())

                if operation == "encrypt":
                    idx = (A * i + B + pos_lower) % length
                else:
                    idx = (pos_lower + length - ((A * i + B) % length)) % length

                if idx < 0:
                    idx += length

                to_return += alphabet[idx].lower()
            else:
                to_return += text[i]
        return to_return

    def non_linear_abc(self, text, A, B, C, language, operation):
        if language == "english":
            alphabet = self.ENG_LETTERS
        else:
            alphabet = self.UKR_LETTERS

        length = len(alphabet)
        to_return = ""

        for i in range(len(text)):
            if text[i].upper() in alphabet:
                pos_lower = alphabet.index(text[i].upper())

                if operation == "encrypt":
                    idx = (A * i ** 2 + B * i + C + pos_lower) % length
                else:
                    idx = (pos_lower + length - ((A * i ** 2 + B * i + C) % length)) % length

                if idx < 0:
                    idx += length

                to_return += alphabet[idx].lower()
            else:
                to_return += text[i]
        return to_return

    def password(self, text, password, language, operation):
        if language == "english":
            alphabet = self.ENG_LETTERS
        else:
            alphabet = self.UKR_LETTERS

        if operation == "encrypt":
            encrypt = 0
        else:
            encrypt = 1

        length = len(alphabet)
        to_return = ""

        for i in range(len(text)):
            if text[i].upper() in alphabet:
                idx = (alphabet.index(text[i].upper()) + (-1) ** encrypt * (alphabet.index(
                    password[i % len(password)].upper())))
                idx %= length

                if idx < 0:
                    idx += length

                to_return += alphabet[idx].lower()

            else:
                to_return += text[i]

        return to_return

    def linear_attack(self, original_message, encoded_message, language):
        if language == "english":
            alphabet = self.ENG_LETTERS
        else:
            alphabet = self.UKR_LETTERS

        A, B = 0, 0
        n = len(alphabet)

        for i in range(n):
            for j in range(n):
                if (j - i) % n == 0:
                    continue
                if self.linear_ab(original_message, i, j, language, "encrypt") == encoded_message:
                    A, B = i, j
                    break
            if A != 0 or B != 0:
                break

        return A, B

    def non_linear_attack(self, original_message, encoded_message, language):
        if language == "english":
            alphabet = self.ENG_LETTERS
        else:
            alphabet = self.UKR_LETTERS

        A, B, C = 0, 0, 0
        n = len(alphabet)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if (k - i * (j ** 2) - j * i + k) % n == 0:
                        continue
                    if self.non_linear_abc(original_message, i, j, k, language, "encrypt") == encoded_message:
                        A, B, C = i, j, k
                        break
                if A != 0 or B != 0 or C != 0:
                    break
            if A != 0 or B != 0 or C != 0:
                break

        return A, B, C

    def password_attack(self, original_message, encoded_message, language):
        if language == "english":
            alphabet = self.ENG_LETTERS
        else:
            alphabet = self.UKR_LETTERS

        length = len(alphabet)
        decrypted_password = ""
        to_return = ""

        text_pos = 0

        while text_pos < len(encoded_message):

            if encoded_message[text_pos].upper() in alphabet and original_message[text_pos].upper() in alphabet:
                encrypted_idx = alphabet.index(encoded_message[text_pos].upper())
                original_idx = alphabet.index(original_message[text_pos].upper())
                diff = (encrypted_idx - original_idx) % length
                decrypted_password += alphabet[diff]

                decrypted_text = self.password(original_message, decrypted_password, language, "encrypt")
                if decrypted_text == encoded_message:
                    to_return += decrypted_password.lower()
                    return to_return

            text_pos += 1


class GammaCipher:
    def generate_key(self, text):
        key = ""
        for _ in range(len(text) + random.randint(0, 10)):
            ascii_symbol = random.randint(0, 1000)
            key += chr(ascii_symbol)
        return key

    def g_encrypt(self, plaintext, gamma):
        result = ""
        for i in range(len(plaintext)):
            result += chr(ord(plaintext[i]) ^ ord(gamma[i % len(gamma)]))
        return result

    def g_decrypt(self, ciphertext, gamma):
        result = ""
        for i in range(len(ciphertext)):
            result += chr(ord(ciphertext[i]) ^ ord(gamma[i % len(gamma)]))
        return result


class KnapsackCipher:
    def __init__(self, private_key=None, m=None, n=None):
        self.private_key = private_key or []
        self.m = m
        self.n = n

    def generate_keys(self):
        rand = random.Random()
        self.private_key = [2, 3, 7]
        for i in range(3, 8):
            self.private_key.append(2 * self.private_key[i - 1] + rand.randint(0, 9))
        self.n = rand.randint(1, 99)
        while True:
            self.m = self.n * 20 + rand.randint(0, self.n * 10)
            if gcd(self.m, self.n) == 1:
                break

    def encrypt(self, message):
        public_key = [(x * self.n) % self.m for x in self.private_key]

        sums = []
        for c in message:
            binary = ord(c)
            sum_value = sum(((binary >> i) & 1) * public_key[7 - i] for i in range(8))
            sums.append(sum_value)

        return ','.join(map(str, sums))

    def decrypt(self, message):
        values = list(map(int, message.split(',')))
        t = self.modular_inverse(self.n, self.m)

        if t is None:
            raise ValueError("Multiplicative inverse does not exist")

        chars = []
        for value in values:
            sum_value = (value * t) % self.m
            bits = [0] * 8
            for i in range(7, -1, -1):
                if sum_value >= self.private_key[i]:
                    bits[i] = 1
                    sum_value -= self.private_key[i]

            num = 0
            for bit in bits:
                num = (num << 1) | bit

            chars.append(chr(num))

        return ''.join(chars)

    def modular_inverse(self, a, m):
        m0, x0, x1 = m, 0, 1
        if m == 1:
            return 0
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += m0
        return x1


class RSACipher:
    @staticmethod
    def is_prime(n):
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True

    @staticmethod
    def euler_func(p, q):
        return (p - 1) * (q - 1)

    @staticmethod
    def extended_euclidean_algorithm(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = RSACipher.extended_euclidean_algorithm(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    @staticmethod
    def modular_inverse(num, mod):
        return RSACipher.extended_euclidean_algorithm(num, mod)[1] % mod

    @staticmethod
    def generate_keys(bit_length):
        half_bit_length = bit_length // 2
        while True:
            p = random.randint(2 ** (half_bit_length - 1), 2 ** half_bit_length - 1)
            if RSACipher.is_prime(p):
                break
        while True:
            q = random.randint(2 ** (half_bit_length - 1), 2 ** half_bit_length - 1)
            if RSACipher.is_prime(q) and p != q:
                break

        n = p * q

        phi = RSACipher.euler_func(p, q)
        while True:
            e = random.randint(2, phi - 1)
            if RSACipher.extended_euclidean_algorithm(e, phi)[0] == 1:
                break
        pub_key = (e, n)

        d = RSACipher.modular_inverse(e, phi)
        priv_key = (d, n)
        return pub_key, priv_key

    @staticmethod
    def rsa_encrypt(public_key, plain_text):
        e, n = public_key
        try:
            encrypted_text = pow(int(plain_text), e, n)
        except ValueError:
            encrypted_text = [pow(ord(char), e, n) for char in plain_text]
        return encrypted_text

    @staticmethod
    def rsa_decrypt(private_key, encrypted_text):
        d, n = private_key
        try:
            decrypted_text = str(pow(encrypted_text, d, n))
        except TypeError:
            decrypted_text = ''.join([chr(pow(char, d, n)) for char in encrypted_text])
        return decrypted_text


class Key_Exchange_DH:
    @staticmethod
    def generate_key_pair(p, g, private_key=None):
      if private_key is None:
          private_key = random.randint(2, p - 1)
      public_key = pow(g, private_key) % p
      return public_key, private_key

    @staticmethod
    def exchange_keys(p, public_key_B, private_key_A):
      return pow(public_key_B, private_key_A) % p
