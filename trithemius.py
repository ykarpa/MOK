from cipher import TrithemiusCipher
from main import Main
import tkinter as tk
from tkinter import ttk, Spinbox


class Trithemius(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Шифр Тритеміуса")
        self.geometry("750x500")

        self.trithemius = TrithemiusCipher()

        self.create_input_output_fields()
        self.create_encryption_fields()
        # self.create_radio_buttons()

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
        self.output_text.config(yscrollcommand=output_scrollbar.set)  # , state=tk.DISABLED)

        input_label.grid(row=0, column=0, padx=5, pady=5)
        self.input_text.grid(row=1, column=0, padx=5, pady=5)
        input_scrollbar.grid(row=1, column=1, sticky="ns")
        output_label.grid(row=2, column=0, padx=5, pady=5)
        self.output_text.grid(row=3, column=0, padx=5, pady=5)
        output_scrollbar.grid(row=3, column=1, sticky="ns")

    def create_encryption_fields(self):
        encryption_panel = ttk.Frame(self)
        encryption_panel.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        self.language_var = tk.StringVar(value="english")
        english_radio = ttk.Radiobutton(encryption_panel, text="Англійська", value="english",
                                        variable=self.language_var)
        ukrainian_radio = ttk.Radiobutton(encryption_panel, text="Українська", value="ukrainian",
                                          variable=self.language_var)

        english_radio.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ukrainian_radio.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        operation_var = tk.StringVar(value="encrypt")
        encrypt_radio = ttk.Radiobutton(encryption_panel, text="Зашифрувати", value="encrypt", variable=operation_var)
        decrypt_radio = ttk.Radiobutton(encryption_panel, text="Розшифрувати", value="decrypt", variable=operation_var)

        encrypt_radio.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        decrypt_radio.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Додавання додаткових полів залежно від вибору типу шифрування
        self.coefficient_entries = []
        self.coefficient_entry_labels = []

        def show_coefficient_entries():
            for entry in self.coefficient_entries:
                entry.grid_forget()
            for label in self.coefficient_entry_labels:
                label.grid_forget()
            self.coefficient_entries.clear()
            self.coefficient_entry_labels.clear()

        def on_type_change():
            operation = operation_var.get()
            if self.type_var.get() == "linear":
                show_coefficient_entries()
                for i in range(2):
                    entry_label = ttk.Label(encryption_panel, text=f"Коефіцієнт {self.trithemius.ENG_LETTERS[i]}:")
                    entry_label.grid(row=3 + i, column=0, padx=5, pady=5, sticky="w")
                    entry = ttk.Entry(encryption_panel)
                    entry.grid(row=3 + i, column=1, padx=5, pady=5, sticky="w")
                    self.coefficient_entry_labels.append(entry_label)
                    self.coefficient_entries.append(entry)
            elif self.type_var.get() == "nonlinear":
                show_coefficient_entries()
                for i in range(3):
                    entry_label = ttk.Label(encryption_panel, text=f"Коефіцієнт {self.trithemius.ENG_LETTERS[i]}:")
                    entry_label.grid(row=3 + i, column=0, padx=5, pady=5, sticky="w")
                    entry = ttk.Entry(encryption_panel)
                    entry.grid(row=3 + i, column=1, padx=5, pady=5, sticky="w")
                    self.coefficient_entry_labels.append(entry_label)
                    self.coefficient_entries.append(entry)
            else:
                show_coefficient_entries()
                entry_label = ttk.Label(encryption_panel, text="Гасло:")
                entry_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
                entry = ttk.Entry(encryption_panel)
                entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
                self.coefficient_entry_labels.append(entry_label)
                self.coefficient_entries.append(entry)

        self.type_var = tk.StringVar()
        linear_radio = ttk.Radiobutton(encryption_panel, text="Лінійне", value="linear", variable=self.type_var,
                                       command=on_type_change)
        nonlinear_radio = ttk.Radiobutton(encryption_panel, text="Нелінійне", value="nonlinear", variable=self.type_var,
                                          command=on_type_change)
        password_radio = ttk.Radiobutton(encryption_panel, text="За гаслом", value="password", variable=self.type_var,
                                         command=on_type_change)

        linear_radio.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        nonlinear_radio.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        password_radio.grid(row=2, column=2, padx=5, pady=5, sticky="w")

        execute_button = ttk.Button(encryption_panel, text="Виконати",
                                    command=lambda: self.update_output(operation_var.get()), width=20)
        execute_button.grid(row=10, column=0, columnspan=3, pady=10)

    # def create_radio_buttons(self):
    #     radio_panel = ttk.Frame(self)
    #     radio_panel.grid(row=0, column=1, padx=10, pady=10, sticky="n")
    #
    #     self.radio_var = tk.StringVar(value="enter")
    #
    #     enter_radio = ttk.Radiobutton(radio_panel, text="Ввести", value="enter", variable=self.radio_var,
    #                                   command=self.show_input_entry)
    #     file_radio = ttk.Radiobutton(radio_panel, text="Прочитати з файлу", value="file", variable=self.radio_var,
    #                                  command=self.show_file_input)
    #
    #     enter_radio.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    #     file_radio.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    def update_output(self, operation):
        input_text = self.input_text.get("1.0", tk.END + "-1c")
        type_var = self.type_var.get()
        language = self.language_var.get()

        if type_var == "linear":
            a = int(self.coefficient_entries[0].get())
            b = int(self.coefficient_entries[1].get())
            result = self.trithemius.linear_ab(input_text, a, b, language, operation)
            print(result)
        elif type_var == "nonlinear":
            a = int(self.coefficient_entries[0].get())
            b = int(self.coefficient_entries[1].get())
            c = int(self.coefficient_entries[2].get())
            result = self.trithemius.non_linear_abc(input_text, a, b, c, language, operation)
        else:
            password = self.coefficient_entries[0].get()
            result = self.trithemius.password(input_text, password, language, operation)

        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)
        self.output_text.config(state=tk.DISABLED)