import tkinter as tk
from tkinter import ttk, messagebox
from main import Main
from cipher import Key_Exchange_DH


class DH(Main):
    def __init__(self):
        super().__init__()

        self.title("Протокол обміну ключами Діффі-Гелмана")
        self.geometry("700x500")

        self.dh = Key_Exchange_DH()

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

        self.menubar.add_command(label="Розробник", command=super().show_developer_info)
        self.menubar.add_command(label="Вихід", command=self.confirm_exit)

        self.config(menu=self.menubar)

    def create_input_output_fields(self):
        input_output_panel = ttk.Frame(self)
        input_output_panel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        p_label = ttk.Label(input_output_panel, text="Введіть p:")
        self.p_entry = ttk.Entry(input_output_panel, width=20)

        g_label = ttk.Label(input_output_panel, text="Введіть g:")
        self.g_entry = ttk.Entry(input_output_panel, width=20)

        private_key_label = ttk.Label(input_output_panel, text="Введіть свій приватний ключ:")
        self.private_key_entry = ttk.Entry(input_output_panel, width=20)

        generate_key_button = ttk.Button(input_output_panel, text="Генерувати ключ", command=self.generate_keys)

        public_key_A_label = ttk.Label(input_output_panel, text="Ваш публічний ключ:")
        self.public_key_A_display = ttk.Label(input_output_panel, text="")

        public_key_B_label = ttk.Label(input_output_panel, text="Введіть публічний ключ іншого користувача:")
        self.public_key_B_entry = ttk.Entry(input_output_panel, width=20)

        calculate_shared_key_button = ttk.Button(input_output_panel, text="Обчислити спільний секретний ключ",
                                                 command=self.calculate_shared_key)
        output_text = ttk.Label(input_output_panel, text="Спільний секретний ключ: ")
        self.output_text = ttk.Label(input_output_panel, text="")

        p_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.p_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        g_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.g_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        private_key_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.private_key_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        generate_key_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        public_key_A_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.public_key_A_display.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        public_key_B_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.public_key_B_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        calculate_shared_key_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        output_text.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self.output_text.grid(row=7, column=1, padx=5, pady=5, sticky="w")

        input_output_panel.grid_rowconfigure(6, weight=1)
        input_output_panel.grid_columnconfigure(2, weight=1)

    def generate_keys(self):
        p_str = self.p_entry.get().strip()
        g_str = self.g_entry.get().strip()
        private_key_str = self.private_key_entry.get().strip()

        if not p_str or not g_str or not private_key_str:
            messagebox.showerror("Помилка", "Будь ласка, заповніть всі поля.")
            return

        try:
            p = int(p_str)
            g = int(g_str)
            private_key = int(private_key_str)
        except ValueError:
            messagebox.showerror("Помилка", "Неправильний формат числа.")
            return

        public_key_A, _ = Key_Exchange_DH.generate_key_pair(p, g, private_key)
        self.public_key_A_display.config(text=str(public_key_A))

    def calculate_shared_key(self):
        p_str = self.p_entry.get().strip()
        public_key_A_str = self.public_key_A_display.cget("text").strip()
        private_key_A_str = self.private_key_entry.get().strip()
        public_key_B_str = self.public_key_B_entry.get().strip()

        if not p_str or not public_key_A_str or not private_key_A_str or not public_key_B_str:
            messagebox.showerror("Помилка", "Будь ласка, заповніть всі поля.")
            return

        try:
            p = int(p_str)
            public_key_A = int(public_key_A_str)
            private_key_A = int(private_key_A_str)
            public_key_B = int(public_key_B_str)
        except ValueError:
            messagebox.showerror("Помилка", "Неправильний формат числа.")
            return

        shared_key = Key_Exchange_DH.exchange_keys(p, public_key_B, private_key_A)
        self.output_text.config(text=str(shared_key))
