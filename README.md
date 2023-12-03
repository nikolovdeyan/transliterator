# Transliterator | Транслитератор

A small utility program to handle transliteration of Bulgarian strings into English. Includes a handy GUI with PySimpleGUI. 


## Project Description

Transliteration is a type of conversion of a text from one script to another that involves swapping letters (thus trans- + liter-) in predictable ways ([Wikipedia](https://en.wikipedia.org/wiki/Transliteration)). This tool allows for transliteration from Cyrillic to Latin character sets according to the [Transliteration Act](https://www.mrrb.bg/static/media/ups/articles/attachments/TRANSLITERATION%20ACT48938c89238d30492f9d6456d4b8ee7e.pdf) of 2009.

This tool provides support for most provisions in the law and allows transliteration of multiline texts by keeping all non-Cyrillic symbols and line breaks in place. Special cases such as the name of the country Bulgaria and words ending with -ия are also handled.

#### Features
- A GUI and console interfaces for performing transliteration.
- Support for basic transliteration rules as described in Art. 4 of the Transliteration Act.
- Support for transliteration rules described in Art.5, Art.6, and Art.7 of the Transliteration Act.

Note that no support is provided for the transliteration rules described in Art.9 of the Transliteration Act. 


## Installation

Transliterator only has one dependency ([PySimpleGUI](https://www.pysimplegui.org/en/latest/)).

To install the requirements in your Virtual Environment:
```
pip install -r requirements.txt
```


## Usage

This program can be used directly by importing the trans module or via the provided GUI.

#### Using Transliterator Directly 

``` python
import transliterator as t

my_text = """
София, 
Ловеч, Пазарджик
Панагюрище,
България,
| 1 | 2 |
| Я | я | 
| Щ | щ |
"""

transliterated_text = t.transliterate(my_text)

print(transliterated_text)
```


#### Using Transliterator's GUI


```
import transliterator as t
t.gui()
```


## License
The software is released under the GNU General Public License (GPL) which can be found in the main repository directory.