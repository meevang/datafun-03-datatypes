"""
Mee Vang Task 5
Modify this docstring.

"""

# import from local util_datafun_logger.py
from util_datafun_logger import setup_logger

# Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)


def illustrate_tuples():
    """This function illustrates tuples in Python."""

    """
    TUPLES .......................................................

    In Python, a tuple is a immutable sequence type. 
    This means that once you create a tuple, 
    you cannot change the values it contains: 
    you can't add, remove, or change the values of any of the elements 
        in the tuple.
    Tuples are created using parentheses.

    You can access the elements of a tuple using indexing, like a list.
    The first index is 0 and the last index is -1.

    Since a tuple (like a list) is ordered, you can use slicing to get a
    range of elements from the tuple. [start:end:step]

    Tuples support concatenation, repetition, and membership testing.

    Tuples enable a function to return multiple values, for example:
    (slope, intercept) = statistics.linear_regression(xlist, ylist)
    (host, port) = get_host_and_port()

    Tuples are often used as keys in dictionaries.
    """

    # Create some tuples
    tuple_brand = ("Pepsi", "Coca-Cola", "7up", "Fanta", "Dr. Pepper")
    tuple_flavor = ("Cola", "Cherry", "Orange", "Lemon-lime")

    logger.info(f"tuple_brand = {tuple_brand}")
    logger.info(f"tuple_flavor = {tuple_flavor}")

    # tuple concatenation
    tupleCat = tuple_brand + tuple_flavor

    # tuple repetition
    tupleAThrice = tuple_brand * 2

    # TODO: Start using this f-string "syntactic sugar" for quick ouptut
    # just add space = space inside the curly braces
    # it will print the name of the variable and the value
    logger.info(f"{tuple_brand = }")
    logger.info(f"{tuple_flavor = }")
    logger.info(f"{tupleCat = }")
    logger.info(f"{tupleAThrice = }")

#Sets: create two sets. Get the intersection and the union.
def illustrate_sets():
    """This function illustrates sets in Python."""

    """
    SETS .......................................................    

    A set is an unordered collection of unique elements.
    A set is created using curly braces.
    Sets can use the same methods as lists and tuples.
    Sets support the following operations:

    Membership testing (using the in and not in operators)
    Element addition (using the add method)
    Element removal (using the remove and discard methods)
    Set union (using the union method or the | operator)
    Set intersection (using the intersection method or the & operator)
    Set difference (using the difference method or the - operator)
    Set symmetric difference (using the symmetric_difference method or ^ operator)


    """

    set_brandA = {1, 2, 3, 4, 5}
    set_brandB = {4, 5, 6, 7, 8}

    logger.info(f"set_brandA = {set_brandA}")
    logger.info(f"set_brandB = {set_brandB}")

    # set union
    set_unionC = set_brandA | set_brandB
    logger.info(f"Set Union = {set_unionC}")

    # set intersection
    set_interD = set_brandA & set_brandB
    logger.info(f"Intersection = {set_interD}")

    # set difference
    set_diffE = set_brandA - set_brandB
    logger.info(f"Difference = {set_diffE}")

#Use a dictionary to create key-value pairs of each word and its count from a file. 
def illustrate_dictionaries():
    """This function illustrates dictionaries in Python."""

    """
    DICTIONARIES .......................................................    

    A dictionary is an unordered collection of key-value pairs.
    A dictionary is created using curly braces.
    A dictionary is accessed using keys, not indexes.
    A dictionary is mutable, so you can add, remove, and change values.
    A dictionary is iterable, so you can use it in a for loop.
    A dictionary is not ordered, so you can't slice to access a range of values.

    Dictionaries support the following operations:

    Indexing: access the value associated with a key in the dictionary. 
    For example: dogA['name'].

    Membership testing: use 'in' and 'not in' operators 
    to test whether a key is in the dictionary. 
    For example: 'name' in dogA.

    Adding and updating items: use indexing to add a new key-value pair,
    or to update the value associated with an existing key. 
    For example: dogA['age'] = 2.

    Removing items: Use the del statement to remove a key-value pair. 
    For example: del dogA['weight_kg'].

    Iteration: You can use a for loop to iterate over the 
    keys, values, or key-value pairs in a dictionary. 
    For example: for key in dogA: print(key)

    Dictionaries are a lot like 
    JSON objects - a common data format used in web development.

    """

    sodaA_dict = {"Calories": 0, "Sugar": 0, "Type": "Zero"}
    sodaB_dict = {"Calories": 150, "Sugar": 34, "Type": "Regular"}

    logger.info(f"sodaA_dict = {sodaA_dict}")
    logger.info(f"sodaB_dict = {sodaB_dict}")

    with open("text_simple.txt") as file_object:
        word_list = file_object.read().split()

    word_counts_dict = {}
    for word in word_list:
        if word in word_counts_dict:
            word_counts_dict[word] += 1
        else:
            word_counts_dict[word] = 1

    logger.info("Word count is a good way to begin processing text.")
    logger.info(f"Given text_simple.txt, the word_counts_dict = {word_counts_dict}")

    # IMPORTANT: Dictionary comprehesions - the preferred approach

    # Create a dictionary of word counts from a list of words
    # A dictionary is always key:value pairs
    # Say "I want word:count for each word in word_list"
    # Cast the result to a dictionary by using curly braces {}
    word_counts_dict2 = {word: word_list.count(word) for word in word_list}

    # Spend most of your practice on comprehensions - they are
    # key to transforming data in Python.

    logger.info("Given text_simple.txt and comprehensions,")
    logger.info(f"the the word_counts_dict2 = {word_counts_dict2}")


def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!
# Remember, code blocks must be indented consistently after a colon.

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    # call your functions here
    illustrate_tuples()
    illustrate_sets()
    illustrate_dictionaries()

    logger.info("Add more logging statements to the code to see what happens.")
    logger.info("Explore enough to understand.")
    logger.info("Apply these skills to your own topic domain.")
    show_log()
