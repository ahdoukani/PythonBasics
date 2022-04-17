import datetime
from fractions import Fraction
from abc import ABC, abstractmethod
from typing import Protocol
from dataclasses import dataclass
import numpy as np
import tensor as Tensor
import filters
from typing import Sequence

# from scipy import signal
# Printing strings -----------------------------------------------------------------------------------------------------

"""formatted string literals aka f-strings """


def printing_strings_f_string():
    year = 2020
    event = 'summersale'
    revenue = 952000
    store = "Harrods"
    print(f'{store} made £{revenue} in their {year} {event}.')


"""The string format Method .format"""


def printing_strings_format():
    # .format(args*,**kwargs). takes arguments and keyword argumnts indicated by asterisk
    #  **coord refers to the key word argument, kwarg named coord.
    # coord is a dictionary- you can access dictionary values through their key words and format in place
    # of a string

    coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
    print('Coordinates: {latitude}, {longitude}'.format(**coord))

    # ---Practice using format specifiers---
    # implicit positional arguments- the position of the {} corresponds to the position of th argument in .format()
    name = 'houcine'
    reverse_name = 'enicuoh'
    print('the reverse of {} is {}'.format(name, reverse_name))

    # here ive also impicitly indicated the position of argument to be used but i am accessing each character in the string
    # variable
    name = 'houcine'
    print('the reverse of {} is {}{}{}{}{}{}{}'.format(name, name[6], name[5], name[4], name[3], name[2], name[1],
                                                       name[0]))
    # explicit positional arguments - {number} refers to position of argument in .format()...so {7} is name[0] which is 'h'

    name = 'houcine'
    print('the spelling of {0} is {7}-{6}-{5}-{4}-{3}-{2}-{1}'.format(name, name[6], name[5], name[4], name[3], name[2],
                                                                      name[1], name[0]))

    # here im using items of arguments
    # the number inside curly brackets  but outside square brackets refers to position of the argument in .format()... 0
    # the number in the square bracket refers to the position of the item in the argument..[1] and [2]
    vector = (1, 2, 3, 4)
    print('the second and third value of the vector {0} is {0[1]} and {0[2]} respectively'.format(vector))

    # accessing an argument's attributes of objects

    # regular class objects


class Fruit:
    def __init__(self, name, colour):
        self.name, self.colour = name, colour

    #  printing the return of regular method with parameters
    #      notice the 'self=self' built in argument for .format()
    #      the RHS self is the local var in the method or method parameter-'self' refers to any class member variable
    #      the RHS Doesnt need to be 'self', it can be any object identifier you pass
    #      the LHS self is the identifier (variable name) in the format string in this case the self in {self.name} or
    #      {self.colour}
    #      the RHS can be something other than self.. check main to see an example of this
    #      more simply:  LHS = part of string to to format, RHS = Variable to replace that part of string

    def describe_fruit(self):
        return 'fruit name: {self.name}, fruit colour: {self.colour}'.format(self=self)

    #  defining the __str__ dunder to return a string

    def __str__(self):
        return 'fruit name: {self.name}, fruit colour: {self.colour}'.format(self=self)

    # using {!r} (repr()  shows the quotes , using and {!s} (string) doesnt show the quotes.
    # remember 0 refers to the position of argument of the .format() function


def using_r_and_s():
    return 'greeting with quotes: {0!r}, greeting without quotes: {0!s}'.format('hello')

    # aligning text


def alignment():
    text = 'text to align'
    # left align uses ":<"
    # the value "30" refers to the width of the line
    print('{:<30}'.format(text))
    # right align uses ":>"
    # the value "30" refers to the width of the line
    print('{:>30}'.format(text))
    # central align uses ":^"
    # the value "30" refers to the width of the line
    print('{:^30}'.format(text))
    # central align with '*' as a filler for the spaces uses "*:^"
    # the value "30" refers to the width of the line
    print('{:*^30}'.format(text))  # use '*' as a fill char

    # showing positive and (or) negative signs on numbers


