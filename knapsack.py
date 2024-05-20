from cipher import KnapsackCipher
from main import Main
import tkinter as tk
from tkinter import ttk, messagebox


class KnapsackTask(Main):
    def __init__(self):
        super().__init__()

        self.title("Задача рюкзака")
        self.geometry("785x500")

        self.cipher = KnapsackCipher()

        self.create_menu()
        self.create_input_output_fields()
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
        input_text_panel = ttk.Frame(self)
        input_text_panel.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        input_label = ttk.Label(input_text_panel, text="Введіть текст, щоб зашифрувати/розшифрувати",
                                font=("Verdana", 10))
        input_label.grid(row=0, column=0, padx=5, pady=5)
        self.input_text = tk.Text(input_text_panel, height=10, width=42, wrap=tk.WORD)
        self.input_text.grid(row=1, column=0, padx=5, pady=5)
        input_scrollbar = ttk.Scrollbar(input_text_panel, command=self.input_text.yview)
        self.input_text.config(yscrollcommand=input_scrollbar.set)
        input_scrollbar.grid(row=1, column=1, sticky="ns")

        input_data_panel = ttk.Frame(self)
        input_data_panel.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        t_label = tk.Label(input_data_panel, text="Взаємнопросте число t з m:", font=("Segoe UI", 9))
        t_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.t_input = tk.Entry(input_data_panel, width=28)
        self.t_input.grid(row=0, column=1, padx=10, pady=5)

        m_label = tk.Label(input_data_panel, text="Модуль m:", font=("Segoe UI", 9))
        m_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.m_input = tk.Entry(input_data_panel, width=28)
        self.m_input.grid(row=1, column=1, padx=10, pady=5)

        b_label = tk.Label(input_data_panel, text="Послідовність чисел B:", font=("Segoe UI", 9))
        b_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.b_input = tk.Entry(input_data_panel, width=28)
        self.b_input.grid(row=2, column=1, padx=10, pady=5)

        self.generate_keys_btn = tk.Button(input_data_panel, text="Згенерувати ключі", command=self.generate_keys,
                                           width=25, height=3, font=("", 9), background="#ffffff")
        self.generate_keys_btn.grid(row=3, column=1, padx=10, pady=5)

        output_panel = ttk.Frame(self)
        output_panel.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="w")

        ciphertext_label = tk.Label(output_panel, text="Зашифрований текст:", font=("Verdana", 10), justify="left")
        ciphertext_label.grid(row=0, column=0, padx=10, pady=5)

        self.ciphertext_output = tk.Text(output_panel, height=10, width=33)
        self.ciphertext_output.grid(row=1, column=0, padx=10, pady=5)

        decrypted_ciphertext_label = tk.Label(output_panel, text="Розшифрований текст:", font=("Verdana", 10), justify="left")
        decrypted_ciphertext_label.grid(row=0, column=1, padx=10, pady=5)

        self.decrypted_ciphertext_output = tk.Text(output_panel, height=10, width=32)
        self.decrypted_ciphertext_output.grid(row=1, column=1, padx=10, pady=5)

        btn_panel = ttk.Frame(output_panel)
        btn_panel.grid(row=0, column=2, rowspan=2)
        encrypt_btn = tk.Button(btn_panel, text="Зашифрувати", command=self.encrypt, width=25, height=3, font=("", 9), background="#ffffff")
        encrypt_btn.grid(row=1, column=2, padx=10, pady=5)

        decrypt_btn = tk.Button(btn_panel, text="Розшифрувати", command=self.decrypt, width=25, height=3, font=("", 9), background="#ffffff")
        decrypt_btn.grid(row=2, column=2, padx=10, pady=5)

    def generate_keys(self):
        self.cipher.generate_keys()
        self.m_input.delete(0, tk.END)
        self.m_input.insert(0, str(self.cipher.m))
        self.t_input.delete(0, tk.END)
        self.t_input.insert(0, str(self.cipher.n))
        self.b_input.delete(0, tk.END)
        self.b_input.insert(0, ','.join(map(str, self.cipher.private_key)))

    def encrypt(self):
        plaintext = self.input_text.get("1.0", tk.END).strip()
        if not plaintext:
            messagebox.showerror("Error", "Input text is empty!")
            return

        try:
            self.cipher.m = int(self.m_input.get().strip())
            self.cipher.n = int(self.t_input.get().strip())
            self.cipher.private_key = list(map(int, self.b_input.get().strip().split(',')))
        except ValueError:
            messagebox.showerror("Error", "Invalid m, t, or B values!")
            return

        try:
            ciphertext = self.cipher.encrypt(plaintext)
            self.ciphertext_output.delete("1.0", tk.END)
            self.ciphertext_output.insert(tk.END, ciphertext)
        except Exception as e:
            messagebox.showerror("Encryption Error", str(e))

    def decrypt(self):
        ciphertext = self.ciphertext_output.get("1.0", tk.END).strip()
        if not ciphertext:
            messagebox.showerror("Error", "Ciphertext is empty!")
            return

        try:
            self.cipher.m = int(self.m_input.get().strip())
            self.cipher.n = int(self.t_input.get().strip())
            self.cipher.private_key = list(map(int, self.b_input.get().strip().split(',')))
        except ValueError:
            messagebox.showerror("Error", "Invalid m, t, or B values!")
            return

        try:
            decrypted_text = self.cipher.decrypt(ciphertext)
            self.decrypted_ciphertext_output.delete("1.0", tk.END)
            self.decrypted_ciphertext_output.insert(tk.END, decrypted_text)
        except Exception as e:
            messagebox.showerror("Decryption Error", str(e))

    def confirm_exit(self):
        if messagebox.askokcancel("Вихід", "Ви впевнені, що хочете вийти?"):
            self.destroy()
