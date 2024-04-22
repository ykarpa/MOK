from cipher import CaesarCipher
from main import Main
import tkinter as tk
from tkinter import ttk, Spinbox


class Caesar(Main):
    def __init__(self):
        super().__init__()
        self.title("Шифр Цезаря")

        self.cipher = CaesarCipher()

        self.create_menu()
        self.create_input_output_fields()
        self.create_encryption_fields()
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


        # self.menubar.add_command(label="Шифрувати зображення", command=self.encrypt_image)
        self.menubar.add_command(label="Атака", command=self.brute_force_attack)
        self.menubar.add_command(label="Статистика", command=super().show_statistics_window)
        self.menubar.add_command(label="Розробник", command=super().show_developer_info)
        self.menubar.add_command(label="Вихід", command=super().confirm_exit)

        self.config(menu=self.menubar)

    def brute_force_attack(self):
        attack_window = tk.Toplevel(self)
        attack_window.title("Атака методом грубої сили")

        input_label = ttk.Label(attack_window, text="Повідомлення:")
        input_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        input_text = tk.Text(attack_window, height=5, width=50, wrap=tk.WORD)
        input_text.grid(row=1, column=0, padx=5, pady=5)

        output_label = ttk.Label(attack_window, text="Зашифроване повідомлення:")
        output_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        output_text = tk.Text(attack_window, height=5, width=50, wrap=tk.WORD)
        output_text.grid(row=3, column=0, padx=5, pady=5)

        key_label = ttk.Label(attack_window, text="Ключ:")
        key_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        key_output = ttk.Label(attack_window, text="")
        key_output.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        def perform_attack():
            original_message = input_text.get("1.0", tk.END).strip()
            encrypted_message = output_text.get("1.0", tk.END).strip()

            for step in range(27):
                decrypted_message = self.cipher.eng_decrypt(encrypted_message, step)
                if decrypted_message == original_message:
                    key_output.config(text=str(step))
                    break
            else:
                for step in range(34):
                    decrypted_message = self.cipher.ua_decrypt(encrypted_message, step)
                    if decrypted_message == original_message:
                        key_output.config(text=str(step))
                        break
                    else:
                        key_output.config(text="Помилка: ключ не знайдено")

        attack_button = ttk.Button(attack_window, text="Запустити атаку", command=perform_attack)
        attack_button.grid(row=6, column=0, padx=5, pady=5)

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
        self.output_text.config(yscrollcommand=output_scrollbar.set, state=tk.DISABLED)

        input_label.grid(row=0, column=0, padx=5, pady=5)
        self.input_text.grid(row=1, column=0, padx=5, pady=5)
        input_scrollbar.grid(row=1, column=1, sticky="ns")
        output_label.grid(row=2, column=0, padx=5, pady=5)
        self.output_text.grid(row=3, column=0, padx=5, pady=5)
        output_scrollbar.grid(row=3, column=1, sticky="ns")

    def create_encryption_fields(self):
        encryption_panel = ttk.Frame(self)
        encryption_panel.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        step_label = ttk.Label(encryption_panel, text="Крок шифрування:")
        step_label.grid(row=0, column=0)

        self.step_var = tk.IntVar(value=0)
        step_spinbox = Spinbox(encryption_panel, from_=0, to=26, textvariable=self.step_var, state="readonly")
        step_spinbox.grid(row=0, column=1, padx=5, pady=5)

        self.language_var = tk.StringVar(value="english")
        english_radio = ttk.Radiobutton(encryption_panel, text="Англійська", value="english",
                                        variable=self.language_var)
        ukrainian_radio = ttk.Radiobutton(encryption_panel, text="Українська", value="ukrainian",
                                          variable=self.language_var)

        english_radio.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ukrainian_radio.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        operation_var = tk.StringVar(value="encrypt")
        encrypt_radio = ttk.Radiobutton(encryption_panel, text="Зашифрувати", value="encrypt", variable=operation_var)
        decrypt_radio = ttk.Radiobutton(encryption_panel, text="Розшифрувати", value="decrypt", variable=operation_var)

        encrypt_radio.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        decrypt_radio.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        execute_button = ttk.Button(encryption_panel, text="Виконати",
                                    command=lambda: self.update_output(operation_var.get()),
                                    width=20)
        execute_button.grid(row=4, column=0, columnspan=2, pady=10)

    def update_output(self, operation):
        input_text = self.input_text.get("1.0", tk.END + "-1c")
        step = int(self.step_var.get())
        print(step)

        if self.language_var.get() == "english":
            if operation == "encrypt":
                result = self.cipher.eng_encrypt(input_text, step)
            else:
                result = self.cipher.eng_decrypt(input_text, step)
        else:
            if operation == "encrypt":
                result = self.cipher.ua_encrypt(input_text, step)
            else:
                result = self.cipher.ua_decrypt(input_text, step)

        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)
        self.output_text.config(state=tk.DISABLED)

app = Caesar()
app.mainloop()