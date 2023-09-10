"""
Mee Vang Task 4

Modify this docstring.

"""

# imports first
import random

from util_datafun_logger import setup_logger

# Set up logging .............................................

logger, logname = setup_logger(__file__)

# reusable functions next
#Create about five lists. I'll use listA, listB, etc, but yours should make sense for your domain. 
brand_of_soda = ["Pepsi", "Coca-cola", "7up", "Fanta", "Mountain Dew", "Dr. Pepper"]

type_of_soda = ["Regular", "Diet", "Zero"]

flavor = ["Cola", "Lemon-lime", "Cherry", "Orange"]

calories = [0, "Over 100", "Over 200", "Over 300"]

grams_of_sugar = [0, 100, 150, 200, 250]

# call functions and execute code
# Use the built-in functions: len(), set(), and zip() to combine 2 or more lists into tuples.
def use_combine_lists_len():
    len_list = len(type_of_soda)
    logger.info(f"Length: {len_list}")

def use_combine_lists_set():
    set_list = tuple(set(flavor))
    logger.info(f"Set List: {set_list}")

def use_combined_lists_zip():
    zip_list = tuple(zip(calories, grams_of_sugar))
    logger.info(f"Zip list: {zip_list}")

# Use random.choice() to pick a random value from one of your lists.
def random_choice():
    random_list = random.choice(type_of_soda)
    logger.info(f"Random type of soda : {random_list}")

#Customize the sentence generator to create random sentences about your domain. 
def random_sent():
    logger.info("Calling random_sent()")
    random_soda = (f"{random_soda} taste the same as {random_soda}")
    logger.info(f"Random sentence: {random_soda}")


def process_text_hamlet():
    """Read in text_hamlet.txt and process it"""
    logger.info("Calling process_text_hamlet()")

    # read in woodchuck to get a list of words
    with open("text_hamlet.txt", "r") as fileObject:
        text = fileObject.read()
        list_words = text.split()  # split on whitespace
        unique_words = set(list_words)  # remove duplicates by making a set

        # Get the count and list of words
        word_ct = len(list_words)

        logger.info(f"The list of words is: {list_words}")
        logger.info(f"There are {word_ct} words in the file.")

        # Print the count and list of unique words
        unique_word_ct = len(unique_words)

        logger.info(f"The set of unique words is: {unique_words}")
        logger.info(f"There are {unique_word_ct} unique words in the file.")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())

# use if __name__ == "__main__":
if __name__ == "__main__":
    logger.info("Calling functions from main block")

    process_text_hamlet()
    use_combine_lists_len()
    use_combine_lists_set
    use_combined_lists_zip()
    random_choice()
    random_sent
    show_log()
