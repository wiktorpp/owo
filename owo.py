from random import choice

prefixes = [
    '<3 ',
    '0w0 ',
    'H-hewwo?? ',
    'HIIII! ',
    'Haiiii! ',
    'Huohhhh. ',
    'OWO ',
    'OwO ',
    'UwU '
]

suffixes = [
    ' ( ͡° ᴥ ͡°)',
    ' (´・ω・｀)',
    ' (ʘᗩʘ\')',
    ' (இωஇ )',
    ' (๑•́ ₃ •̀๑)',
    ' (• o •)',
    ' (⁎˃ᆺ˂)',
    ' (╯﹏╰）',
    ' (●´ω｀●)',
    ' (◠‿◠✿)',
    ' (✿ ♡‿♡)',
    ' (❁´◡`❁)',
    ' (　\'◟ \')',
    ' (人◕ω◕)',
    ' (；ω；)',
    ' (｀へ´)',
    ' ._.',
    ' :3',
    ' :D',
    ' :P',
    ' ;-;',
    ' ;3',
    ' ;_;',
    ' <{^v^}>',
    ' >_<',
    ' >_>',
    ' UwU',
    ' XDDD',
    ' ^-^',
    ' ^_^',
    ' x3',
    ' x3',
    ' xD',
    ' ÙωÙ',
    ' ʕʘ‿ʘʔ',
    ' ㅇㅅㅇ',
    ', fwendo',
    '（＾ｖ＾）',
]

substitutions = {
    'r': 'w',
    'l': 'w',
    'R': 'W',
    'L': 'W',
  #  'ow': 'OwO',
    'no': 'nu',
    'has': 'haz',
    'have': 'haz',
    ' says': ' sez',
    'you': 'uu',
    'the ': 'da ',
    'The ': 'Da ',
    'THE ': 'THE ',
}

def owo(text, addAffixes=False):
    if addAffixes == True:
        text = f"{choice(prefixes)}{text}{choice(suffixes)}"
    for key, value in substitutions.items():
        text = text.replace(key, value)
    return text