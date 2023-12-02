# Transliterator | Транслитератор

A small utility program to handle transliteration of Bulgarian strings into English. Includes a handy GUI with PySimpleGUI. 


## Project Description

Transliteration is a type of conversion of a text from one script to another that involves swapping letters (thus trans- + liter-) in predictable ways ([Wikipedia](https://en.wikipedia.org/wiki/Transliteration)). This tool allows for transliteration from Cyrillic to Latin character sets according to the [Transliteration Act](https://www.mrrb.bg/static/media/ups/articles/attachments/TRANSLITERATION%20ACT48938c89238d30492f9d6456d4b8ee7e.pdf) of 2009.

This tool provides support for most provisions in the law and allows transliteration of multiline texts by keeping all non-Cyrillic symbols and line breaks in place. Special cases such as the name of the country Bulgaria and words ending with -ия are also handled.


## Installation

Transliterator only has one dependency ([PySimpleGUI](https://www.pysimplegui.org/en/latest/)), which is only required if the GUI of the program is going to be used. If only the transliteration logic is required, this step could be skipped.

To install the requirements in your Virtual Environment:
```
pip install -r requirements.txt
```


## Usage

The program can be used directly by importing the trans module or via the provided GUI.

### Using Transliterator Directly 

```

```


### Using Transliterator's GUI


```

```


## License
The software is released under the GNU General Public License (GPL) which can be found in the main repository directory.