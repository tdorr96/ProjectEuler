import string

if __name__ == '__main__':

    with open('0042_words.txt', 'r') as open_f:
        for line in open_f:
            words = line.split(',')
            words = [w.replace('"', '') for w in words]

    triangle_numbers = [int(0.5 * n * (n+1)) for n in range(1, 31)]

    def word_value(word):
        return sum(string.ascii_uppercase.index(char)+1 for char in word)

    triangle_words = filter(lambda w: word_value(w) in triangle_numbers, words)
    print(len(list(triangle_words)))
