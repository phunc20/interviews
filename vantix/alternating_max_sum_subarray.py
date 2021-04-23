def alternating_max_subarray(L):
    max_ = -float("inf")
    head = 0
    #def suboptimal(L, head_):
    def suboptimal(head_):
        sub_max = L[head_]
        length = 1
        if head_ == len(L) - 1:
            return sub_max, length
        so_far = sub_max
        #for i in range(head_, len(L)):
        for i, num in enumerate(L[head_+1:len(L)]):
            so_far += (-1)**(i+1) * num
            if so_far > sub_max:
                sub_max = so_far
                length = i + 2
        return sub_max, length
    length = 1
    for index in range(len(L)):
        sub_max, length_ = suboptimal(index)
        if sub_max > max_:
            max_ = sub_max
            head = index
            length = length_
    return max_, head, length


def test(L, expected):
    #sol = alternating_max_subarray(L)
    sol, head, length = alternating_max_subarray(L)
    if sol == expected:
        print("Congratulations!")
    else:
        print(f"sol = {sol}")
        print(f"expected = {expected}")
        print(f"head = {head}")
        print(f"length = {length}")
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
