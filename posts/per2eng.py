def per_2_eng(per_str):
    persian_str = per_str
    char_mapping = {
        "آ": "a",
        "ا": "a",
        "ب": "b",
        "پ": "p",
        "ت": "t",
        "ث": "s",
        "ج": "j",
        "چ": "ch",
        "ح": "h",
        "خ": "kh",
        "د": "d",
        "ذ": "z",
        "ر": "r",
        "ز": "z",
        "ژ": "zh",
        "س": "s",
        "ش": "sh",
        "ص": "s",
        "ض": "z",
        "ط": "t",
        "ظ": "z",
        "ع": "a",
        "غ": "gh",
        "ف": "f",
        "ق": "g",
        "ک": "k",
        "گ": "g",
        "ل": "l",
        "م": "m",
        "ن": "n",
        "و": "v",
        "ه": "h",
        "ی": "i"
    }

    eng_str = ''.join([char_mapping[char] if char in char_mapping else char for char in persian_str])

    return eng_str