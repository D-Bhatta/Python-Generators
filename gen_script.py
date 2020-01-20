import logging
import logging.config
from json import load as jload
import csv

""" Configure logger lg with config for appLogger from config.json["logging"] """
with open('config.json', 'r') as f:
        config = jload(f)
        logging.config.dictConfig(config["logging"])
lg = logging.getLogger('appLogger')
# lg.debug("This is a debug message")

def using_generators():
    def reading_large_files():
        """ Introduced with PEP 255, generator functions are a special kind of function that return a lazy iterator. These are objects that you can loop over like a list. However, unlike lists, lazy iterators do not store their contents in memory.  """
        def reading_large_files1():
            """ A common use case of generators is to work with data streams or large files, like CSV files. These text files separate data into columns by using commas. This format is a common way to share data. Now, what if you want to count the number of rows in a CSV file?  """
            with open("techcrunch.csv", "r") as f:
                csv_gen = csv.reader(f)
                row_count = 0
                for row in csv_gen:# pylint: disable=unused-variable
                    row_count += 1
                row_count_string = f"Row count is {row_count} in reading_large_files1"
                lg.info(row_count_string)
                #print(row_count_string)
        reading_large_files1()
        def reading_large_files2():
            """ What’s happening here? Well, you’ve essentially turned csv_reader() into a generator function. This version opens a file, loops through each line, and yields each row, instead of returning it. """
            def csv_reader(filename):
                with open(filename, "r") as f:
                    for row in f:
                        yield row
            csv_gen = csv_reader("techcrunch.csv")
            row_count = 0
            for row in csv_gen:# pylint: disable=unused-variable
                row_count += 1
            row_count_string = f"Row count is {row_count} in reading_large_files2"
            lg.info(row_count_string)
        reading_large_files2()
        def reading_large_files3():
            """ You can also define a generator expression (also called a generator comprehension), which has a very similar syntax to list comprehensions. In this way, you can use the generator without calling a function: """
            csv_gen = (row for row in open("techcrunch.csv", "r"))
            row_count = 0
            for row in csv_gen:# pylint: disable=unused-variable
                row_count += 1
            row_count_string = f"Row count is {row_count} in reading_large_files3"
            lg.info(row_count_string)
        reading_large_files3()
    reading_large_files()
    def generating_an_infinite_sequence():
        def infinite_sequence():
            num = 0
            while True:
                yield num
                num += 1
        nums = "Infinite sequence nums = "
        for i in infinite_sequence():
            nums += str(i) + "  "
            if i == 999: break
        lg.info(nums)
    generating_an_infinite_sequence()

using_generators()  