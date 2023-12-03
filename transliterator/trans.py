"""
Main transliterator logic.
"""
import re


def transliterate(text: str) -> str:
    """
    Transliterate a string according to the Bulgarian standard.

    :param str text: The text to be transliterated.
    :returns: The transliterated text.
    :rtype: str
    """
    bg_ch_basic = ("абвгдезийклмнопрстфхуАБВГДЕЗИЙКЛМНОПРСТФХУ",
                   "abvgdeziyklmnoprstfhuABVGDEZIYKLMNOPRSTFHU")
    bg_ch_composite = {
        "ж": "zh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "sht",
        "ъ": "a",
        "ь": "y",
        "ю": "yu",
        "я": "ya",
        "Ж": "Zh",
        "Ц": "Ts",
        "Ч": "Ch",
        "Ш": "Sh",
        "Щ": "Sht",
        "Ъ": "A",
        "Ь": "Y",
        "Ю": "Yu",
        "Я": "Ya",
    }

    special_cases = {
        "България": "Bulgaria",
    }

    # Prepare translation table
    basic_chars = str.maketrans(*bg_ch_basic)
    composite_chars = str.maketrans(bg_ch_composite)
    transl_table = {**basic_chars, **composite_chars}

    # Handle new lines:
    transliterated_lines = []
    for line in text.splitlines():
        # Handle words that are special cases:
        transl_raw = [
            special_cases.get(w)
            if w in special_cases
            else w
            for w in re.split(r"(\W)", line)
        ]
        # Translate words in line
        transl_raw = [w.translate(transl_table) for w in transl_raw]
        # Handle words that end with "iya":
        transl_list = [w[:-3]+"ia" if w[-3:] == "iya" else w for w in transl_raw]
        transliterated_lines.append("".join(transl_list))

    transliterated_text = "\n".join(transliterated_lines)

    return transliterated_text
