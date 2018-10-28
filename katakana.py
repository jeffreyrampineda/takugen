from translatorHelper import Language

Katakana = Language(__name__)

Katakana._vowels = [' ', 'a', 'e', 'i', 'o', 'u']

Katakana._unicode_table = {
    'a': {
        'primary': '30a2',
        'w': { 'primary': '30ef' }
    },
    'e': { 'primary': '30a8' },
    'i': { 'primary': '30a4' },
    'o': { 'primary': '30aa' },
    'u': { 'primary': '30a6' },
    'w': { 'primary': '0077' }
}