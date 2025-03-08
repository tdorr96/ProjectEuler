def all_ways_coin(n, coins):
    # Use recursion. E.g., if we were looking at £2:
    # - £2 plus all the ways of adding up to £2-£2 = 0, i.e. None
    # - £1 plus al the ways of adding up to £2-£1 = £1
    # - 50p plus all the ways of adding up to £2-50p = £1.50
    # We have to be careful to avoid duplicates though, so when we recursively call, only allow coins
    # to be used that are smaller or equal to the one just used to reduce it

    all_ways = []
    for index, coin in enumerate(coins):
        if coin < n:
            sub_ways = all_ways_coin(n-coin, coins[index:])
            all_ways.extend(map(lambda sub_l: [coin] + sub_l, sub_ways))
        elif coin == n:
            all_ways.append([coin])

    return all_ways


if __name__ == '__main__':

    print(len(all_ways_coin(200, [200, 100, 50, 20, 10, 5, 2, 1])))