def number_signs():
    # show both signs always)
    print('{:+f}; {:+f}'.format(3.14, -3.14))
    # show a space for positive numbers and shows negative sign)
    print('{: f}; {: f}'.format(3.14, -3.14))
    # show only the minus -- same as '{:f}; {:f} except no space for positive numbers ')
    print('{:-f}; {:-f}'.format(3.14, -3.14))

    # changing numbers to decimal, hexadecimal, octal and  binary
    # must specify the position of argument of .format() method


def changing_number_type():
    number = 1992

    print('dec: {0:d}, hex: {0:x}, oct: {0:o}, bin: {0:b} '.format(number))

    # with 0x, 0o, or 0b as prefix:
    print('dec: {0:d}, hex: {0:#x}, oct: {0:#o}, bin: {0:#b} '.format(number))


def applying_number_commas():
    number2 = 1263463245
    # using a comma to separate thousands, {:,}
    print('{:,}'.format(number2))

    # expressing a percentage with the level of precision


def expressing_percentages():
    number3 = 35729
    number4 = 2256
    fraction = number4 / (number3 + number4)
    # this expresses value to format as a percentage with 2 decimal place precision
    print('The percentage is: {:.2%}'.format(fraction))
    # this expresses value to format as a percentage with 3 decimal place precision
    print('The percentage is: {:.3%}'.format(fraction))

    # using type specific formatting, you must fist import 'datetime module'
    # (Minor units of time)  %m, month and %d day. (Major units of time) :Y  YEAR, :%H HOUR, :%M MINUTE, :%S SECOND

    d = datetime.datetime(2010, 7, 4, 12, 15, 58)
    '{:%Y-%m-%d %H:%M:%S}'.format(d)

    # nested formatting using loops: notice the nested curley brackets


def nested_formatting_arguments():
    # takes align to be '<^>' and text to be ['left', 'center', 'right'],...
    # then applies the following print instruction to items of corresponding position
    # 0 stands for argument position to format in .format() function, this refers to the item from 'text'
    # {fill} is substituted with the item from 'align'
    # {align} is substituted with the item from 'align'
    # notice the nested curley brackets: all inner curley brackets are applied to the result of outer curly brackets
    # 16 is a value specifying the width of string
    for align, text in zip('<^>', ['left', 'center', 'right']):
        print('{0:{fill}{align}16}'.format(text, fill=align, align=align))


"""Manual String Formatting """


def manual_string_formatting():
    # the end= ' ' indicates to place a space at the end of the line instead of a newline (\n)
    # repr(variable or string).rjust(padding from left, character to ad with)
    for x in range(1, 11):
        print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
        # Note use of 'end' on previous line
        print(repr(x * x * x).rjust(4))

    print('----------------------------------------------')
    # same as above
    for x in range(1, 11):
        print(repr(x).rjust(2), repr(x * x).rjust(3), repr(x * x * x).rjust(4))


"""Old String Formatting"""

"""Template strings"""


# Data types ----------------------------------------------------------------------------------------------------------

