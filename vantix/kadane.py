def alternating_kadane(L, first_negative=False):
    if first_negative:
        max_current = max_global = -L[0]
    else:
        max_current = max_global = L[0]
    if first_negative:
        for p in range(1, len(L)):
            x = L[p]
            y = (-1)**(p+1) * x
            max_current = max(y, max_current + y)
            if max_current > max_global:
                max_global = max_current
    else:
        for p in range(1, len(L)):
            x = L[p]
            y = (-1)**(p) * x
            max_current = max(y, max_current + y)
            if max_current > max_global:
                max_global = max_current
    return max_global

def alternating_max_subarray(L):
    max1 = alternating_kadane(L, first_negative=False)
    max2 = alternating_kadane(L, first_negative=True)
    return max(max1, max2)

def test(L, expected):
    #sol = alternating_max_subarray(L)
    sol = alternating_max_subarray(L)
    if sol == expected:
        print("Congratulations!")
    else:
        print(f"sol = {sol}")
        print(f"expected = {expected}")
    print()


if __name__ == "__main__":
    case = 0

    case += 1
    print(f"testCase{case:02d}")
    L = [10,3,-2,-9,5]
    expected = 19
    test(L, expected)

    case += 1
    print(f"testCase{case:02d}")
    L = [3,-2,-9,5]
    expected = 12
    test(L, expected)
