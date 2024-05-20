import json
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

        x = (screen_width - 700) // 2
        y = (screen_height - 500) // 2

        self.geometry("700x500+{}+{}".format(x, y))

        self.button_frame = tk.Frame(self)
        self.button_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.create_buttons()

    def create_buttons(self):
        button_functions = [self.caesar_cipher, self.trithemius_cipher, self.xor_cipher, self.knapsack_cipher, self.rsa_cipher, self.dh_key_exchange]

        for i, button_text in enumerate(["Шифр Цезаря", "Шифр Тритеміуса", "Шифр Гамування", "Задача рюкзака", "Шифр RSA", "Обмін ключами Діффі-Гелмана"]):
            button = tk.Button(self.button_frame, text=button_text, command=button_functions[i], width=30, height=2, background="lightgrey")
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
        self.destroy()
        from xor import XOR
        app = XOR()
        app.mainloop()

    def knapsack_cipher(self):
        self.destroy()
        from knapsack import KnapsackTask
        app = KnapsackTask()
        app.mainloop()

    def rsa_cipher(self):
        self.destroy()
        from rsa import RSA
        app = RSA()
        app.mainloop()

    def dh_key_exchange(self):
        self.destroy()
        from dh import DH
        app = DH()
        app.mainloop()

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

    def build_frequency_table(self, language):
        frequency_table = Counter()

        if language == "english":
            with open("english_frequencies.json", "r", encoding="utf-8") as file:
                frequency_table.update(json.load(file))
        else:
            with open("ukrainian_frequencies.json", "r", encoding="utf-8") as file:
                frequency_table.update(json.load(file))

        return frequency_table

    def show_statistics_window(self):
        stats_window = tk.Toplevel(self)
        stats_window.title("Статистика частот літер")

        language_frame = ttk.Frame(stats_window)
        language_frame.grid(row=0, column=0, padx=5, pady=5)

        english_button = ttk.Button(language_frame, text="Англійська", width=15, command=lambda: self.display_frequency_table(self.build_frequency_table("english")))
        english_button.grid(row=0, column=0)

        ukrainian_button = ttk.Button(language_frame, text="Українська", width=15, command=lambda: self.display_frequency_table(self.build_frequency_table("ukrainian")))
        ukrainian_button.grid(row=0, column=1)

        self.text_widget = tk.Text(stats_window, width=30, height=20, wrap=tk.WORD)
        self.text_widget.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(stats_window, orient=tk.VERTICAL, command=self.text_widget.yview)
        self.scrollbar.grid(row=1, column=1, sticky="ns")
        self.text_widget.config(yscrollcommand=self.scrollbar.set)

    def display_frequency_table(self, frequency_table):
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert(tk.END, "   Літера\t\tЧастота\n")
        self.text_widget.insert(tk.END, "-----------------------------\n")

        for char, frequency in frequency_table.items():
            self.text_widget.insert(tk.END, f"     {char}\t\t {frequency}%\n")

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