def using_data_types():
    # Text Type:	str

    # hint typing th variable (optional)
    variable: str = 'hello world'
    # duck typing (default)- compiler does not type check
    variable1 = 'hello world1'

    # things i can do with a string

    # format using.format() or repr(variable).rjust(padding from left, character to ad with)
    print(variable.rjust(20, '*'))
    # Index string
    variable2 = 'o'
    print(variable.index(variable2))
    print(variable1.index('h'))

    # center string - the value represents the number of characters the string takes up including the leading and
    # trailing spaces
    print(variable1.center(20))

    # capitalise- calitalizes first character
    print(variable1.capitalize())

    # casefold - returns all upper case characters to lower case
    variable4 = 'HELLO IM CAPITALIZED'
    print(variable4.casefold())
    # count- returns the number of occurances of a substring

    print(variable4.count('L'))
    # encodes UTF-8 by default
    print(variable.encode())
    # endswith- returns a boolean
    print(variable.endswith('d'))
    # expand tab- requires the '/t' format specifier in the string to indicate position of tab
    # example changes tab size to 2 blank spaces
    variable5 = 'h\te\tl\tl\to'
    print(variable5.expandtabs(2))
    # find- returns index of the first instance of the substring
    print(variable1.find('l'))

    # print(variable1.join()) - The join() string method returns a string by joining all the elements of an iterable
    # (list, string, tuple), separated by a string separator.
    # 'what to join each item with '.join(iterable)
    list1: list = ['my', 'name', 'is', 'houcine']

    print(' '.join(list1))

    # print(variable1.ljust()) - The string ljust() method returns a left-justified string of a given minimum width.
    print(variable1.ljust(30, '^'))

    # print(variable1.lower()) - he lower() method converts all uppercase characters in a string into
    # lowercase characters and returns it.
    print(variable1.lower())

    # upper(0)- The upper() method converts all lowercase characters in a string into uppercase
    # characters and returns it.
    print(variable1.upper())

    # # print(variable1.maketrans()) -
    # print(variable1.maketrans())

    # print(variable1.format_map())
    # used to includ values of a map type such as dictionary in a string
    point = {'x': 4, 'y': -5}
    print('{x} {y}'.format_map(point))

    # print(variable1.lstrip()) - strips leading spaces
    print('   hello my name is houcine'.lstrip())

    # print(variable1.rstrip()) - strips trailing spaces

    # print(variable1.removeprefix()) - removes leading characters( prefixes) in a string
    print(variable1.removeprefix('hello'))

    # print(variable1.removesuffix()) -removes trailin characters( suffixes) in a string
    print(variable1.removesuffix('1'))

    # print(variable1.partition())- returns a three tuple containing:
    # the substring before the the partitioned word
    # the partitioned word
    # the substring after the partitioned word
    # ('before', partitioned, 'after')
    print(variable1.partition('he'))

    # print(variable1.rpartition()) - same as partition() but takes the last occurance of the argument for the partition
    # the partition is located at the second occurrence of  'is'

    print('hello this is my program. This is a practice run'.rpartition('is'))

    # print(variable1.splitlines())
    print(variable1.splitlines())

    # print(variable1.startswith())
    print(variable1.startswith('h'))

    # print(variable1.title()) - returns a string with the first letter of each work capitalized
    print(variable1.title())

    # print(variable1.swapcase()) - swaps all lower case to upper case and all lower case to upper case
    print(variable1.swapcase())

    # print(variable1.zfill())- returns a string with a specified number of zeros to fill the width of the string
    # this is more useful for numbers
    print(variable1.zfill(20))
    numbers = '1234576'
    print(numbers.zfill(20))

    # logical checks on string variables

    # logical checks on string variables

    #  is alpha numeric- contains only numbers and letter
    print(variable1.isalnum())

    # is alpha numeric- contains only letters of alphabet

    print(variable1.isalpha())
    # logical checks on string variables

    print(variable1.isascii())
    # logical checks on string variables

    print(variable1.isdigit())
    # logical checks on string variables

    print(variable1.islower())
    # logical checks on string variables

    print(variable1.isdecimal())

    # logical checks on string variables

    print(variable1.isidentifier())

    # logical checks on string variables

    print(variable1.isnumeric())

    # logical checks on string variables

    print(variable1.isprintable())

    # logical checks on string variables

    print(variable1.isspace())

    # logical checks on string variables

    print(variable1.istitle())

    # logical checks on string variables

    print(variable1.isupper())

    # logical checks on string variables

    # Numeric Types:	int, float, complex


def using_integers():
    integer1: int = 5000
    integer2: int = 2500
    integer3 = 1234
    """as integer ratio"""
    print((integer1 / integer2).as_integer_ratio())
    """Complex part of complex number"""
    complex1 = 5 - 2j
    print(complex1.imag)
    """real part of complex number"""
    print(complex1.real)
    """converts value to bytes"""
    print(integer1.to_bytes(4, byteorder='big'))
    """bit length of integer"""

    # print(integer3.bit_length())
    # """bit count of number"""

    # print(integer3.bit_count())

    """finds the complex conjugate of a number"""
    print(complex1.conjugate())
    """returns th denominator of a fraction"""
    fraction1 = Fraction(75 / 4)
    print(fraction1.denominator)
    """as integer ratio"""
    bytes1 = integer1.to_bytes(4, byteorder='big')
    print(bytes1)
    print(int.from_bytes(bytes1, 'big'))
    """:returns numerator of fraction needc to import the fraction class"""
    print(fraction1.numerator)
    """as integer ratio"""


