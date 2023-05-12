# Doeloe
 A library to convert old Indonesian language into EYD (Ejaan yang Disempurnakan)

## Install Doeloe
Install from PyPI
```
pip install doeloe
```
Editable install from Source
```
git clone https://github.com/bookbot-hive/doeloe.git
pip install -e doeloe
```

## Usage

``` py
>>> from doeloe import transliterate
>>> input_text = "Konon oeang - oeang repoeblik dibawa kaboer ke soerabaja."
>>> transliterate(input_text)
'Konon uang - uang republik dibawa kabur ke surabaya'
```
