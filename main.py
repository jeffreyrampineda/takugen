from pynput import keyboard
from takugen import Translator
import settings
import hangul
import hiragana
import katakana
 
translator = Translator()
translator.language = hiragana.Hiragana

print('Takugen running... ESC to quit')

def on_press(key):

    # do if the program is not typing unicodes
    if not translator.isTypingUnicode and isinstance(key, keyboard._xorg.KeyCode):
        try:
            tr_key, tr_unicode = key.char, translator.language._unicode_table[key.char]

            translator.translateKeyPress(tr_key, tr_unicode)
                    
            translator.previousKeys.popleft()
            translator.previousKeys.append(key.char)
        except KeyError:
            print("cannot find key '{0}' in table".format(key.char))
        if settings.APP_CONFIG['DEBUG']:
            print('previousKeys: ' + str(translator.previousKeys))

def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()