# Sequence Types:	list, tuple, range


def using_lists():
    # append()

    list1 = ['orange', 'blue', 'red', 'green']

    list1.append('yellow')
    print(list1)

    # clear()
    list1.clear()
    print(list1)
    # copy()
    list1 = ['orange', 'blue', 'red', 'green']
    list2 = list1.copy()
    print(list1)
    old_list = [1, 2, 3]

    # copy list using =
    new_list = old_list

    # add an element to list
    old_list.append('a')
    print('New List:', new_list)
    print('Old List:', old_list)
    # count() counts the number of occurances of an element in a list
    print('orange occures {} times'.format(list1.count('orange')))
    # extend() : adds one list to the end of another
    list1.extend(list2)
    print(list1)

    # index(): returns the index of an item in a list
    print(list1.index("red"))

    # insert(): insert an item into a list at a specified index. list.index(index,item to insert)
    list1.insert(2, "indigo")
    # pop():  remove an item at a specified index. list.index(index) and returns the item removed
    print(list1)
    print(list1.pop(3))
    print(list1)
    # remove(): removes an item from a list by specifying the item to be removes ( not the index).
    # Only removes the first occurance of the item in the list
    list3 = ['orange', 'blue', 'red', 'green', 'orange', 'orange']
    print(list3)
    list3.remove("orange")
    print(list3)

    # reverse(): reverses the elements of a list
    print(list3)
    list3.reverse()
    print(list3)
    # sort(): sorts a list in specified ascending or descending order ( list.order(reverse=true) or
    # list.order()
    list4 = [1, 2, 4, 7, 5, 2, 9, 5]
    print(list4)
    list4.sort()
    print(list4)
    list4.sort(reverse=True)
    print(list4)

    # Define Nested Lists

    # Mapping Type:	dict

    # Set Types:	set, frozenset

    # Boolean Type:	bool

    # Binary Types:	bytes, bytearray, memoryview

    # Using Lists  -----------------------------------------------------------------------------------------------------
    # Using Tuples -----------------------------------------------------------------------------------------------------

    # looping-----------------------------------------------------------------------------------------------------------

    # Using OS & Sys ---------------------------------------------------------------------------------------------------

    # List Comprehensions-----------------------------------------------------------------------------------------------


def using_list_comprehensions():
    # list comprehension is mainly used for populating a list you wish to store.
    # the structure of a list comprehension is variable =[EXPRESSION for VALUE in COLLECTION if CONDITION]
    # each list element is angle value given by the expression x*x
    list5 = [x * x for x in range(10) if x % 2 == 0]
    print(list5)

    # list comprehensions with multiple 'if' conditions

    list6 = [1, 2, 4, 7, 5, 2, 9, 5]
    list7 = ['orange', 'blue', 'red', 'green', 'orange', 'orange']
    list8 = [x for x in list6 if x % 2 == 0 if x != 0]

    # list comprehensions with multiple loops- creating a list of tuples '() indicate that each list element is a...
    # tuple with two values denoted by x and z.
    # skeleton: list = [(VALUE1, VALUE2)
    #                   for VALUE in COLLECTION1 if CONDITION 1.1 for VALUE2 in COLLECTION2 if CONDITION2.1]
    list9 = [(x, z) for x in list6 if x % 3 != 0 for z in list7 if z != "orange"]
    print(list8)
    print(list9)

    # list comprehensions with multiple loops- creating a multidimensional list or a list of lists...
    # each element of the list another list containing 2 values denoted by x and z
    list10 = [[x, z] for x in list6 if x % 3 != 0 for z in list7 if z != "orange"]
    print(list10)

    # list comprehensions with multiple loops- creating a list of dictionaries '{} indicate that each list element is a
    # ...dictionaries with two values denoted by x and z.

    # list comprehensions with multiple loops- using multiple if statements with AND/OR conditional arguments
    list11 = [[x, z] for x in list6 if x % 3 != 0 and x != 2 for z in list7 if z != "orange" or z != "blue"]
    print(list11)

    # list comprehensions don't need to be assigned they can just be printed
    print([[x, z] for x in list6 if x % 3 != 0 and x != 2 for z in list7 if z != "orange" or z != "blue"])

    #  list comprehensions  for multi-dimensional list
    print([[x, z] for x in list6 for z in list7])

    #  nested list comprehensions
    print('mylist is :', [[y for y in list6] for x in list7])

    # zipping and unzipping------------------------------------------------------------------------------------------


