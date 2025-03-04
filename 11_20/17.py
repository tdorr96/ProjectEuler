digits_to_word = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}
teens_to_word = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}
tens_to_word = {
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}


def number_to_word(n):

    if n == 1000:
        return "one thousand"

    s = ""

    if n >= 100:
        hundreds = int(n/100)
        s += digits_to_word[hundreds] + " hundred"
        n -= hundreds * 100
        if n > 0:
            s += " and "

    if n > 0:
        assert 1 <= n <= 99
        if n in teens_to_word:
            s += teens_to_word[n]
        else:
            tens = n - (n % 10)
            digits = n % 10
            if tens > 0:
                s += tens_to_word[tens]
                if digits > 0:
                    s += '-'
            if digits > 0:
                s += digits_to_word[digits]

    return s


def total_letters(start, end):
    # Counts how many letters are used in writing out the words from start to end (inclusive)

    letter_count = 0
    for n in range(start, end+1):
        s = number_to_word(n)
        s = s.replace(' ', '')
        s = s.replace('-' ,'')
        letter_count += len(s)
    return letter_count


if __name__ == '__main__':

    for d in [digits_to_word, teens_to_word, tens_to_word]:
        for n in d.keys():
            assert(number_to_word(n) == d[n])

    test_cases = {
        21: 'twenty-one',
        99: 'ninety-nine',
        100: 'one hundred',
        101: 'one hundred and one',
        200: 'two hundred',
        555: 'five hundred and fifty-five',
        690: 'six hundred and ninety',
        999: 'nine hundred and ninety-nine'
    }

    for n in test_cases.keys():
        assert(number_to_word(n) == test_cases[n])

    assert(total_letters(1, 5) == 19)

    print(total_letters(1, 1000))


