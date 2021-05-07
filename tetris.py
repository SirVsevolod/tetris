import numpy as np


def l_model_left(adress_zero, L):
    lmodel = []
    for i in range(L[0]):
        lmodel.append([adress_zero[0] - i, adress_zero[1]])
        if i + 1 == L[0]:
            for j in range(1, L[1]):
                lmodel.append([adress_zero[0] - i, adress_zero[1] - j])

    return lmodel


def l_model_right(adress_zero, L=(0,0)):
    lmodel = []
    for i in range(L[0]):
        lmodel.append([adress_zero[0] - i, adress_zero[1]])
        if i + 1 == L[0]:
            for j in range(1, L[1]):
                lmodel.append([adress_zero[0] - i, adress_zero[1] + j])

    return lmodel


def build_L(adress_zero, L, table):#(3, 2)
    answer = [True, True]

    try:
        model = l_model_left(adress_zero, L)
        for i in model:
            if i[1] >= 0:
                if table[i[0]][i[1]] == 1:
                    answer[0] = False
                    break
            else:
                answer[0] = False
                break
    except IndexError: answer[0] = False

    try:
        model = l_model_right(adress_zero, L)
        for i in model:
            if table[i[0]][i[1]] == 1:
                answer[1] = False
                break
    except IndexError: answer[1] = False

    return answer


def k_model(K, zero):
    kvadrat = K[0][0]
    model = []

    for i in range(kvadrat[1]):
        for j in range(kvadrat[0]):
            model.append([int(zero[0] - i), int(zero[1]) + j])

    return model


def Main(list_data):#[(3, 5), [((2, 2), 1)], [((3, 2), 1), ((2, 2), 2)]]

    T = list_data[0]
    K = list_data[1]
    L = list_data[2]

    try:
        T = list(T)
        T.reverse()
        table = np.zeros(shape=T)
        kmodel = k_model(K, [T[0]-1, 0])
        for i in kmodel:
            table[i[0]][i[1]] = 1
        #print(table)
    except IndexError:
        return False

    for i in L:#[((3, 2), 1), ((2, 2), 2)]
        #print(i)
        for j in range(i[1]):
            #print(str(j) + '--j')
            check1 = False
            for y in range(T[0] - 1, -1, -1):
                #print(str(y) + '-y')
                for x in range(0, T[1]):
                    #print(str(x) + "-x")
                    if table[y][x] == 0:
                        check = build_L([y, x], i[0], table)
                        #print(check)
                        if check == [True, False] or check == [True, True]:
                            model = l_model_left([y, x], i[0])
                            #print(model)
                            for point in model:
                                table[point[0]][point[1]] = 1
                            check1 = True
                            #print(table)
                            break
                        elif check == [False, True]:
                            model = l_model_right([y, x], i[0])
                            #print(model)
                            for point in model:
                                table[point[0]][point[1]] = 1
                            #print(table)
                            check1 = True
                            break
                if check1 == True:
                    break
    #print(table)
    count_table = 0
    for i in table:
        for j in i:
            if j == 1:
                count_table += 1
    count = 0
    for i in L:
        count += (i[0][0] + i[0][1] - 1) * i[1]

    count += K[0][0][0] * K[0][0][1]
    #print(count)
    if count_table == count:
        print(True)
    else:
        print(False)
