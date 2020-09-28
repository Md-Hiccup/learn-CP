n = 5
rounds = [[1, 2, 100], [2, 4, 100], [3, 4, 100], [4,5,100]]

def mx_rnd(n, rounds):
    arr = [0]*n

    for r in rounds:
        st, ed, cont = r
        print(st, ed, cont)

        tmp = [0]*n
        tmp[st-1: ed] = [cont]*(ed-st+1)
        arr = [tmp[i] + arr[i] for i in range(len(arr))]

        # while st <= ed:
        #     arr[st-1] += cont
        #     st += 1

    print(arr)
    return (max(arr))


mx = mx_rnd(n, rounds)
print(mx)