def zipping_and_unzipping():
    # zipping is used to group together items of a list/tuple with corresponding indexes in a tuple
    # the zip() function returns an iterator
    # we use the 'list constructor' to type cast. iterator is changed to a list.
    # refer to iterators section to understand what it is
    list12 = ['apple', 'banana', 'peach', 'grape']
    list13 = [50, 120, 25, 19, 130]
    list14 = list(zip(list12, list13))  # list of tuples
    tuple15 = tuple(zip(list12, list13))  # tuple of tuples
    print(list14)
    print(tuple15)
    print(zip(list12, list13))  # pointer
    zipped = zip(list12, list13)
    for i in zipped:
        print(i)

    # unzipping.- you use the zip() function to unzip a collection of items into two lists. zip(*list/tuple)

    list16, list17 = zip(*list14)

    print(list16)
    print(list17)

    # Slicing ----------------------------------------------------------------------------------------------------------
    # you can slice strings and arrays to obtain parts of a string or array by specifying the start and end index...
    # it will return anything within the start and end index including start/end index items/characters
    # skeleton : collection_name[start_index: end_index]

    string1 = 'hello my name is testing123'
    # includes characters  if index 2 to 15
    string2 = string1[2:15]
    print(string2)
    # includes elements 0 to 3
    print(list14[0:3])
    # includes elements 2 to 4 of a tuple
    print(tuple15[2:4])

    # Dictionaries & Sets-----------------------------------------------------------------------------------------------


