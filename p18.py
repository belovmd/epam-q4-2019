BOARD_SIZE = 8


def under_attack(col, queens):
    left = right = col

    for r, c in reversed(queens):
        left, right = left - 1, right + 1

        if c in (left, col, right):
            return True
    return False


def solve(n):
    if n == 0:
        return [[]]

    smaller_solutions = solve(n - 1)

    return [solution+[(n, i+1)]
        for i in range(BOARD_SIZE)
            for solution in smaller_solutions
                if not under_attack(i+1, solution)]
for answer in solve(BOARD_SIZE):
    print (answer)

# read stocks data, print status messages
with open('stocks.csv', 'r') as stocksFile:
    stocks = csv.reader(stocksFile)

    status_labels = {-1: 'down', 0: 'unchanged', 1: 'up'}
    for ticker, name, price, change, pct in stocks:
        status = status_labels[cmp(float(change), 0.0)]
        print ('%s is %s (%.2f)' % (name, status, float(pct)))
