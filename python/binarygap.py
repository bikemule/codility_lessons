
def binary_gap(num):
    mask = 1
    
    max_gap = 0
    gap = 0

    while num > 0:
        if num & mask == 0:
            gap += 1
        else:
            if max_gap < gap:
                max_gap = gap
            gap = 0
        num = num >> 1

    return max_gap

def print_binary_gap(num):
    print("{0} ({0:b}) has a binary gap of: {1}".format(num, binary_gap(num)))

if __name__ == '__main__':
    print_binary_gap(1)
    print_binary_gap(2)
    print_binary_gap(6)
    print_binary_gap(255)
    print_binary_gap(437)
    print_binary_gap(437000)
    print_binary_gap(0xF0DA4C9D7)