def using_dictionaries():
    # dictionaries are used to store values in  the format (key:value pairs). Values are associated with their keys
    # creating a dictionary - created in the form variable ={ key1:value1, key2:value2, key3.value3....}
    # each key in a dictionary must be unique- KEYS CANNOT BE THE SAME

    dict1 = {'book': 'LOTR', 'film': 'THE MATRIX', 'game': 'Deus Ex'}

    print(dict1)

    # creating a dictionary using a loop:
    square_dict = dict()
    for num in range(1, 11):
        square_dict[num] = num * num
    print(square_dict)

    # creating a dictionary using a dictionary comprehension
    # skeleton: dictionary = {key: value for vars in iterable}
    i = "2"
    square_dict = {num: num * num for num in range(1, 11)}
    print(square_dict)

    dict_by_comp = {item: item_name for (item, item_name) in dict1.items()}
    print(dict_by_comp)

    # using dictionary comprehensions with if-else logic
    original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
    new_dict_1 = {k: ('old' if v > 40 else 'young') for (k, v) in original_dict.items()}
    print(new_dict_1)

    # nested dictionaries:  1) in definition 2) combining multiple dictionaries into one 3) using loops

    #  in definition

    family = {'dad': {'name': "Joe", 'year': 1980}, 'mum': {'name': "Jane", 'year': 1982},
              'me': {'name': "bob", 'year': 1992}}
    print(family)

    #  combine multiple dictionaries into one

    dad = {'name': "Joe", 'year': 1980}
    mum = {'name': "Jane", 'year': 1982}
    me = {'name': "bob", 'year': 1992}
    same_family = {"dad": dad, "mum": mum, "me": me}
    print(same_family)

    # using loops

    looped_dict = {}
    for x in range(0, 3):
        looped_dict[x] = {}
        for k in range(0, 3):
            looped_dict[x][k] = x * k

    print(looped_dict)

    # populating nested dictionary without loops

    dict5 = dict()
    dict5['sec_dict'] = {}
    dict5['sec_dict']['third_dict'] = {}
    dict5['sec_dict']['third_dict']['inner_key'] = "value1"
    dict5['sec_dict']['third_dict']['inner_key2'] = "value2"
    dict5['sec_dict']['third_dict']['inner_key3'] = "value3"

    dict6 = {'0': {'w': 'Tensor_w', 'b': 'Tensor_b'}, '1': {'w': 'Tensor_w', 'b': 'Tensor_b'},
             '2': {'w': 'Tensor_w', 'b': 'Tensor_b'}}
    print('ITEMS OF DICT6 : ', dict6.items())

    for x in dict5.values():
        print(x)

    # nested dictionary comprehensions
    nested_dict = {k_out: {k_in: k_in * k_out for k_in in range(0, 3)} for k_out in range(0, 3)}
    print(nested_dict)
    print({x: {k: k * x for k in range(0, 3)} for x in range(0, 3)})
    # nested_dict ={key: {your value is a dictionary comprehension} for var in iterable
    # python evaluates inner comprehension before outer

    # accessing items in a dictionary: thisdict["KEY"]

    book_value = dict1["book"]
    print(book_value)

    # accessing keys in a dictionary: keys()
    print(dict1.keys())

    # adding items: this can be done by 1) dict["key"] = "value"     , 2) dict.update('key':'value')
    dict1["hobby"] = "salsa"
    print(dict1)
    dict1.update({'dish': 'noodles'})
    print(dict1)

    # accessing dictionaries by looping

    # looping through values: values() or dict[x]
    for x in dict1.values():
        print(x)
    for y in dict1:
        print(dict1[y])

    # changing items: referring to key OR use update() function
    # the update function accepts only dictionary types or iterables  with key value pairs (like a list of dictionaries)

    dict1["book"] = 'crime and punishment'
    print(dict1)
    dict2 = dict1.copy()
    dict1.update({'film': 'Inception'})
    print(dict1)
    # removing items: pop(), popitem(),del, clear()
    dict1.pop("game")  # removes item by referring to a key name
    print(dict1)
    dict2.popitem()  # removes last inserted item in dictionary
    print(dict2)
    del dict2["film"]
    print(dict2)
    dict2.clear()  # clears all the items in dictionary but does not remove the dictionary itself
    print(dict2)
    del dict2
    try:
        print(dict2)
    except:
        print("There is an error because dict2 no longer exists")

    # copy dictionaries: use dict2= dict1.copy() makes shallow copy, or assign dict2=dict1 ( any changes to 1 will ...
    # affect the other

    # fromkeys():  creates a new dictionary from the given sequence of elements with a value provided by the user.
    # dictionary.fromkeys(sequence, optional_value)

    keys = ["key1", "key2", "key3", "key4"]
    dict_using_fromkeys = dict.fromkeys(keys)
    print(dict_using_fromkeys)
    dict_using_fromkeys1 = dict.fromkeys(x for x in keys)
    print(dict_using_fromkeys1)
    dict_using_fromkeys2 = dict.fromkeys(keys, "new")
    print(dict_using_fromkeys2)
    dict_using_fromkeys3 = dict.fromkeys((x for x in keys), 'new')
    print(dict_using_fromkeys3)

    # get(): The get() method returns the value for the specified key if the key is in the dictionary.
    print(dict1.get('film'))
    print(dict1.get("class", "key not in dictionary"))

    # items(): The items() method returns a view object that displays a list of dictionary's (key, value) tuple pairs.

    course = {"year1": "thermodynamics", "year2": "fluid Mechanics", "year3": "Chemical Reaction Engineering"}
    print(course.items())
    # setdefault: The setdefault() method returns the value of a key (if the key is in dictionary).
    # If not, it inserts key with a value to the dictionary.
    # dict.setdefault(key, optional_default_value)
    course.setdefault("year4", "Design Project")
    print(course.items())


