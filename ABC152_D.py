N = int(input())


def calc(N):
    digit = 0
    exp10 = 1

    while exp10 <= N:
        digit += 1
        exp10 *= 10

    if digit == 1:
        answer = N
        return answer

    answer = 0
    if digit == 2:
        for i in range(1, 10):
            for j in range(1, 10):
                if i == j:
                    if 10 * i + i <= N:
                        answer += 4
                    else:
                        answer += 1
                else:
                    Cij = 10 * i + j
                    Cji = 10 * j + i
                    if Cij <= N and Cji <= N:
                        answer += 1
        return answer

    else:
        for i in range(1, 10):
            for j in range(1, 10):
                if i == j:
                    Cij = 2
                    exp10 = 1
                    for k in range(digit - 3):
                        exp10 *= 10
                        Cij += exp10
                    n = exp10 * 100 * i + i
                    if n <= N:
                        if exp10 * 100 * (i + 1) > N:
                            for k in range(N - n + i + 1):
                                if k % 10 == i:
                                    Cij += 1
                        else:
                            Cij += exp10 * 10
                    answer += Cij * Cij
                else:
                    Cij = 1
                    Cji = 1
                    exp10 = 1
                    for k in range(digit - 3):
                        exp10 *= 10
                        Cij += exp10
                        Cji += exp10
                    n = exp10 * 100 * i + j
                    m = exp10 * 100 * j + i
                    if n <= N:
                        if exp10 * 100 * (i + 1) > N:
                            for k in range(N - n + j + 1):
                                if k % 10 == j:
                                    Cij += 1
                        else:
                            Cij += exp10 * 10
                    if m <= N:
                        if exp10 * 100 * (j + 1) > N:
                            for k in range(N - m + i + 1):
                                if k % 10 == i:
                                    Cji += 1
                        else:
                            Cij += exp10 * 10

                    answer += Cij * Cji
        return answer


print(calc(N))
# when N = 2020 it doesn't work somehow...
