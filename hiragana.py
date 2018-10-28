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
    'i': { 
        'primary': '3044',
        'w': { 'primary': '3090' },
        'r': { 'primary': '308a' },
        'm': { 'primary': '307f' },
        'h': { 
            'primary': '3072',
            'c': { 'primary': '3061' },
            's': { 'primary': '3057' },
        },
        'n': { 'primary': '306b' },
        'k': { 'primary': '304d' },
        'g': { 'primary': '304e' },
        'j': { 'primary': '3058' },
        'd': { 'primary': '3062' },
        'b': { 'primary': '3073' },
        'p': { 'primary': '3074' }
    },
    'u': { 
        'primary': '3046',
        'r': { 'primary': '308b' },
        'y': { 'primary': '3086' },
        'm': { 'primary': '3080' },
        'f': { 'primary': '3075' },
        'n': { 'primary': '306c' },
        's': { 
            'primary': '3059',
            't': { 'primary': '3064' },
        },
        'k': { 'primary': '304f' },
        'g': { 'primary': '3050' },
        'z': { 'primary': '305a' },
        'd': { 'primary': '3065' },
        'b': { 'primary': '3076' },
        'p': { 'primary': '3077' }
    },
    'b': { 'primary': '0062' },
    'c': { 'primary': '0063' },
    'd': { 'primary': '0064' },
    'e': { 'primary': '3048' },
    'f': { 'primary': '0066' },
    'g': { 'primary': '0067' },
    'h': { 'primary': '0068' },
    'j': { 'primary': '006a' },
    'k': { 'primary': '006B' },
    'm': { 'primary': '006D' },
    'n': { 'primary': '006E' },
    'o': { 'primary': '304a' },
    'p': { 'primary': '0070' },
    'r': { 'primary': '0072' },
    's': { 'primary': '0073' },
    't': { 'primary': '0074' },
    'w': { 'primary': '0077' },
    'y': { 'primary': '0079' },
    'z': { 'primary': '007A' }
}