import re

def convert_string(input_string):
    conversion_dict = {
        "DJ": "J",
        "J": "Y",
        "TJ": "C",
        "OE": "U",
        "NJ": "NY",
        "SJ": "SY",
        "CH": "KH"
    }

    pattern = re.compile('|'.join(re.escape(key) for key in conversion_dict.keys()), re.IGNORECASE)
    output_string = pattern.sub(lambda x: conversion_dict[x.group().upper() if x.group().isupper() else x.group().lower()], input_string)

    return output_string