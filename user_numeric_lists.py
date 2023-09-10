""" Mee Vang Project 3"""

# import from standard library
import statistics
import math

# TODO: import from local util_datafun_logger.py 
# import from local files
from util_datafun_logger import setup_logger

# TODO: Call the setup_logger function to create a logger and get the log file name
# Call the setup_logger function
logger, logname = setup_logger(__file__)


# TODO: Create some shared data lists if you like - or just create them in your functions
list1= [5, 6, 11, 15, 19, 22, 25, 33, 45, 49, 50, 54, 57, 58, 62, 66, 73, 77, 80, 85]

listx = list(range(10))
listy = [1, 2, 3, 4, 5, 6, 8, 10, 12, 20]

# TODO: define some custom functions
def illustrate_list_statistics():
    """This function illustrates descriptive statistics for a numric list."""

    logger.info(f"score_list: {list1}")

# calculate the mean, median, and mode
    mean = statistics.mean(list1)
    median = statistics.median(list1)
    mode = statistics.mode(list1)

    logger.info(f"mean: {mean}")
    logger.info(f"median: {median}")
    logger.info(f"mode: {mode}")

# calculate std dev and variance 
    stdev = statistics.stdev(list1)
    variance = statistics.variance(list1)

    logger.info(f"stdev: {stdev:.2f}")
    logger.info(f"variance: {variance:.2f}")


def illustrate_list_correlation_and_prediction():
    """This function illustrates correlation and prediction for a numric list."""

    logger.info(f"listx: {listx}")
    logger.info(f"listy: {listy}")

    # Descriptive: Measures of correlation
    # Use two numerical lists of the same size
    # Use statisttics module to get correlation between listx and listy

    correlationxy = statistics.correlation(listx, listy)
    logger.info(f"correlation between x and y: {correlationxy}")

    slope, intercept = statistics.linear_regression(listx, listy)
    logger.info(f"The equation of the best fit line is: y = {slope}x + {intercept}")

    x_max = max(listx)
    newx = 15 # predict for a future x value

    # Use the slope and intercept to predict a y value for the future x value
    # y = mx + b

    newy = slope * newx + intercept

    logger.info("We predict that when x = {newx}, y will be about {newy}")


def illustrate_list_built_in_functions():
    # BUILT-IN FUNCTIONS ......................................
    # Many built-in functions work on lists
    # try min(), max(), len(), sum(), sorted(), reversed()

    # Using the score list provided above, do the following:
    # Calcuate the max and min scores
    max_value = max(list1)
    min_value = min(list1)

    logger.info(f"Given score list: {list1}")
    logger.info(f"The max() is {max_value}")
    logger.info(f"The min() is {min_value}")

    # Calculate the length of the list
    len_list = len(list1)
    logger.info(f"The len() is {len_list}")

    # Calculate the sum of the list
    sum_list = sum(list1)
    logger.info(f"The sum() is {sum_list}")

    # Calculate the average of the list
    avg_list = sum_list / len_list
    logger.info(f"The average is {avg_list}")

    logger.info(f"Given score list: {list1}")
    # Return a new list soreted in ascending order
    asc_scores = sorted(list1)
    logger.info(f"Using the built-it function sorted(lst) gives: {asc_scores}")

    # Return a new list soreted in descending order
    desc_scores = sorted(list1, reverse=True)
    logger.info(
        f"Using the built-in function sorted(lst,reverse=True) gives: {desc_scores}"
    )


