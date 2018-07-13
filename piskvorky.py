import random

""" # n*n velkost plochy
       while True:
           try:
               size = int(input("Zadajte velkost plochy: "))
               break
           except ValueError:
               print("Zly vstup, skuste este raz")
   """

size = 10

board = [[" " for x in range(size)] for y in range(size)]
values = [[0 for x in range(size)] for y in range(size)]


def clear_board(board):
    for i in range(size):
        for j in range(size):
            board[i][j] = " "


def clear_values(values):
    for i in range(size):
        for j in range(size):
            values[i][j] = 0


def solve_index(x, y, size):
    return x*size + y


def solve_x(index, size):
    b = int(index)
    return int(b/size)


def solve_y(index, size):
    c = int(index)
    return c % size


def print_board(board, size):
    print(" ", end=" ")
    for i in range(size):
        print(i, " ", end=" ")
    print()
    for x in range(0, size):
        print(x, ' | '.join(board[x]))
        print("  -------------------------------------")


def print_values(values, size):
    for x in range(0, size):
        print(values[x])


def first_init_values(size, values):
    # rows and columns
    for i in range(size):
        for j in range(size):
            if j+4 < size:
                for k in range(5):  # jedna patica
                    values[i][j+k] += 10
            if i+4 < size:
                for k in range(5):
                    values[i+k][j] += 10

    # diagonals
    for i in range(size):
        for j in range(size):
            if i+4 < size and j+4 < size:
                for k in range(5):
                    values[i+k][j+k] += 10
            if i+4 < size and j-4 >= 0:
                l = 0
                for k in range(0, -5, -1):
                    values[i+l][j+k] += 10
                    l += 1


def calculate(tmp, board, size):
    count_x = {1: 45, 2: 70, 3: 400, 4: 1500}
    count_o = {1: 50, 2: 80, 3: 420, 4: 5000}
    count_of_char = 0
    contains_x = False
    contains_o = False
    value = 0

    for i in range(5):
        if tmp[i] == "X":
            contains_x = True
            count_of_char += 1
        elif tmp[i] == "O":
            contains_o = True
            count_of_char += 1
        if contains_x and contains_o:
            # ak je v patici aj X aj O tak sa nic nepripocitava, lebo nikto nemoze ziskat tuto paticu
            return 0

    if not contains_x and not contains_o:
        value = 10
    elif contains_x:
        if count_of_char == 5:
            print("VYHRA!")
            value = -1
        else:
            value = count_x[count_of_char]
    elif contains_o:
        if count_of_char == 5:
            print("PREHRA!")
            value = -2
        else:
            value = count_o[count_of_char]

    return value


def solve_five(index, size, values, board):
    x = solve_x(index, size)
    y = solve_y(index, size)
    value = 0
    for i in range(size):
        include_index = False
        tmp = []
        for k in range(5):
            if 0 <= i+k < size:
                tmp.append(board[x][i+k])
                tmp_index = solve_index(x, i+k, size)
                if tmp_index == index:
                    include_index = True
        if len(tmp) == 5 and include_index:
            tmp_value = calculate(tmp, board, size)
            if tmp_value == -1:  # vyhra
                return -1
            elif tmp_value == -2:
                return -2  # prehra
            else:
                value += tmp_value

    for i in range(size):
        include_index = False
        tmp = []
        for k in range(5):
            if 0 <= i+k < size:
                tmp.append(board[i+k][y])
                tmp_index = solve_index(i+k, y, size)
                if tmp_index == index:
                    include_index = True
        if len(tmp) == 5 and include_index:  # iba ak obsahuje index, iba vtedy sa pripocita vypocitana hodnota
            tmp_value = calculate(tmp, board, size)
            if tmp_value == -1:
                return -1
            elif tmp_value == -2:
                return -2  # prehra
            else:
                value += tmp_value

    for i in range(size):
        for j in range(size):
            include_index = False
            tmp = []
            for k in range(5):
                if 0 <= i+k < size and 0 <= j+k < size:
                    tmp.append(board[i+k][j+k])
                    tmp_index = solve_index(i+k, j+k, size)
                    if tmp_index == index:
                        include_index = True
            if len(tmp) == 5 and include_index:
                tmp_value = calculate(tmp, board, size)
                if tmp_value == -1:
                    return -1  # vyhra
                elif tmp_value == -2:
                    return -2  # prehra
                else:
                    value += tmp_value

    for i in range(size):
        for j in range(size-1, -1, -1):
            include_index = False
            tmp = []
            for k in range(5):
                if 0 <= i + k < size and 0 <= j - k < size:
                    tmp.append(board[i + k][j - k])
                    tmp_index = solve_index(i + k, j - k, size)
                    if tmp_index == index:
                        include_index = True
            if len(tmp) == 5 and include_index:
                tmp_value = calculate(tmp, board, size)
                if tmp_value == -1:
                    return -1
                elif tmp_value == -2:
                    return -2  # prehra
                else:
                    value += tmp_value
    values[x][y] = value
    if board[x][y] != " ":  # uz obsadene policko
        values[x][y] = 0
        return 0
    return 1


