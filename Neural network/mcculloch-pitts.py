def f(w, u, m):
    x = float(0)
    for i in range(m):
        x += (w[i]*u[i])
    if x < 0:
        return 0
    else:
        return 1


def logical_not():
    print('<<<BRAMKA NOT>>>')
    m = 2
    u = list()
    w = [-0.3,0.2]

    x = float(input('Wartosc:\n> '))
    u.append(x)
    u.append(float(1))
    return f(w,u,m)


def logical_and():
    print('<<<BRAMKA AND>>>')
    m = 3
    u = list()
    w = [0.3,0.3,-0.5]
    x1 = float(input('Pierwsza wartosc:\n> '))
    x2 = float(input('Druga wartosc:\n> '))
    
    u.append(x1)
    u.append(x2)
    u.append(float(1))
    return f(w,u,m)


def logical_nand():
    print('<<<BRAMKA NAND>>>')
    m = 3
    u = list()
    w = [-0.3,-0.3,0.5]

    x1 = float(input('Pierwsza wartosc:\n> '))
    x2 = float(input('Druga wartosc:\n> '))

    u.append(x1)
    u.append(x2)
    u.append(float(1))
    return f(w,u,m)


def logical_or():
    print('<<<BRAMKA OR>>>')
    m = 3
    u = list()
    w = [0.3,0.3,-0.1]

    x1 = float(input('Pierwsza wartosc:\n> '))
    x2 = float(input('Druga wartosc:\n> '))

    u.append(x1)
    u.append(x2)
    u.append(float(1))
    return f(w,u,m)


if __name__ == '__main__':
    choice = -1
    while choice != 0:
        choice = int(input('Podaj bramke\n1. NOT\n2. AND\n3. NAND\n4. OR\n0. Zamknij\n> '))
        if choice == 1:
            print(f'Wyjscie: {logical_not()}')
        elif choice == 2:
            print(f'Wyjscie: {logical_and()}')
        elif choice == 3:
            print(f'Wyjscie: {logical_nand()}')
        elif choice == 4:
            print(f'Wyjscie: {logical_or()}')
        elif choice == 0:
            break
        print('\n---------------------------------------------------------------\n')
