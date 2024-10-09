+++
title = 'blockbuster'
date = 2024-09-30T04:21:35+05:30
draft = false
+++

recently, while watching the music video for faris shafi's [blockbuster](https://www.youtube.com/watch?v=-urTPhh7gNk), i noticed something interesting. the song was in punjabi, but the subtitles (and even the hoardings and other text) on the screen were in the arabic script.

it struck me then that punjabi is quite a unique language, as it's written in two different scripts: shahmukhi (used mainly in pakistan) and gurmukhi (used mainly in india). i can understand some gurmukhi punjabi, but shahmukhi remains a mystery to me. yet, since the two scripts represent the same sounds, it should be possible to transliterate one into the other. might be worth exploring.


# how?

- define phoneme mappings between shahmukhi and gurumukhi.
- write a python function to perform the conversion.
- use an example to illustrate the process.


# shahmukhi phoneme mapping

```
shahmukhi_to_phoneme = {
    'ا': 'a',
    'ب': 'b',
    'پ': 'p',
    'ت': 't',
    'ٹ': 'ṭ',
    'ث': 's',
    'ج': 'j',
    'چ': 'c',
    'ح': 'h',
    'خ': 'kh',
    'د': 'd',
    'ڈ': 'ḍ',
    'ذ': 'z',
    'ر': 'r',
    'ڑ': 'ṛ',
    'ز': 'z',
    'ژ': 'zh',
    'س': 's',
    'ش': 'sh',
    'ص': 's',
    'ض': 'z',
    'ط': 't',
    'ظ': 'z',
    'ع': 'a',
    'غ': 'gh',
    'ف': 'f',
    'ق': 'q',
    'ک': 'k',
    'گ': 'g',
    'ل': 'l',
    'م': 'm',
    'ن': 'n',
    'و': 'o',
    'ہ': 'h',
    'ء': 'a',
    'ی': 'y',
    'ے': 'e',
    'َ': 'a',   
    'ِ': 'i',  
    'ُ': 'u', 
}
```


# gurumukhi phoneme mapping

```
# Phoneme to Gurmukhi mapping
phoneme_to_gurmukhi = {
    'a': 'ਅ',
    'aa': 'ਆ',
    'i': 'ਇ',
    'ii': 'ਈ',
    'u': 'ਉ',
    'oo': 'ਊ',
    'e': 'ਏ',
    'ai': 'ਐ',
    'o': 'ਓ',
    'au': 'ਔ',
    'k': 'ਕ',
    'kh': 'ਖ',
    'g': 'ਗ',
    'gh': 'ਘ',
    'ng': 'ਙ',
    'c': 'ਚ',
    'ch': 'ਛ',
    'j': 'ਜ',
    'jh': 'ਝ',
    'ny': 'ਞ',
    'ṭ': 'ਟ',
    'ṭh': 'ਠ',
    'ḍ': 'ਡ',
    'ḍh': 'ਢ',
    'ṇ': 'ਣ',
    't': 'ਤ',
    'th': 'ਥ',
    'd': 'ਦ',
    'dh': 'ਧ',
    'n': 'ਨ',
    'p': 'ਪ',
    'ph': 'ਫ',
    'b': 'ਬ',
    'bh': 'ਭ',
    'm': 'ਮ',
    'y': 'ਯ',
    'r': 'ਰ',
    'l': 'ਲ',
    'v': 'ਵ',
    'sh': 'ਸ਼',
    'ṣ': 'ਸ',
    'h': 'ਹ',
    'ḷ': 'ਲ਼',
    'ṛ': 'ੜ',
    'f': 'ਫ਼',
    'z': 'ਜ਼',
    'x': 'ਖ਼',
    'ɣ': 'ਗ਼',
    'q': 'ਕ਼',
}
```

# transliteration

using simple python dict lookups we can perform some rudimentary transliteration.

for instance first line of the song: شہر وچ چر چے نے
is converted into: ਸ਼ਹਰ ਵਿੱਚ ਚਰਚੇ ਨੇ (sheher vich charche ne) (there are discussions in the town)

# thoughts

dictionary lookups is a pretty straightforward idea to solve the problem, though it's not without its challenges. one of the key hurdles comes from the way [implicit vowels](https://learnpunjabi.org/pdf/gslehal-pap24.pdf) are handled in shahmukhi. but despite these limitations, it feels like a good first step in tackling this problem. should set up proper evaluation on some toy dataset and build further.






