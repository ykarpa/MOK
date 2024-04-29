import random


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
