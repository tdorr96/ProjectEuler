import string


def alphabetical_value(name):

    return sum(string.ascii_uppercase.index(letter)+1 for letter in name)


if __name__ == '__main__':

    with open('0022_names.txt', 'r') as open_f:
        names = [name.replace('"', '') for name in open_f.readline().split(',')]

    names = sorted(names)
    total_score = sum((idx+1) * alphabetical_value(name) for idx, name in enumerate(names))
    print(total_score)


