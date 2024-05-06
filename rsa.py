import tkinter as tk
from tkinter import ttk, messagebox
from main import Main
from cipher import RSACipher


class RSA(Main):
    def __init__(self):
        super().__init__()

        self.title("Шифр RSA")
        self.geometry("700x500")

        self.rsa = RSACipher()

        self.create_menu()
        self.create_input_output_fields()
        self.create_rsa_fields()

        self.create_buttons()

    def create_buttons(self):
        pass

    def create_menu(self):
        self.menubar = tk.Menu(self)

        file_menu = tk.Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="Створити", command=super().create_file)
        file_menu.add_command(label="Відкрити", command=super().open_file)
        file_menu.add_command(label="Зберегти", command=super().save_file)
        file_menu.add_command(label="Друк", command=super().print_file)
        self.menubar.add_cascade(label="Файл", menu=file_menu)

        self.menubar.add_command(label="Статистика", command=super().show_statistics_window)
        self.menubar.add_command(label="Розробник", command=super().show_developer_info)
        self.menubar.add_command(label="Вихід", command=self.confirm_exit)

        self.config(menu=self.menubar)

    def create_input_output_fields(self):
        input_output_panel = ttk.Frame(self)
        input_output_panel.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        input_label = ttk.Label(input_output_panel, text="Введіть текст, щоб зашифрувати/розшифрувати")
        self.input_text = tk.Text(input_output_panel, height=10, width=40, wrap=tk.WORD)
        input_scrollbar = ttk.Scrollbar(input_output_panel, command=self.input_text.yview)
        self.input_text.config(yscrollcommand=input_scrollbar.set)

        output_label = ttk.Label(input_output_panel, text="Результат")
        self.output_text = tk.Text(input_output_panel, height=10, width=40, wrap=tk.WORD)
        output_scrollbar = ttk.Scrollbar(input_output_panel, command=self.output_text.yview)
        self.output_text.config(yscrollcommand=output_scrollbar.set)

        input_label.grid(row=0, column=0, padx=5, pady=5)
        self.input_text.grid(row=1, column=0, padx=5, pady=5)
        input_scrollbar.grid(row=1, column=1, sticky="ns")
        output_label.grid(row=2, column=0, padx=5, pady=5)
        self.output_text.grid(row=3, column=0, padx=5, pady=5)
        output_scrollbar.grid(row=3, column=1, sticky="ns")

        input_output_panel.grid_rowconfigure(0, weight=1)
        input_output_panel.grid_columnconfigure(0, weight=1)

    def create_rsa_fields(self):
        rsa_panel = ttk.Frame(self)
        rsa_panel.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        pub_key_label = ttk.Label(rsa_panel, text="Публічний ключ (e, n):")
        pub_key_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.pub_key_entry = ttk.Entry(rsa_panel)
        self.pub_key_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        priv_key_label = ttk.Label(rsa_panel, text="Приватний ключ (d, n):")
        priv_key_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.priv_key_entry = ttk.Entry(rsa_panel)
        self.priv_key_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        generate_button = ttk.Button(rsa_panel, text="Згенерувати ключі", command=self.generate_keys)
        generate_button.grid(row=2, column=0, columnspan=2, pady=5)

        encrypt_button = ttk.Button(rsa_panel, text="Зашифрувати", command=self.encrypt)
        encrypt_button.grid(row=3, column=0, columnspan=2, pady=5)

        decrypt_button = ttk.Button(rsa_panel, text="Розшифрувати", command=self.decrypt)
        decrypt_button.grid(row=4, column=0, columnspan=2, pady=5)

    def generate_keys(self):
        pub_key, priv_key = self.rsa.generate_keys(12)
        self.pub_key_entry.delete(0, tk.END)
        self.pub_key_entry.insert(0, str(pub_key))
        self.priv_key_entry.delete(0, tk.END)
        self.priv_key_entry.insert(0, str(priv_key))

    def encrypt(self):
        pub_key_str = self.pub_key_entry.get().strip()
        priv_key_str = self.priv_key_entry.get().strip()

        # try:
        #     pub_key = eval(pub_key_str)
        #     priv_key = eval(priv_key_str)
        # except SyntaxError:
        #     messagebox.showerror("Помилка", "Невірний формат ключів")
        #     return

        pub_key = eval(pub_key_str)
        priv_key = eval(priv_key_str)

        plaintext = self.input_text.get("1.0", tk.END).strip()
        if not plaintext:
            messagebox.showerror("Помилка", "Введіть текст для шифрування")
            return

        encrypted_text = self.rsa.rsa_encrypt(pub_key, plaintext)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, str(encrypted_text))

    def decrypt(self):
        pub_key_str = self.pub_key_entry.get().strip()
        priv_key_str = self.priv_key_entry.get().strip()

        # try:
        #     pub_key = eval(pub_key_str)
        #     priv_key = eval(priv_key_str)
        # except SyntaxError:
        #     messagebox.showerror("Помилка", "Невірний формат ключів")
        #     return

        pub_key = eval(pub_key_str)
        priv_key = eval(priv_key_str)

        encrypted_text = self.input_text.get("1.0", tk.END).strip()
        if not encrypted_text:
            messagebox.showerror("Помилка", "Введіть зашифрований текст для розшифрування")
            return

        decrypted_text = self.rsa.rsa_decrypt(priv_key, eval(encrypted_text))
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, decrypted_text)



