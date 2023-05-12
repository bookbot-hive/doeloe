import re

def transliterate(input_string):
    conversion_dict = {
        "dj": "j",
        "j": "y",
        "tj": "c",
        "oe": "u",
        "nj": "ny",
        "sj": "sy",
        "ch": "kh"
    }

    pattern = re.compile('|'.join(re.escape(key) for key in conversion_dict.keys()), re.IGNORECASE)
    output_string = pattern.sub(lambda x: conversion_dict[x.group().lower() if x.group().islower() else x.group().upper()], input_string)

    return output_string