"""
checkio elementary mission three-words
Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by whitespaces (one space).
The words contains only letters.
You should check if the string contains three words in succession.
For example, the string "start 5 one two three 7 end" contains three words in succession.

Input: A string with words.

Output: The answer as a boolean.
"""
def checkio(words):
"""
function counting if there is three words in succession
"""
	#Counter.
    compteur = 0
    #Loop to split text.
    for word in words.split():
    	#If word is alpha counter increments.
        compteur = (compteur + 1) * word.isalpha()
        #If counter eqauls to 3 return True.
        if compteur == 3: 
            return True
    # if word not aplha or counter not equal to 3.
    else: 
    	return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"