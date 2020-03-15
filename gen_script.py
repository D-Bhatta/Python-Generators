import csv
import logging
import logging.config
from json import load as jload

""" Configure logger lg with config for appLogger from config.json["logging"] """
with open('config.json', 'r') as f:
        config = jload(f)
        logging.config.dictConfig(config["logging"])
lg = logging.getLogger('appLogger')
# lg.debug("This is a debug message")

class Generators(object):
    def using_generators(self):
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
                    return row_count
            
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
                return row_count
            
            def reading_large_files3():
                """ You can also define a generator expression (also called a generator comprehension), which has a very similar syntax to list comprehensions. In this way, you can use the generator without calling a function: """
                csv_gen = (row for row in open("techcrunch.csv", "r"))
                row_count = 0
                for row in csv_gen:# pylint: disable=unused-variable
                    row_count += 1
                row_count_string = f"Row count is {row_count} in reading_large_files3"
                lg.info(row_count_string)
                return row_count
            
            return reading_large_files1(),reading_large_files2(),reading_large_files3()

        def generating_an_infinite_sequence():
            """ First, you initialize the variable num and start an infinite loop. Then, you immediately yield num so that you can capture the initial state. This mimics the action of range().After yield, you increment num by 1. If you try this with a for loop, then you’ll see that it really does seem infinite """
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
            return nums

        def generating_an_infinite_sequence2():
            """ Here, you have a generator called gen, which you manually iterate over by repeatedly calling next(). This works as a great sanity check to make sure your generators are producing the output you expect. """
            def infinite_sequence():
                num = 0
                while True:
                    yield num
                    num+=1
            nums = "Second infinite sequence = "
            gen = infinite_sequence()
            while True:
                i = next(gen)
                nums += str(i) + "  "
                if i == 999: break
            lg.info(nums)
            return nums

        def detecting_palindromes():
            def infinite_sequence():
                num = 0
                while True:
                    yield num
                    num+=1
            def is_palindrome(num):
                # skip single digit inputs
                if num // 10 == 0:
                    return False
                temp = num
                reversed_num = 0
                # reverse the input num
                while temp!=0:
                    reversed_num = (reversed_num*10) + (temp % 10)
                    temp = temp // 10
                # check if reversed num and num are the same number
                if num == reversed_num:
                    return True
                else:
                    return False
            pal_nums = "Palindrome number sequence: "
            for i in infinite_sequence():
                if i == 102202:
                    break
                pal = is_palindrome(i)
                if pal:
                    pal_nums += str(i) + "  "
            lg.info(pal_nums)
            return pal_nums
        return [reading_large_files(),generating_an_infinite_sequence(),generating_an_infinite_sequence2(),detecting_palindromes()]
    def understanding_generators(self):
        def building_generators_with_generator_expressions():
            nums_squared_lc = [i**2 for i in range(5)]
            nums_squared_gc = (i**2 for i in range(5))
            lg.info('type of nums_squared_lc:{}'.format(type(nums_squared_lc)))
            lg.info('type of nums_squared_gc:{}'.format(type(nums_squared_gc)))
            return [str(type(nums_squared_lc)), str(type(nums_squared_gc))]
        types = building_generators_with_generator_expressions()
        def profiling_generator_performance():
            from sys import getsizeof
            nums_squared_lc = [i**2 for i in range(10000)]
            nums_squared_gc = (i**2 for i in range(10000))
            # Add string info 
            lg.info('size of lc:{}'.format(getsizeof(nums_squared_lc)))
            lg.info('size of gc:{}'.format(getsizeof(nums_squared_gc)))
            from cProfile import run
            run('sum([i**2 for i in range(10000)])','lc.profile')
            import pstats
            p = pstats.Stats('lc.profile')
            # print number of calls
            lg.info(('Number of function calls for lc:'+' {}'.format(p.prim_calls)))
            run('sum((i**2 for i in range(10000)))','gc.profile')
            q = pstats.Stats('gc.profile')
            lg.info(('Number of function calls for gc:'+' {}'.format(q.prim_calls)))
            return [getsizeof(nums_squared_lc),getsizeof(nums_squared_gc),p.prim_calls,q.prim_calls]
        stats = profiling_generator_performance()
        return [types, stats]
    def understanding_yeild_statement(self):
        """ On the whole, yield is a fairly simple statement. Its primary job is to control the flow of a generator function in a way that’s similar to return statements. As briefly mentioned above, though, the Python yield statement has a few tricks up its sleeve.When you call a generator function or use a generator expression, you return a special iterator called a generator. You can assign this generator to a variable in order to use it. When you call special methods on the generator, such as next(), the code within the function is executed up to yield.When the Python yield statement is hit, the program suspends function execution and returns the yielded value to the caller. (In contrast, return stops function execution completely.) When a function is suspended, the state of that function is saved. This includes any variable bindings local to the generator, the instruction pointer, the internal stack, and any exception handling.This allows you to resume function execution whenever you call one of the generator’s methods. In this way, all function evaluation picks back up right after yield. """
        def multi_yield():
            yield_str = "This is the first string"
            yield yield_str
            yield_str = "This is the second string"
            yield yield_str
        multi_obj = multi_yield()
        strings = []
        for i in range(10): # pylint: disable=unused-variable
            try:
                strings.append(next(multi_obj))
            except StopIteration:
                lg.error("Stop Iteration error: generator exhausted")
                break
        lg.info(strings)
        return strings
    def adv_generator_methods(self):
        """ Using send(), throw(), and close() """
        pals = []
        pals2 = []
        pals3 = []
        def is_palindrome(num):
            if num // 10 == 0:
                return False
            temp = num
            rev = 0
            while temp!=0:
                rev = (rev *10) + (temp % 10)
                temp = temp // 10
            if rev == num:
                return True
            else:
                return False
        def infinite_palindromes():
            num = 0
            while True:
                if is_palindrome(num):
                    i = (yield num)
                    if i is not None:
                        num = i
                num = num + 1
        def use_send():
            pal_gen = infinite_palindromes()
            for i in pal_gen:
                pals.append(i)
                if i == 10000100001:
                    break
                digits = len(str(i))
                pal_gen.send(10**(digits))
        def use_throw():
            pal_gen = infinite_palindromes()
            for i in pal_gen:
                pals2.append(i)
                digits = len(str(i))
                if digits == 5:
                    pal_gen.throw(ValueError("we don't like this large palindrome"))
                pal_gen.send(10**(digits))
        def use_close():
            pal_gen = infinite_palindromes()
            for i in pal_gen:
                pals3.append(i)
                digits = len(str(i))
                if digits == 5:
                    pal_gen.close()
                pal_gen.send(10**(digits))
        use_send()
        lg.info(pals)
        try:
            use_throw()
        except ValueError:
            lg.error("ValueError exception thrown by generator")
        lg.info(pals2)
        try:
            use_close()
        except StopIteration:
            lg.error("StopIteration exception thrown by generator")
        lg.info(pals3)
        return pals, pals2, pals3
    def data_pipelines(self):
        filename = "techcrunch.csv"
        # read every line in file
        lines = (line for line in open(filename))
        # split each line into a list of values
        list_line = (s.rstrip().split(",") for s in lines )
        # extract the column names
        cols = next(list_line)
        # create a dict of values from lists
        company_dicts = (dict(zip(cols,data)) for data in list_line)
        # Filter out irrelevant data
        funding = (
            int(company_dict["raisedAmt"])
            for company_dict in company_dicts
            if company_dict["round"]  == "a"
        )
        # calculate total and avg        
        total_amt_raised = sum(funding)
        result_sum = f"Total series A fundraising : ${total_amt_raised}"
        lg.info(result_sum)
        # avg raised per company
        """ Find out number of companies  
        \nDivide total_amt_raised by number of companies"""
        def dict_gen():
            # read every line in file
            lines = (line for line in open(filename))
            # split each line into a list of values
            list_line = (s.rstrip().split(",") for s in lines )
            # extract the column names
            cols = next(list_line)
            # create a dict of values from lists
            company_dicts = (dict(zip(cols,data)) for data in list_line)
            return company_dicts
        company_dicts = dict_gen()

        num_comps = len(set((
            str(company_dict["company"])
            for company_dict in company_dicts
            if company_dict["round"]  == "a"
        )))
        avg = total_amt_raised//num_comps
        result_avg = f"Average amount raised by company = {avg}"
        lg.info("Number of companies:"+str(num_comps))
        lg.info(result_avg)
        return total_amt_raised, num_comps, avg



gen = Generators()
gen.using_generators()
gen.understanding_generators()
gen.understanding_yeild_statement()
gen.adv_generator_methods()
gen.data_pipelines()
