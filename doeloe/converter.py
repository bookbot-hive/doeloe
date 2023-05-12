import re


def transliterate(text):
    mapping = {
        "dj": "j",
        "j": "y",
        "tj": "c",
        "oe": "u",
        "nj": "ny",
        "sj": "sy",
        "ch": "kh",
    }

    for k in list(mapping.keys()):
        mapping[k.capitalize()] = mapping[k].capitalize()

    pattern = re.compile("|".join(re.escape(key) for key in mapping.keys()))
    output_string = pattern.sub(lambda x: mapping[x.group()], text)

    return output_string
