import time

start_time = time.time()


def collatz(n):
    results = {}
    for number in range(2, n + 1):
        value = number
        steps = 0
        while value != 1:
            value = operations(value)
            steps += 1
        results[number] = steps
    return max(results.items(), key=lambda x: x[1])


def operations(value):
    if value % 2 == 0:
        return value // 2
    return 3 * value + 1


if __name__ == "__main__":
    print(collatz(1000))
    print('%s second' % (time.time() - start_time))
