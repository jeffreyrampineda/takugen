from pynput.keyboard import Key, Controller
from collections import deque
import settings
# import asyncio

# TODO - use async/await for all typings

class Language:
    def __init__(self, language='none', vowels=[], unicode_table={}):
        self._language = language
        self._vowels = vowels
        self._unicode_table = unicode_table

class TranslatorHelper:
    controller = Controller()
    isTypingUnicode = False
    previousKeys = deque([' ',' ',' '])
    language = None

    def removeCurrentCharacter(self, currentKey):
        self.controller.release(currentKey)
        self.keyTap(Key.backspace)

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
        tr_unicode = self.selectPrimaryOrSecondary(keyPress, tr_unicode)

        self.removeCurrentCharacter(keyPress)

        # used for single hangul jama
        if len(tr_unicode) == 4:
            self.unicodeTyper(tr_unicode)

        # used for double hangul jama
        else:
            self.unicodeTyper(tr_unicode[0:4])
            self.unicodeTyper(tr_unicode[4:])

    def keyTap(self, key):
        self.controller.press(key)
        self.controller.release(key)

    # returns primary or 
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
                return tr_unicode[self.previousKeys[2]][self.previousKeys[1]]
            else:
                return tr_unicode[self.previousKeys[2]]

        # Default to single key press
        else:
            return tr_unicode