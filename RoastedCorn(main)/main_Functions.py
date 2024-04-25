def checkLengthOfStrings(c):
	return len(c)
    
def checkingCharIndex(x,y,z):
    x = ''
    word = "semicolon"
    index = len(word)
    if len(x) < index:
        return word[0], word[1], word[7], word[8]
    if len(y) < index:
        return word[5], word[8], word[7], word[8]
    if len(z) < index:
        return word[5]
        
def suffixToStrings(x,y,z):
    x = ''
    word = "abc"
    word2 = "string"
    word3 = "on"
    index = len(word)
    index2 = len(word2)
    index3 = len(word3)
    if len(x) < index:
        return word + "ing"
    if len(y) < index:
        return word + "ly"
    if len(z) < index:
        return word + "ing"