import tkinter as tk
import threading
from pynput import keyboard
from takugen import Translator
import settings
import hangul
import hiragana
import katakana
 
translator = Translator()
root = tk.Tk()
language_selected_text = tk.StringVar(root)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hangul_button = tk.Button(self, text="Hangul", command= lambda: self.select_language(1))
        self.hangul_button.pack(side="top")

        self.hiragana_button = tk.Button(self, text="Hiragana", command= lambda: self.select_language(2))
        self.hiragana_button.pack(side="top")

        self.katakana_button = tk.Button(self, text="Katakana", command= lambda: self.select_language(3))
        self.katakana_button.pack(side="top")

    def select_language(self, option=0):
        options = {
            1: hangul.Hangul,
            2: hiragana.Hiragana,
            3: katakana.Katakana,
        }

        language = options[option]
        translator.language = language
        language_selected_text.set(language._language)

        TranslatorThread().start()

class TranslatorThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._is_running = False

    def on_press(self, key):

        # do if the program is not typing unicodes
        if not translator.isTypingUnicode and isinstance(key, keyboard._xorg.KeyCode) and language_selected_text.get() != "None":
            try:
                tr_key, tr_unicode = key.char, translator.language._unicode_table[key.char]

                translator.translateKeyPress(tr_key, tr_unicode)
                        
                translator.previousKeys.popleft()
                translator.previousKeys.append(key.char)
            except KeyError:
                print("cannot find key '{0}' in table".format(key.char))
            if settings.APP_CONFIG['DEBUG']:
                print('previousKeys: ' + str(translator.previousKeys))

    def on_release(self, key):
        if key == keyboard.Key.esc:
            language_selected_text.set("None")
            self.stop()
            return False
    def stop(self):
        print("Stopping")
        self._is_running = False
    def run(self):
        print(f'Starting {translator.language._language}')
        self._is_running = True

        while(self._is_running):
            # Collect events until released
            with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
                listener.join()
        print("Task finished")

app = Application(master=root)
app.master.title("Takugen")
app.master.minsize(1000, 400)

tk.Label(root, textvariable=language_selected_text).pack()
language_selected_text.set('None')
app.mainloop()

## TODO: Close/Stop current TranslatorThread when switching between languages
##          - You have to ESC first before switching to another language or will cause error
## TODO: Combine TranslatorThread with Translator