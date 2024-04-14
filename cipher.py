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