def illustrate_list_methods():
    """This function illustrates methods that can be called on a list"""

    """

     LIST METHODS ............................................... 

     Here are some common methods that operate on an instance of a list.

     append(x): Add an item to the end of the list.
     extend(iterable): Add all the items from an iterable (such as another list)
          to the end of the list.
     insert(i, x): Insert an item at a given position.
     remove(x): Remove the first occurrence of an item.
     pop([i]): Remove the item at the given position in the list, 
     and return it. If no index is specified, 
     removes and returns the last item in the list.
     clear(): Remove all items from the list.
     index(x[, start[, end]]): Return the index of the first occurrence of
          an item.
     count(x): Return the number of occurrences of an item.
     sort(key=None, reverse=False): Sort the items in the list 
          in ascending order.
     reverse(): Reverse the order of the items in the list.
     copy(): Return a shallow copy of the list.

     """

    #4.1 append() a single value to the list
    lst = [1, 2, 4, 5, 6]
    lst.append(3)

    #4.2 extend the list with another list
    lst.extend([7, 8, 9])

    #4.3 insert() at an index, insert a value
    i = 0
    newvalue = 15
    lst.insert(i, newvalue)

    #4.4 remove(5) remove the number 5 from the list, if found (change 5 to a value in your list)
    item_to_remove = 5
    lst.remove(item_to_remove)

    #4.5 Count how many times 111 appears in the list
    count_of_2 = lst.count(111)

    #4.6 Sort the list in ascending order using the sort() method
    asc_lst2 = lst.sort()

    #4.7 Sort the list in descending order using the sort() method
    desc_lst2 = lst.sort(reverse=True)

    #4.8 Copy the list to a new list
    new_lst = lst.copy()
    logger.info(f"new_scores is: {new_lst}")

    #4.9 pop() the first item off the top of the list/stack
    # Remove the first item from the new list
    # The first item in a list is at index 0
    # Think of it as an offset from the beginning of the list
    first = new_lst.pop(0)
    logger.info(
        f"Popped the first (index=0): {first} and now, new_scores is: {new_lst}"
    )

    #4.10 pop() the last time off the bottom of the list/stack
    # Remove the last item from the new list
    # The last item from new index -1
    last = new_lst.pop(-1)
    logger.info(
        f"Popped the last (index=0): {last} and now, new_scores is: {new_lst}"
    )

def illustrate_list_transformations():
    """This function illustrates transformations that can be applied to a list"""

    logger.info("Number list: {list1}")

    # LIST TRANFORMATIONS ............................
    # Use the built in filter() function to keep x such that x is less than 4 (or some other cutoff), or keep the even ones, whatever.
    # FILTER and MAP are critical tranformations in big data applications

    # Use the built-in function filter() anywhere you need to filter a list
    # Filter the new list to only include x value less than 4
    # Say "KEEP x such that x < 4 is True" 
    # Cast the result using square brackets to get back a list
    xless_than = list(filter(lambda x: x < 4, list1))
    logger.info(f"X values less than 4: {xless_than}")

    # Use the built in map() function to map each x to cuberoot of x
    xcubed = [map(lambda x: x ** (1/3), list1)]
    logger.info(f"Doubled scores: {xcubed}")

    #Use the built in map() function to calculate the volume of a cube with a side equal to the value in your list. Hint: Volume = side * side * side
    # map() function to calculate the volume of a cube w/ a side equal to the value of your list
    side = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    volume = [map(lambda x: side * side* side, side)]
    logger.info(f"Volume: {volume}")


def illustrate_list_comprehensions():
    """This function illustrates list comprehensions"""

    logger.info("List 1: {list1}")

    #Use a list comprehension to filter (start within square brackets) to get x (for each x in list1) if x is less than 4 or some other cutoff. 
    xless_than = [x for x in list1 if x < 4]
    logger.info("x values over 4 (using list comprehensions!): {xless_than}")

    #list comp to triple value in list1
    tripled_x = [x*3 for x in list1]
    logger.info("Tripled x values: {tripled_x}")

    #list comp to transform numeric list into another numeric list
    sqr_x = map(lambda x: x ** 2, list1)
    logger.info(f"Square x values: {sqr_x}")


def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
if __name__ == "__main__":
    logger.info("Calling functions from main block")

    # call your functions here (see instructions)
    illustrate_list_statistics()
    illustrate_list_correlation_and_prediction()
    illustrate_list_built_in_functions()
    illustrate_list_methods()
    illustrate_list_transformations()
    illustrate_list_comprehensions()

    logger.info("Add more logging statements to the code to see what happens.")
    logger.info("Explore enough to understand.")
    logger.info("Apply these skills to your own topic domain.")

    show_log()