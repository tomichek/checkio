"""
checkio elementary mission even the last.

You are given an array of integers.
You should find the sum of the elements with even indexes (0th, 2nd, 4th...)
then multiply this summed number and the final element of the array together.
Don't forget that the first element has an index of 0.

For an empty array, the result will always be 0 (zero).

Input: A list of integers.

Output: The number as an integer.
"""

def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    #if there is an array
    if array:
    	#return the sum of even indexes and multiply them with the last number
        return sum(array[::2]) * array[-1]
    #if array empty return 0
    return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"