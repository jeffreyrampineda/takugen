from pynput import keyboard
import translatorHelper
import settings
import hangul
import hiragana
import katakana

helper = translatorHelper.TranslatorHelper()
helper.language = hiragana.Hiragana

def on_press(key):
    if isinstance(key, keyboard._xorg.KeyCode) and key.char == '.':
        print(helper.previousKeys)
    # do if the program is not typing unicodes
    if not helper.isTypingUnicode and isinstance(key, keyboard._xorg.KeyCode):
        try:
            tr_key, tr_unicode = key.char, helper.language._unicode_table[key.char]

            helper.translateKeyPress(tr_key, tr_unicode)
                    
            helper.previousKeys.popleft()
            helper.previousKeys.append(key.char)
        except KeyError:
            print("cannot find key '{0}' in table".format(key.char))
        if settings.APP_CONFIG['DEBUG']:
            print('previousKeys: ' + str(helper.previousKeys))

def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()