import datetime


def functions_results(func):
    """Stores the results of function calls and the time it takes to get

    the result during program start
    """
    if 'results' not in globals():
        global results
        results = {}

    def wrapper(*args, **kwargs):
        before_call = datetime.datetime.now()
        res = func(*args, **kwargs)
        after_call = datetime.datetime.now()
        time = after_call - before_call
        name = func.__name__
        results[name] = results.get(name, []) + [(res, str(time))]
        return results
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
print(results)