# def is_prime(n):
#     """Check if a number is prime"""
#     for i in range(2,n):
#         if (n % i) == 0:
#             return False
#     return True
#
#
# def euler_func(p, q):
#     """Count the positive integers (up to p*q) that are relatively prime to p*q"""
#     return (p - 1) * (q - 1)
#
#
# def extended_euclidean_algorithm(a, b):
#     """Extended Euclidean algorithm for finding gcd, x, y"""
#     if a == 0 :
#         return b, 0, 1
#     gcd,x1,y1 = extended_euclidean_algorithm(b % a, a)
#     x = y1 - (b // a) * x1
#     y = x1
#     return gcd, x, y
#
#
# def modular_inverse(num, mod):
#     return extended_euclidean_algorithm(num, mod)[1] % mod
#
#
# def generate_keys(bit_length):
#     """Generate public and private keys"""
#     # Generation of p and q
#     half_bit_length = bit_length // 2
#     while True:
#         p = random.randint(2**(half_bit_length-1), 2**half_bit_length-1)
#         if is_prime(p):
#             break
#     while True:
#         q = random.randint(2**(half_bit_length-1), 2**half_bit_length-1)
#         if is_prime(q) and p != q:
#             break
#     # Calculation of the module
#     n = p * q
#     # Public key creation
#     phi = euler_func(p, q)
#     while True:
#         e = random.randint(3, phi - 1)
#         if extended_euclidean_algorithm(e, phi)[0] == 1:
#             break
#     pub_key = (e, n)
#     # Private key creation
#     d = modular_inverse(e, phi)
#     priv_key = (d, n)
#     return pub_key, priv_key
#
#
# def rsa_encrypt(public_key, plain_text):
#     """Encrypt text using input parameters"""
#     e, n = public_key
#     try:
#         encrypted_text = pow(int(plain_text), e, n)
#     except ValueError:  # Якщо виняток виникає при спробі конвертації тексту у ціле число
#         encrypted_text = [pow(ord(char), e, n) for char in plain_text]
#     return encrypted_text
#
#
# def rsa_decrypt(private_key, encrypted_text):
#     """Decrypt text using input parameters"""
#     d, n = private_key
#     try:
#         decrypted_text = str(pow(encrypted_text, d, n))
#     except TypeError:  # Якщо виняток виникає при спробі розшифрувати список
#         decrypted_text = ''.join([chr(pow(char, d, n)) for char in encrypted_text])
#     return decrypted_text
#
#
# # def rsa_encrypt(public_key, plain_text):
# #     """Encrypt text using input parameters"""
# #     e, n = public_key
# #     return pow(int(plain_text), e, n)
#
#
# # def rsa_decrypt(private_key, encrypted_text):
# #     """Decrypt text using input parameters"""
# #     d, n = private_key
# #     decrypted_text = str(pow(encrypted_text, d, n))
# #     return ''.join(decrypted_text)
#
#
# keys = generate_keys(12)
# key1 = (3, 9173503)
# key2 = (6111579, 9173503)
# initial_text = "111111"
# encrypted_text = rsa_encrypt(key1, initial_text)
# decrypted_text = rsa_decrypt(key2, encrypted_text)
# print("Ключі - ", keys)
# print("Початковий текст - ", initial_text)
# print("Зашифрований текст - ", encrypted_text)
# print("Розшифрований текст - ", decrypted_text)