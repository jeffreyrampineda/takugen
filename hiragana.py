from translatorHelper import Language

Hiragana = Language(__name__)

Hiragana._vowels = [' ', 'a', 'e', 'i', 'o', 'u']

Hiragana._unicode_table = {
    'a': {
        'primary': '3042',
        'secondary': '3042',
        'w': {
            'primary': '308f',
            'secondary': '308f'
        }
    },
    'e': {
        'primary': '3048',
        'secondary': '3048',
    },
    'i': {
        'primary': '3044',
        'secondary': '3044',
    },
    'o': {
        'primary': '304a',
        'secondary': '304a',
    },
    'u': {
        'primary': '3046',
        'secondary': '3046',
    },
    'w': {
        'primary': '0077',
        'secondary': '0077'
    }
}