def alternating_kadane(L):
    max_current = max_global = L[0]
    for p in range(1, len(L)):
        x = L[p]
        y = (-1)**(p+1) * x
        if p % 2 == 0:
            max_current = max(y, max_current + y)
        else:
            #max_current = max(max_current, max_current + y)
            pass
        if max_current > max_global:
            max_global = max_current
    return max_global

def alternating_max_subarray(L):
    max1 = alternating_kadane(L)
    max2 = alternating_kadane(L[1:])
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
