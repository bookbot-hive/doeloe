# Doeloe

A library to convert old Indonesian Republican Spelling System (Edjaan Repoeblik) into EYD (Ejaan yang Disempurnakan).

## Install Doeloe

Install from PyPI

```sh
pip install doeloe
```

Editable install from Source

```sh
git clone https://github.com/bookbot-hive/doeloe.git
pip install -e doeloe
```

## Usage

```py
>>> from doeloe import transliterate
>>> transliterate("Konon oeang - oeang repoeblik dibawa kaboer ke Djakarta.")
"Konon uang - uang republik dibawa kabur ke Jakarta."
>>> transliterate("Soerabaja adalah tjontoh kota jang biasanja dikoendjoengi Sjamsoedin pada achir tahoen.")
"Surabaya adalah contoh kota yang biasanya dikunjungi Syamsudin pada akhir tahun."
```

## References

```bibtex
@misc{Doeloe2018,
  author = {Yuka Langbuana},
  title = {Doeloe},
  year = {2018},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/YukaLangbuana/Doeloe}}
}
```