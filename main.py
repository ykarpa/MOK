import tkinter as tk
from tkinter import ttk, Spinbox, filedialog, messagebox
from tkinter import Toplevel, Label, colorchooser
from collections import Counter

from PIL import Image, ImageTk


class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("МОК")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Розрахунок координат верхнього лівого кута вікна для розміщення його у центрі
        x = (screen_width - 700) // 2
        y = (screen_height - 500) // 2

        # Встановлення розмірів та позиції вікна
        self.geometry("700x500+{}+{}".format(x, y))

        # Створення контейнера для кнопок
        self.button_frame = tk.Frame(self)
        self.button_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.create_buttons()  # Створення кнопок

    def create_buttons(self):
        # Функції для обробки натискань кнопок
        button_functions = [self.caesar_cipher, self.trithemius_cipher, self.xor_cipher]

        # Створення кнопок і розміщення їх у вікні
        for i, button_text in enumerate(["Шифр Цезаря", "Шифр Тритеміуса", "Шифр Гамування"]):
            button = tk.Button(self.button_frame, text=button_text, command=button_functions[i], width=20, height=2)
            button.grid(row=i, column=0, pady=10)

    def caesar_cipher(self):
        self.destroy()
        from caesar import Caesar
        app = Caesar()
        app.mainloop()

    def trithemius_cipher(self):
        self.destroy()
        from trithemius import Trithemius
        app = Trithemius()
        app.mainloop()

    def xor_cipher(self):
        # Додати код для реалізації шифру Гамування
        pass

        # Додаткові методи для обробки команд меню

    def create_file(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                file_content = file.read()
                self.input_text.delete("1.0", tk.END)
                self.input_text.insert(tk.END, file_content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            encrypted_text = self.output_text.get("1.0", tk.END)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(encrypted_text)

    def print_file(self):
        print_text = self.output_text.get("1.0", tk.END)
        print_text = print_text.strip()

        print_window = tk.Toplevel(self)
        print_window.title("Друк файлу")

        print_text_widget = tk.Text(print_window, height=10, width=40)
        print_text_widget.insert(tk.END, print_text)
        print_text_widget.pack(padx=10, pady=10)

        print_button = ttk.Button(print_window, text="Друкувати", command=lambda: self.print_text(print_text_widget))
        print_button.pack(pady=10)

    def print_text(self, text_widget):
        text_to_print = text_widget.get("1.0", tk.END)
        print("Друкуємо текст:\n", text_to_print)

    def show_statistics(self):
        input_text = self.input_text.get("1.0", tk.END + "-1c")
        language = self.language_var.get()

        if language == "english":
            frequency_table = self.build_frequency_table(input_text, "english")
        else:
            frequency_table = self.build_frequency_table(input_text, "ukrainian")

        self.show_statistics_window(frequency_table)


    def build_frequency_table(self, text, language):
        frequency_table = Counter()
        total_letters = 0

        if language == "english":
            alphabet = "abcdefghijklmnopqrstuvwxyz"
        else:  # Ukrainian
            alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

        for char in alphabet:
            frequency_table[char.lower()] = 0

        for char in text:
            if char.lower() in alphabet:
                frequency_table[char.lower()] += 1
                total_letters += 1

        for char in frequency_table:
            frequency_table[char] /= total_letters if total_letters > 0 else 1

        return frequency_table

    def show_statistics_window(self, frequency_table):
        stats_window = Toplevel(self)
        stats_window.title("Статистика частот літер")

        text_widget = tk.Text(stats_window, width=30, height=20, wrap=tk.WORD)
        text_widget.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        text_widget.insert(tk.END, "Літера\t\tЧастота\n")
        text_widget.insert(tk.END, "-----------------------------\n")

        for char, frequency in frequency_table.items():
            text_widget.insert(tk.END, f"{char}\t\t{frequency:.2%}\n")

        scrollbar = ttk.Scrollbar(stats_window, orient=tk.VERTICAL, command=text_widget.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        text_widget.config(yscrollcommand=scrollbar.set)

    def show_developer_info(self):
        dev_info_window = Toplevel(self)
        dev_info_window.title("Developer Info")
        dev_info_window.geometry("300x300")

        label = Label(dev_info_window, text="Карпа Юрій\nГрупа ПМІ-36\nGitHub - ykarpa")
        label.pack(pady=10)

        image_path = "./img/my_photo.jpg"
        try:
            original_image = Image.open(image_path)
            resized_image = original_image.resize((200, 200), Image.LANCZOS)
            photo = ImageTk.PhotoImage(resized_image)

            image_label = Label(dev_info_window, image=photo)
            image_label.image = photo
            image_label.pack(pady=10)
        except Exception as e:
            print(f"Error loading image: {e}")

    def confirm_exit(self):
        result = messagebox.askyesno("Підтвердження виходу", "Ви впевнені, що хочете вийти?")
        if result:
            self.destroy()


if __name__ == "__main__":
    app = Main()
    app.mainloop()
