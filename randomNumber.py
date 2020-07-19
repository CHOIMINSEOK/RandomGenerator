from random import randrange

get_zero_or_one = lambda: randrange(2)


def get_random(max_number):
    # Please implement this method # using only `get_zero_or_one`
    k = 0
    while max_number > 2 ** k:
        k = k + 1

    num = max_number
    while num >= max_number:
        num = 0
        for i in range(0, k):
            num += (2 ** i) * get_zero_or_one()

    return num


# Test
numberCount = [0] * 30
i = 0

while i < 9999 :
    numberCount[get_random(30)] += 1
    i += 1

print numberCount
