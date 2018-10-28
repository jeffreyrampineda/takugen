from translatorHelper import Language

Hiragana = Language(__name__)

Hiragana._vowels = [' ', 'a', 'e', 'i', 'o', 'u']

Hiragana._unicode_table = {
    'a': {
        'primary': '3042',
        'w': { 'primary': '308f' },
        'r': { 'primary': '3089' },
        'y': { 'primary': '3084' },
        'm': { 'primary': '307e' },
        'h': { 'primary': '306f' },
        'n': { 'primary': '306a' },
        't': { 'primary': '305f' },
        's': { 'primary': '3055' },
        'k': { 'primary': '304b' },
        'g': { 'primary': '304c' },
        'z': { 'primary': '3056' },
        'd': { 'primary': '3060' },
        'b': { 'primary': '3070' },
        'p': { 'primary': '3071' }
    },
    'b': { 'primary': '0062' },
    'c': { 'primary': '0063' },
    'd': { 'primary': '0064' },
    'e': { 'primary': '3048' },
    'f': { 'primary': '0066' },
    'g': { 'primary': '0067' },
    'h': { 'primary': '0068' },
    'i': { 'primary': '3044' },
    'j': { 'primary': '006a' },
    'k': { 'primary': '006B' },
    'm': { 'primary': '006D' },
    'n': { 'primary': '006E' },
    'o': { 'primary': '304a' },
    'p': { 'primary': '0070' },
    'r': { 'primary': '0072' },
    's': { 'primary': '0073' },
    't': { 'primary': '0074' },
    'u': { 'primary': '3046' },
    'w': { 'primary': '0077' },
    'y': { 'primary': '0079' },
    'z': { 'primary': '007A' }
}