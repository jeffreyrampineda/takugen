import tkinter as tk
from pynput import keyboard
from takugen import Translator
import hangul
import hiragana
import katakana
 
root = tk.Tk()
language_selected_text = tk.StringVar(root)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hangul_button = tk.Button(self, text="Hangul", command= lambda: self.select_language(0))
        self.hangul_button.pack(side="top")

        self.hiragana_button = tk.Button(self, text="Hiragana", command= lambda: self.select_language(1))
        self.hiragana_button.pack(side="top")

        self.katakana_button = tk.Button(self, text="Katakana", command= lambda: self.select_language(2))
        self.katakana_button.pack(side="top")

    def select_language(self, option=0):
        options = [
            hangul.Hangul,
            hiragana.Hiragana,
            katakana.Katakana,
        ]

        language = options[option]
        language_selected_text.set(language._language)

        Translator(language).start()

app = Application(master=root)
app.master.title("Takugen")
app.master.minsize(200, 200)

tk.Label(root, textvariable=language_selected_text).pack()
language_selected_text.set('None')
app.mainloop()

## TODO: Close/Stop current TranslatorThread when switching between languages
##          - You have to ESC first before switching to another language or will cause error