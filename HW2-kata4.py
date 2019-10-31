""" 4 kyu - Text align justify
https://www.codewars.com/kata/537e18b6147aa838f600001b

Your task in this Kata is to emulate text justification in monospace font.
You will be given a single-lined text and the expected justification width.
The longest word will never be greater than this width.

Here are the rules:

- Use spaces to fill in the gaps between words.
- Each line should contain as many words as possible.
- Use '\n' to separate lines.
- Gap between words can't differ by more than one space.
- Lines should end with a word not a space.
- '\n' is not included in the length of a line.
- Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,'
 (2, 2, 2, 1 spaces)).
- Last line should not be justified, use only one space between words.
- Last line should not contain '\n'
- Strings with one word do not need gaps ('somelongword\n').

Example with width=30:

Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet tellus.
"""


def justify(text, width):
    curr_pos_in_text = 0
    new_text = ''
    while curr_pos_in_text < len(text):
        if text[curr_pos_in_text] == ' ':
            curr_pos_in_text += 1
            continue
        if len(text) - curr_pos_in_text <= width:
            new_text = new_text + text[curr_pos_in_text:]
            break

        if curr_pos_in_text == 0:
            empty_space_in_row = text[curr_pos_in_text + width:: -1].find(' ')
        else:
            empty_space_in_row = text[curr_pos_in_text + width:
                                      curr_pos_in_text - 1: -1].find(' ')

        my_row = text[curr_pos_in_text:
                      curr_pos_in_text + width - empty_space_in_row]
        new_row = ''
        if empty_space_in_row <= 0:
            new_row = my_row
        else:
            spaces_in_my_row = my_row.count(' ')
            if spaces_in_my_row == 0:
                spaces_between_words = 0
                one_more_space = 0
            else:
                spaces_between_words = ((empty_space_in_row //
                                        spaces_in_my_row) + 1)
                one_more_space = empty_space_in_row % spaces_in_my_row

            my_row = my_row.split(' ')
            for word_number in range(len(my_row) - 1):
                if word_number < one_more_space:
                    new_row = (new_row + my_row[word_number] +
                               ' ' * (spaces_between_words + 1))
                else:
                    new_row = (new_row + my_row[word_number] +
                               (' ' * spaces_between_words))
            if len(my_row) > 1:
                new_row = new_row + my_row[-1]
            elif len(my_row) == 1:
                new_row = my_row[0]
        new_text = new_text + new_row + '\n'
        curr_pos_in_text = curr_pos_in_text + width - empty_space_in_row
    return new_text


print(justify('My name is Anton Stychnevsky. I am from Vitebsk, and now I '
              'live in Minsk and study Python. By the way, '
              'London is the capital of Great Britain', 17))  # for example