def after_round(x, y, values, board, size):
    print(x, y)
    tmp = []
    j = 4
    for i in range(-4, 5):
        # rows
        if 0 <= i+x < size:
            tmp.append(solve_index(x+i, y, size))
        # columns
        if 0 <= i+y < size:
            tmp.append(solve_index(x, y+i, size))
        # diagonals
        if 0 <= x+i < size and 0 <= y+i < size:
            tmp.append(solve_index(x+i, y+i, size))
        if 0 <= x+i < size and 0 <= y+j < size:
            tmp.append(solve_index(x+i, y+j, size))
        j -= 1

    uniq_tmp = list(set(tmp))
    uniq_tmp.remove(solve_index(x, y, size))
    length = len(uniq_tmp)
    for i in range(length):
        tmp_value = solve_five(uniq_tmp[i], size, values, board)  # body, ktorym treba prepocitat hodnoty
        if tmp_value == -1:  # vyhra
            break
        elif tmp_value == -2:  # prehra
            break
        values[x][y] = 0  # uz navstiveny vrchol

    return tmp_value


first_init_values(size, values)


def test_verify():  # aby sa zavolal test ked sa spusti verify_values ???
    print(board)
    pass


def move(moves):
    nums = [int(x) for x in moves]

    length = len(nums)
    print("dlzka: ", length)
    print(nums)

    if length == 0:  # uz je koniec hry
        clear_board(board)
        clear_values(values)
        nums = []
    else:
        assert length % 2 == 1  # isiel clovek ma ist pocitac
        x = solve_x(nums[length-1], size)
        assert 0 <= x < size
        y = solve_y(nums[length-1], size)
        assert 0 <= y < size
        board[int(x)][int(y)] = "X"
        tmp_value = after_round(int(x), int(y), values, board, size)
        if tmp_value == -1:  # vyhra
            # clear_board(board)
            nums.append(-1)

        max_value = values[0][0]
        max_indices = []
        for i in range(size):
            for j in range(size):
                if values[i][j] > max_value:
                    max_value = values[i][j]
                    max_indices = [solve_index(i, j, size)]
                elif values[i][j] == max_value:
                    max_indices.append(solve_index(i, j, size))

        rand_max_index = random.choice(max_indices)
        x = solve_x(rand_max_index, size)
        assert 0 <= x < size
        y = solve_y(rand_max_index, size)
        assert 0 <= y < size

        if max_value == 0:
            print("REMIZA")
            # clear_board(board)
            nums.append(-3)  # remiza
        else:
            board[x][y] = "O"
            nums.append(solve_index(x, y, size))

            tmp_value = after_round(int(x), int(y), values, board, size)
            if tmp_value == -2:  # prehra
                # clear_board(board)
                nums.append(-2)
        print("pohyby: ", nums)

    return nums