def using_sets():
    # a set is an unordered, unchangeable collection that does not contain duplicate values.

    set1 = {'value1', 'value2', 'value3'}
    # add()
    print(set1)
    set1.add("value4")
    print(set1)
    # clear()
    set2 = {'hello', 'my', 'name', 'is', 'scint'}
    print(set2)
    set2.clear()
    set2 = {'hello', 'my', 'name', 'is', 'scint'}
    # copy()
    set3 = {}
    print(set3)
    set3 = set2.copy()  # shallow copy: changing 1 set doesnt affect the other
    print(set3)

    # difference(): If A and B are two sets. The set difference of A and B is a set of elements that exists
    # only in set A but not in B. For example:
    # it does this without affecting the original sets
    # REMOVES THE COMMON ELEMENTS AND RETURNS only the elements left over from the set you called difference() on.
    set4 = {'hello', 'my', 'name', 'is', 'scint', 'difference'}
    print(set4)
    print('a ', set4.difference(set2))
    print(set2)
    print('b ', set2.difference(set4))
    print(set2)
    # difference_update()If A and B are two sets. The set difference of A and B is a set of elements that exists
    #     # only in set A but not in B. For example:
    #    DOES AFFECT/ UPDATE THE ORIGINAL SET
    # When you call 'difference() after you have called difference_update() should return none
    print(set4)
    print(set2)
    set4.difference_update(set2)
    print('c ', set2.difference_update(set4))  # returns none because object is mutated
    print(set4)
    print("d ", set4.difference_update(set2))  # returns none because object is mutated

    print(set2)

    # discard(): method takes a single element x and removes it from the set (if present).

    set2.discard("hello")
    print(set2)

    # intersection() : The intersection() method returns a new set with elements that are common to all sets.
    # This does not affect the original sets

    set2.intersection(set4)

    # intersction_uppdate(): The intersection() method returns a new set with elements that are common to all sets.
    #     # this will affect the set you call interection_update() on.
    set4.discard("name")
    print(set2)
    print(set4)
    set2.intersection_update(set4)
    print(set2)

    # isdisjoint()
    # The isdisjoint() method returns True if two sets are disjoint sets. If not, it returns False.
    # Two sets are said to be disjoint sets if they have no common elements.
    # should return false as set2 and set 4 have common elements

    print(set2.isdisjoint(set4))

    # issubset() The issubset() method returns True if all elements of a set are present in another set
    # should return false as set 4 contains 'hello' but does not contain 'main'

    print(set2.issubset(set4))

    # issuperset():

    # issupersetissubset() The issubset() method returns True if all elements
    # of a set are present in another set AND MORE
    print(set2)
    print(set4)
    print('is set2 a super set of set4:', set2.issuperset(set4))

    # pop(): The pop() method removes an arbitrary element from the set and returns the element removed.
    set4.pop()
    print(set4)

    # remove()
    set4.add("me")
    set4.add("is")
    print(set4)
    set4.remove('is')
    print(set4)

    # symetric_difference(): # REMOVES THE COMMON ELEMENTS AND RETURNS...
    #  BOTH the elements left over from the set you called symetric_difference() on and the OTHER SET.
    set2.add("im alive")
    print('x', set2)
    set2.symmetric_difference(set4)
    print('y', set2)

    # symetric_difference_update()# REMOVES THE COMMON ELEMENTS AND RETURNS...
    #     #  BOTH the elements left over from the set you called difference() on and the OTHER SET.
    # Updates the set you called symetric_difference_update() on.
    print('z', set2)
    set2.symmetric_difference_update(set4)
    print('xz', set2)

    # union(): The Python set union() method returns a new set with  the distinct elements from all the sets.
    print(set2)
    print(set4)
    print(set3)
    set5 = set(set2.union(set4, set3))
    print(set5)

    # update(): he Python set update() method updates the set, adding items from other iterables. Will not include ...
    # duplicates
    set6 = {1, 2, 3, 4, 5}
    set5.update(set6)
    print(set5)

    A = {'a', 'b'}
    B = {1, 2, 3}
    A.update(B)
    print(A)
    set5.update(set5)
    print(set5)
    pass


