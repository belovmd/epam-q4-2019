from time import time


def functions_results(func):
    """Stores the results of function calls and the time it takes to get

    the result during program start
    """
    if 'results' not in globals():
        global results
        results = {}

    def wrapper(*args, **kwargs):
        before_call = time()
        res = func(*args, **kwargs)
        after_call = time()
        time_passed = after_call - before_call
        name = func.__name__
        result_time = results.get(name, [])
        result_time.append((res, str(time_passed)))
        results[name] = result_time
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
