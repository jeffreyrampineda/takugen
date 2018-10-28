from translatorHelper import Language

Katakana = Language(__name__)

Katakana._vowels = [' ', 'a', 'e', 'i', 'o', 'u']

Katakana._unicode_table = {
    'a': {
        'primary': '30a2',
        'w': { 'primary': '30ef' },
        'r': { 'primary': '30e9' },
        'y': { 'primary': '30e4' },
        'm': { 'primary': '30de' },
        'h': { 'primary': '30cf' },
        'n': { 'primary': '30ca' },
        't': { 'primary': '30bf' },
        's': { 'primary': '30b5' },
        'k': { 'primary': '30ab' },
        'g': { 'primary': '30ac' },
        'z': { 'primary': '30b6' },
        'd': { 'primary': '30c0' },
        'b': { 'primary': '30d0' },
        'p': { 'primary': '30d1' }
    },
    'b': { 'primary': '0062' },
    'c': { 'primary': '0063' },
    'd': { 'primary': '0064' },
    'e': { 'primary': '30a8' },
    'f': { 'primary': '0066' },
    'g': { 'primary': '0067' },
    'h': { 'primary': '0068' },
    'i': { 'primary': '30a4' },
    'j': { 'primary': '006a' },
    'k': { 'primary': '006B' },
    'm': { 'primary': '006D' },
    'n': { 'primary': '006E' },
    'o': { 'primary': '30aa' },
    'p': { 'primary': '0070' },
    'r': { 'primary': '0072' },
    's': { 'primary': '0073' },
    't': { 'primary': '0074' },
    'u': { 'primary': '30a6' },
    'w': { 'primary': '0077' },
    'y': { 'primary': '0079' },
    'z': { 'primary': '007A' }
}