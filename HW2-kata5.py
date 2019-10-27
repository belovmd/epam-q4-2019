""" 4 kyu - Simplifying multilinear polynomials https://www.codewars.com/kata/55f89832ac9a66518f000118

When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually
bigger), and that was easy-peasy ("2x+xy"). But tell that to your pc and we'll see!

Write a function: simplify, that takes a string in input, representing a multilinear non-constant polynomial in
integers coefficients (like "3x-zx+2xy-x"), and returns another string as output where the same expression has been
simplified in the following way ( -> means application of simplify):

All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:
"cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"

All monomials appears in order of increasing number of variables, e.g.:
"-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"

If two monomials have the same number of variables, they appears in lexicographic order, e.g.:
"a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"

There is no leading + sign if the first coefficient is positive, e.g.:
"-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"

N.B. to keep it simplest, the string in input is restricted to represent only multilinear non-constant polynomials,
so you won't find something like `-3+yx^2'. Multilinear means in this context: of degree 1 on each variable.

Warning: the string in input can contain arbitrary variables represented by lowercase characters in the english
alphabet.
"""


def simplify(poly):
    dict_of_vars = {}
    i = 0
    while i < len(poly):
        if poly[i] == '-':
            sign = -1
            i += 1
        elif poly[i] == '+':
            sign = 1
            i += 1
        elif i == 0:
            sign = 1
        coeff = ''
        var = ''
        while True:
            if i == len(poly):
                pass
            elif poly[i].isdigit():
                coeff += poly[i]
                i += 1
                continue
            elif poly[i].isalpha():
                if coeff == '':
                    coeff = 1
                var += poly[i]
                i += 1
                continue
            coeff = sign * int(coeff)
            sorted_var = sorted(var)
            var = ''
            for letter in sorted_var:
                var += letter
            if var in dict_of_vars.keys():
                dict_of_vars[var] += coeff
            else:
                dict_of_vars[var] = coeff
            break

    answer = ''
    for term2 in sorted(dict_of_vars.keys(), key=lambda x: (len(x), x)):
        if dict_of_vars[term2] != 0:
            if dict_of_vars[term2] > 0:
                if answer != '':
                    answer += '+'
            else:
                answer += '-'

            if abs(dict_of_vars[term2]) == 1:
                answer += term2
            else:
                answer += str(abs(dict_of_vars[term2])) + term2
    return answer


print(simplify('dc-dcba-2z+3av+z+z'))  # for example
