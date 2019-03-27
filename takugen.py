from pynput.keyboard import Key, Controller, Listener
from pynput import keyboard
from collections import deque
import time
import threading
import settings

class Language:
    def __init__(self, language='none', vowels=[], unicode_table={}, hasSecondary=False):
        self._language = language
        self._vowels = vowels
        self._unicode_table = unicode_table
        self._hasSecondary = hasSecondary

class Translator(threading.Thread):
    controller = Controller()
    isTypingUnicode = False
    previousKeys = deque([' ',' ',' '])
    language = None
    previousCharCount = 1
    _is_running = False
    def __init__(self, language):
        threading.Thread.__init__(self)
        self.language = language

    def removeCurrentCharacter(self, currentKey):
        self.controller.release(currentKey)
        self.keyTap(Key.backspace)
        time.sleep(0.1)

    def unicodeTyper(self, tr_unicode):
        self.isTypingUnicode = True

        self.pressCombination(Key.ctrl, Key.shift, 'u')
        self.releaseCombination(Key.ctrl, Key.shift, 'u')
        self.controller.type(tr_unicode)
        self.keyTap(Key.enter)

        self.isTypingUnicode = False
        return

    def pressCombination(self, *keys):
        for key in keys:
            self.controller.press(key)

    def releaseCombination(self, *keys):
        for key in keys:
            self.controller.release(key)

    def translateKeyPress(self, keyPress, tr_unicode):
        tr_unicode = self.checkForCombination(keyPress, tr_unicode)

        tr_unicode = tr_unicode['primary'] if not self.language._hasSecondary else self.selectPrimaryOrSecondary(keyPress, tr_unicode)

        self.removeCurrentCharacter(keyPress)

        # used for single hangul jama
        if len(tr_unicode) == 4:
            self.previousCharCount = 1
            self.unicodeTyper(tr_unicode)

        # used for double hangul jama
        else:
            self.previousCharCount = 2
            self.unicodeTyper(tr_unicode[0:4])
            self.unicodeTyper(tr_unicode[4:])

    def keyTap(self, key):
        self.controller.press(key)
        self.controller.release(key)

    # returns primary or secondary
    def selectPrimaryOrSecondary(self, keyPress, tr_unicode):
        if self.previousKeys[2] in self.language._vowels:
            return tr_unicode['secondary']
        else:
            return tr_unicode['primary']

    def checkForCombination(self, keyPress, tr_unicode):
        # Try for 2-keys combinations
        if self.previousKeys[2] in tr_unicode:
            
            # Try for 3-keys combinations
            if self.previousKeys[1] in tr_unicode[self.previousKeys[2]]:

                # time.sleep() provides enough time for OS to receive backspace event
                if self.previousCharCount == 2:
                    self.keyTap(Key.backspace)
                    time.sleep(0.1)
                self.keyTap(Key.backspace)
                time.sleep(0.1)
                self.keyTap(Key.backspace)
                time.sleep(0.1)

                return tr_unicode[self.previousKeys[2]][self.previousKeys[1]]
            else:
                # time.sleep() provides enough time for OS to receive backspace event
                if self.previousCharCount == 2:
                    self.keyTap(Key.backspace)
                    time.sleep(0.1)
                self.keyTap(Key.backspace)
                time.sleep(0.1)

                return tr_unicode[self.previousKeys[2]]

        # Default to single key press
        else:
            return tr_unicode

    def on_press(self, key):

        # do if the program is not typing unicodes
        if not self.isTypingUnicode and isinstance(key, keyboard._xorg.KeyCode) and not (type(self.language) is None):
            try:
                tr_key, tr_unicode = key.char, self.language._unicode_table[key.char]

                self.translateKeyPress(tr_key, tr_unicode)
                        
                self.previousKeys.popleft()
                self.previousKeys.append(key.char)
            except KeyError:
                print("cannot find key '{0}' in table".format(key.char))
            if settings.APP_CONFIG['DEBUG']:
                print('previousKeys: ' + str(self.previousKeys))

    def on_release(self, key):
        if key == Key.esc:
            self.stop()
            return False
    def stop(self):
        print("Stopping")
        self._is_running = False
    def run(self):
        print(f'Starting {self.language._language}')
        self._is_running = True

        while(self._is_running):
            # Collect events until released
            with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
                listener.join()
        print("Task finished")