arr = [int(input()) for _ in range(9)]
stop = 0

def permutation(arr, r):
    used = [0]*len(arr)

    def generate(chosen, used):
        global stop
        if len(chosen) == r and sum(chosen) == 100:
            stop = 1
            chosen.sort()
            for x in chosen:
                print(x)
            return

        if sum(chosen) > 100:
            return

        for i in range(len(arr)):
            if used[i] == 0:
                used[i] = 1
                chosen.append(arr[i])
                generate(chosen, used)

                if stop == 1:
                    return
                else:
                    used[i] = 0
                    chosen.pop()
    generate([], used)

permutation(arr, 7)
