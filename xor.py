import tkinter as tk
from tkinter import ttk, filedialog
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
        entry_panel = ttk.Frame(self.radio_panel)
        entry_panel.grid(row=2, column=0, padx=10, pady=10, sticky="s")

        input_entry_label = ttk.Label(entry_panel, text="Введіть гамма ключ:")
        input_entry_label.grid(row=0, column=0, pady=5)

        self.input_entry = ttk.Entry(entry_panel)
        self.input_entry.grid(row=0, column=1, pady=5)

        generate_button = ttk.Button(entry_panel, text="Згенерувати", command=self.generate_key)
        generate_button.grid(row=1, column=0, columnspan=2, pady=5)

        encrypt_button = ttk.Button(entry_panel, text="Зашифрувати", command=self.encrypt)
        encrypt_button.grid(row=2, column=0, columnspan=2, pady=5)

        decrypt_button = ttk.Button(entry_panel, text="Розшифрувати", command=self.decrypt)
        decrypt_button.grid(row=3, column=0, columnspan=2, pady=5)

    def show_file_input(self):
        file_panel = ttk.Frame(self.radio_panel)
        file_panel.grid(row=2, column=0, padx=10, pady=10, sticky="s")

        open_file_button = ttk.Button(file_panel, text="Відкрити файл", command=self.open_file)
        open_file_button.grid(row=1, column=0, columnspan=2, pady=5)

        self.file_label = ttk.Label(file_panel, text="")
        self.file_label.grid(row=2, column=0, columnspan=2, pady=5)

        self.step_var = tk.IntVar(value=1)

        self.step_spinbox = tk.Spinbox(file_panel, from_=1, to=100, textvariable=self.step_var)
        self.step_spinbox.grid(row=3, column=0, columnspan=2, pady=5)

        encrypt_button = ttk.Button(file_panel, text="Зашифрувати", command=self.encrypt_image)
        encrypt_button.grid(row=4, column=0, columnspan=2, pady=5)

        decrypt_button = ttk.Button(file_panel, text="Розшифрувати", command=self.decrypt_image)
        decrypt_button.grid(row=5, column=0, columnspan=2, pady=5)

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.grid_forget()

    def clear_input_widgets(self):
        self.file_label.pack_forget()
        self.step_spinbox.pack_forget()
        for widget in self.winfo_children():
            widget.destroy()

    def clear_file_widgets(self):
        self.input_entry.pack_forget()
        for widget in self.winfo_children():
            widget.destroy()

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            self.file_label.config(text="Файл: " + file_path)

    def generate_key(self):
        # self.gamma.generate_key(self.input_text.get("1.0", tk.END + "-1c"))
        self.input_entry.config(text=str(self.gamma.generate_key(self.input_text.get("1.0", tk.END + "-1c"))))

    def encrypt(self):
        pass

    def decrypt(self):
        pass


    def update_output(self):
        operation = self.operation_var.get()
        input_text = self.input_text.get("1.0", tk.END + "-1c")
        gamma_key = self.gamma_entry.get()

        if operation == "encrypt":
            result = self.trithemius.encrypt(input_text, gamma_key)
        else:
            result = self.trithemius.decrypt(input_text, gamma_key)

        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)
        self.output_text.config(state=tk.DISABLED)
