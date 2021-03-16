"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print each item in the given array.

    Ex.:
    >>> output_all_items([1, 'hello', True])
    1
    hello
    True
    """

    for item in items:
        print(item)


def get_all_evens(nums):
    """Given an array of numbers, return an array of all even numbers.

    Ex.:
    >>> get_all_evens([7, 8, 10, 1, 2, 2])
    [8, 10, 2, 2]
    """

    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums


def get_odd_indices(items):
    """ Given an array, return all elements at odd numbered indices.

    Ex.:
    >>> get_odd_indices([1, 'hello', True, 500])
    ['hello', 500]
    """

    result = []

    for i in range(len(items)):
        if i % 2 != 0:
            result.append(items[i])
    
    return result


def print_as_numbered_list(items):
    """Given an array, output a numbered list.

    Ex.:
    >>> print_as_numbered_list([1, 'hello', True])
    1. 1
    2. hello
    3. True
    """

    i = 1

    for item in items:
        print(f"{i}. {item}")
        i += 1


def get_range(start, stop):
    """Return an array of numbers in a certain range.

    Ex.:
    >>> get_range(0, 5)
    [0, 1, 2, 3, 4]

    >>> get_range(1, 3)
    [1, 2]
    """
    nums = []

    for num in range(start, stop):
        nums.append(num)
    print(nums)


def censor_vowels(word):
    """Given a string, return a string where vowels are replaced with '*'.

    Ex.:
    >>> censor_vowels('hello world')
    'h*ll* w*rld'
    """

    chars = []

    for letter in word:
        if letter in "aeiou":
            chars.append("*")
        else:
            chars.append(letter)
    
    return "".join(chars)


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
