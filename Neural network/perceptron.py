def f(w : list, u : list, m : int) -> int:
    x = float(0)
    for i in range(m):
        x += (w[i]*u[i])
    if x < 0.0:
        return 0
    return 1


def perceptron(u : list, c : float):
    wt = [1.0 for _ in range(26)]

    t = 1
    counter = 0

    while counter < 5:
        zt = 1 if t % 5 < 3 else 0
        yt = f(wt, u[(t-1) % 5], len(wt))

        for i in range(26):
            wt[i] += c*(zt - yt)*u[(t-1) % 5][i]

        t += 1

        if zt == yt:
            counter += 1
        else:
            counter = 0
    
    print(f't: {t}')
    for ind, value in enumerate(wt):
        print(f'w[{ind}] : {value}')
    print('\n')


def main():
    u = list()

    u.append([1.0 if x in [6,7,12,17,22,25] else 0.0 for x in range(26)])
    u.append([1.0 if x in [2,3,8,13,25] else 0.0 for x in range(26)])
    u.append([1.0 if x in [5,6,11,16,21,25] else 0.0 for x in range(26)])
    u.append([1.0 if x in [6,7,8,11,13,16,17,18,25] else 0.0 for x in range(26)])
    u.append([1.0 if x in [10,11,12,15,17,20,21,22,25] else 0.0 for x in range(26)])

    for c in [1.0, 0.1, 0.01]:
        perceptron(u, c)


if __name__ == '__main__':
    main()


"""
u1 = [0 0 0 0 0
      0 1 1 0 0
      0 0 1 0 0
      0 0 1 0 0
      0 0 1 0 0 1]

u2 = [0 0 1 1 0
      0 0 0 1 0
      0 0 0 1 0
      0 0 0 0 0
      0 0 0 0 0 1]

u3 = [0 0 0 0 0
      1 1 0 0 0
      0 1 0 0 0
      0 1 0 0 0
      0 1 0 0 0 1]

u4 = [0 0 0 0 0
      0 1 1 1 0
      0 1 0 1 0
      0 1 1 1 0
      0 0 0 0 0 1]

u5 = [0 0 0 0 0
      0 0 0 0 0
      1 1 1 0 0
      1 0 1 0 0
      1 1 1 0 0 1]
"""