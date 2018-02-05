def coins(n):
    """Simulate the results of coin-flipping.
    n+1 total coins
    n people
    each person flips over coins that are multiples of their n.
    """

    total_tails = 0

    coin_list = [0] * (n + 1)

    for i in range(1, n+1):
        k = i
        while k < n:
            coin_list[k] = int(not coin_list[k])
            k += i

    return coin_list


if __name__ == '__main__':
    print(coins(2))
