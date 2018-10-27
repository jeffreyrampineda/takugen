from pynput import keyboard
import translatorHelper
import settings
import hangul
import hiragana

# error - backspace is pressed once extra. cause is unknown
#         cannot pinpoint within the program.
#         must be bug in pynput module

ko_ha = translatorHelper.Language(hangul.name, hangul.vowels, hangul.unicode_table)
ja_hi = translatorHelper.Language(hiragana.name, hiragana.vowels, hiragana.unicode_table)

helper = translatorHelper.TranslatorHelper()
helper.language = ja_hi

def on_press(key):
    if isinstance(key, keyboard._xorg.KeyCode) and key.char == '.':
        print(helper.previousKeys)
    # do if the program is not typing unicodes
    if not helper.isTypingUnicode and isinstance(key, keyboard._xorg.KeyCode):
        try:
            romanKey, tr_unicode = key.char, helper.language._unicode_table[key.char]

            # a consonant
            if romanKey not in helper.language._vowels:
                helper.translateKeyPress(romanKey, tr_unicode)
            # a vowel
            else:
                helper.translateKeyPress(romanKey, tr_unicode)
                    
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