def complex_loops():
    input = np.ones((2, 20, 30), dtype=int)
    print("input: ", input)
    filters = np.zeros((3, 4), dtype=int)
    print("filter: ", filters)
    print("input.shape[1]: ", input.shape[1])
    print("filters.shape[0]: ", filters.shape[0])
    print("input.shape[2]: ", input.shape[2])
    output_rows = input.shape[1] - filters.shape[0] + 1
    print("output rows: ", output_rows)
    output_columns = input.shape[2] - filters.shape[0] + 1
    print("output columns: ", output_columns)
    c = 0
    r = 0
    for f in filters:
        c += 1
    for g in filters[0]:
        r += 1
    print("number of rows in filters", c)
    print("number of columns in filters", r)

    a2 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    print("a2: ", a2[1][2])
    pass

    # Copying Structures (Memory Management) ---------------------------------------------------------------------------

    # Exception Handling -----------------------------------------------------------------------------------------------

    # Generators -------------------------------------------------------------------------------------------------------

    # Iterators --------------------------------------------------------------------------------------------------------

    # abstract base classes---------------------------------------------------------------------------------------------
    # Abstract base classes require everything to extend from a base-level object, and also inherit it's default
    # implementations. This is a nominal (name-based) mechanism.

    # is a class that is stated but not defined. ( has no body)
    # this type of class cannot be instantiated, but other classes can inherit from this class.
    # It is a design choice. You set a sort of template class of methods for a class that you anticipate a class to use
    # any future classes that are related to this abstract base class must have certain methods  you will get a run time
    # error
    # this allows groups of closely related classes to have AT LEAST a standard the methods required of them.


class ScribingUtensils(ABC):
    @abstractmethod
    def scribing(self):
        pass

    @abstractmethod
    def rubbing_out(self):
        pass


class PenBlack(ScribingUtensils):  # PenBlack contains AT LEAST a scribing() and rubbing_out() function.
    def scribing(self):
        print('write in thin black ink')

    def rubbing_out(self):
        print('removes pen ink')

    def pall_point_size(self):  # pall point applies the pen and not all scribing instruments
        print('3mm')

    # commands----------------------------------------------------------------------------------------------------------

    # protocols---------------------------------------------------------------------------------------------------------

    # Protocol (structural-based) subtyping instead only declares what methods something has to have, without requiring
    # it tie itself to either to a concrete parent class and its behaviours.

    # class ProcessEquipment(Protocol):
    #
    #     def process(self) -> None:
    #         ...
    #
    #     def material(self) -> None:
    #         ...
    #
    #     def location(self) -> None:
    #         ...

    # class DistillationColumn:
    #
    #     def __init__(self):
    #         print('initialised Distillation Column')
    #
    #     def process(self) -> None:
    #         print("this is a distillation process")
    #
    #     def material(self) -> None:
    #         material = 'crude oil'
    #         print(f"the material being processed is {material}")
    #
    #
    # class DistillationActions:
    #     def __init__(self):
    #         print('created distillation actions class')
    #
    #     def reduce_flow_rate_in(self, equipment: ProcessEquipment) -> None:
    #
    #         equipment.process()
    #         print('flow rate is now reduced')
    #


def matching():
    to_match = "hello"

    match to_match:
        case "hello":
            return to_match + " world"
        case "something else":
            return "something else"



if __name__ == '__main__':
    printing_strings_f_string()
    printing_strings_format()
    fruit1 = Fruit("apple", "red")
    print(fruit1.describe_fruit())
    print(str(Fruit("strawberry", "red")))


    def car_info(fruits=fruit1):
        print('fruit name: {fruit.name}, fruit colour: {fruit.colour}'.format(fruit=fruits))


    car_info(fruits=fruit1)
    print(using_r_and_s())
    alignment()
    number_signs()
    changing_number_type()
    applying_number_commas()
    expressing_percentages()
    nested_formatting_arguments()
    manual_string_formatting()
    using_data_types()
    using_integers()
    using_lists()
    using_list_comprehensions()
    zipping_and_unzipping()
    using_dictionaries()
    using_sets()

    # Scribing_utensil1 = ScribingUtensils() - this will not work because you can instantiate an abstract class
    black_pen = PenBlack()
    black_pen.pall_point_size()
    complex_loops()
    print(matching())


