from pytasks import count_characters
from pytasks import is_palindrome
from pytasks import fizzbuzz
from pytasks import generate_numbers

tasks_dict = {
    'is_palindrome': is_palindrome,
    'generate_numbers': generate_numbers,
    'fizzbuzz': fizzbuzz,
    'count_characters': count_characters,
}


def runner(*run_list):
    if not run_list:
        is_palindrome()
        generate_numbers()
        fizzbuzz()
        count_characters()
    else:
        for func in set(run_list).intersection(tasks_dict.keys()):
            tasks_dict[func]()


if __name__ == '__main__':
    runner()
