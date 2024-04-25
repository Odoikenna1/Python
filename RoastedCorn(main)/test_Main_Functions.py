from main_Functions import checkLengthOfStrings
from main_Functions import checkingCharIndex
from main_Functions import suffixToStrings


def test_checkLengthOfStrings_function():
    assert checkLengthOfStrings("") == 0
    assert checkLengthOfStrings(" ") == 1
    assert checkLengthOfStrings("hello") == 5
    assert checkLengthOfStrings(" hello ") == 7
    assert checkLengthOfStrings("!@#$%") == 5
   
def test_checkingCharIndex():
    assert checkingCharIndex("Semicolon") == ("s","e","o","n")
    assert checkingCharIndex("Semicolon") == ("o","n","o","n")
    assert checkingCharIndex("Semicolon") == ("o")
    
def test_suffixToStrings():
    assert suffixToStrings("abc") == "abcing"
    assert suffixToStrings("string") == "stringly"
    assert suffixToStrings("on") == "oning"