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
    answer = ''
    while len(text) > width:
        line = text[:width]
        if (text[width] == ' ') or (line.find(' ') == -1):
            answer += line + '\n'
            text = text[width + (1 if text[width] == ' ' else 0):]
        else:
            line = line[:line.rfind(' ')]
            text = text[len(line) + 1:]
            words = line.split(' ')
            if len(words) > 1:
                spaces_to_some_w = (width-len(line)) % (len(words) - 1)
                spaces_to_all_w = (width - len(line)) // (len(words) - 1)
                for word_n in range(spaces_to_some_w):
                    words[word_n] += ' '
                answer += (' ' * (1 + spaces_to_all_w)).join(words) + '\n'
            else:
                answer += line + '\n'
    return answer + text


print(justify('My name is Anton Stychnevsky. I am from Vitebsk, and now I '
              'live in Minsk and study Python. By the way, '
              'London is the capital of Great Britain', 17))  # for example
