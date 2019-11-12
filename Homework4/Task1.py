import datetime


def functions_results(func):
    """Stores the results of function calls and the time it takes to get

    the result during program start
    """
    if 'func_results' not in globals():
        global func_results
        func_results = {}

    def wrapper(*args, **kwargs):
        before_call = datetime.datetime.now()
        res = func(*args, **kwargs)
        after_call = datetime.datetime.now()
        res_time = after_call - before_call
        func_results[func.__name__] = func_results.get(func.__name__, []) + [(res, str(res_time))]
        return func_results
    return wrapper


@functions_results
def test1():
    return 'Some text'


@functions_results
def test2(count_me_string):
    chars_counter = {}
    for i in count_me_string:
        chars_counter[i] = chars_counter.get(i, 0) + 1
    return chars_counter


test1()
test2('abc')
test2('mytest')
print(func_results)
