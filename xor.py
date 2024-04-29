import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from cipher import GammaCipher
from main import Main


class XOR(Main):
    def __init__(self):
        super().__init__()

        self.title("Шифр Гамування")
        self.geometry("750x500")

        self.gamma = GammaCipher()

        self.create_menu()
        self.create_input_output_fields()
        self.create_radio_buttons()

        self.entry_panel = None
        self.file_panel = None

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

        self.input_text = tk.Text(input_output_panel, height=10, width=40, wrap=tk.WORD)
        input_scrollbar = ttk.Scrollbar(input_output_panel, command=self.input_text.yview)
        self.input_text.config(yscrollcommand=input_scrollbar.set)

        output_label = ttk.Label(input_output_panel, text="Результат")
        self.output_text = tk.Text(input_output_panel, height=10, width=40, wrap=tk.WORD)
        output_scrollbar = ttk.Scrollbar(input_output_panel, command=self.output_text.yview)
        self.output_text.config(yscrollcommand=output_scrollbar.set)

        self.input_text.grid(row=0, column=0, padx=5, pady=5)
        input_scrollbar.grid(row=0, column=1, sticky="ns")
        output_label.grid(row=1, column=0, padx=5, pady=5)
        self.output_text.grid(row=2, column=0, padx=5, pady=5)
        output_scrollbar.grid(row=2, column=1, sticky="ns")

        input_output_panel.grid_rowconfigure(0, weight=1)
        input_output_panel.grid_columnconfigure(0, weight=1)

    def create_radio_buttons(self):
        self.radio_panel = ttk.Frame(self)
        self.radio_panel.grid(row=0, column=1, padx=10, pady=10, sticky="n")

        self.radio_var = tk.StringVar()

        enter_radio = ttk.Radiobutton(self.radio_panel, text="Ввести", value="enter", variable=self.radio_var,
                                      command=self.show_input_entry)
        file_radio = ttk.Radiobutton(self.radio_panel, text="Прочитати з файлу", value="file", variable=self.radio_var,
                                     command=self.show_file_input)

        enter_radio.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        file_radio.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    def show_input_entry(self):
        if self.file_panel:
            self.file_panel.grid_forget()
        if not self.entry_panel:
            self.entry_panel = ttk.Frame(self.radio_panel)

            input_entry_label = ttk.Label(self.entry_panel, text="Введіть гамма ключ:")
            input_entry_label.grid(row=0, column=0, pady=5)

            self.input_entry = ttk.Entry(self.entry_panel)
            self.input_entry.grid(row=0, column=1, pady=5)

            generate_button = ttk.Button(self.entry_panel, text="Згенерувати", command=self.generate_key)
            generate_button.grid(row=1, column=0, columnspan=2, pady=5)

            encrypt_button = ttk.Button(self.entry_panel, text="Зашифрувати", command=self.encrypt)
            encrypt_button.grid(row=2, column=0, columnspan=2, pady=5)

            decrypt_button = ttk.Button(self.entry_panel, text="Розшифрувати", command=self.decrypt)
            decrypt_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.entry_panel.grid(row=2, column=0, padx=10, pady=10, sticky="s")

    def show_file_input(self):
        if self.entry_panel:
            self.entry_panel.grid_forget()
        if not self.file_panel:
            self.file_panel = ttk.Frame(self.radio_panel)

            open_file_button = ttk.Button(self.file_panel, text="Відкрити файл", command=self.open_file)
            open_file_button.grid(row=1, column=0, columnspan=2, pady=5)

            self.file_label = ttk.Label(self.file_panel, text="")
            self.file_label.grid(row=2, column=0, columnspan=2, pady=5)

        self.file_panel.grid(row=2, column=0, padx=10, pady=10, sticky="s")

    def open_file(self):
        self.file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if self.file_path:
            file_name = os.path.basename(self.file_path)
            self.file_label.config(text="Файл: " + file_name)
            panel = ttk.Frame(self.file_panel)
            panel.grid(row=3, column=0, padx=10, pady=10, sticky="s")

            self.step_var = tk.IntVar(value=0)

            self.step_spinbox = tk.Spinbox(panel, from_=1, to=100, textvariable=self.step_var,
                                           command=self.on_spinbox_change)
            self.step_spinbox.grid(row=0, column=0, padx=10, pady=10)

            self.selected_gamma_entry = ttk.Entry(panel)
            self.selected_gamma_entry.grid(row=0, column=1, padx=10, pady=10)

            generate_key_button = ttk.Button(self.file_panel, text="Згенерувати", command=self.generate_key_file)
            generate_key_button.grid(row=4, column=0, columnspan=2, pady=5)

            encrypt_button = ttk.Button(self.file_panel, text="Зашифрувати", command=self.encrypt)
            encrypt_button.grid(row=5, column=0, columnspan=2, pady=5)

            decrypt_button = ttk.Button(self.file_panel, text="Розшифрувати", command=self.decrypt)
            decrypt_button.grid(row=6, column=0, columnspan=2, pady=5)
        self.on_spinbox_change()

    def generate_key(self):
        key = self.gamma.generate_key(self.input_text.get("1.0", tk.END + "-1c"))
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, key)

    def generate_key_file(self):
        num_gammas = int(self.step_spinbox.get())
        text = self.input_text.get("1.0", tk.END + "-1c")
        gammas = [self.gamma.generate_key(text) for _ in range(num_gammas)]
        with open(self.file_path, "w", encoding="utf-16") as file:
            for gamma in gammas:
                file.write(gamma + "\n\n")
        messagebox.showinfo("Повідомлення", f"Згенеровано {num_gammas} ключів, збережено у файл {self.file_path}")
        self.on_spinbox_change()

    def on_spinbox_change(self):
        selected_row = int(self.step_var.get())
        with open(self.file_path, "r", encoding="utf-16") as file:
            gammas = file.readlines()
            if selected_row <= len(gammas):
                selected_gamma = gammas[selected_row - 1].strip()
                self.selected_gamma_entry.delete(0, tk.END)
                self.selected_gamma_entry.insert(0, selected_gamma)
            else:
                self.selected_gamma_entry.delete(0, tk.END)
                self.selected_gamma_entry.insert(0, "")

    def encrypt(self):
        if self.radio_var.get() == "enter":
            gamma_key = self.input_entry.get()
        elif self.radio_var.get() == "file":
            gamma_key = self.selected_gamma_entry.get()
        plaintext = self.input_text.get("1.0", tk.END + "-1c")
        ciphertext = self.gamma.g_encrypt(plaintext, gamma_key)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, ciphertext)
        self.output_text.config(state=tk.DISABLED)

    def decrypt(self):
        if self.radio_var.get() == "enter":
            gamma_key = self.input_entry.get()
        elif self.radio_var.get() == "file":
            gamma_key = self.selected_gamma_entry.get()
        ciphertext = self.input_text.get("1.0", tk.END + "-1c")
        plaintext = self.gamma.g_decrypt(ciphertext, gamma_key)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, plaintext)
        self.output_text.config(state=tk.DISABLED)

