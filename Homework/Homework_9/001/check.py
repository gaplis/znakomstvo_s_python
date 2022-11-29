def check_win(array, xo, count):
    if array[0][0] == xo and array[1][0] == xo and array[2][0] == xo \
        or array[0][1] == xo and array[1][1] == xo and array[2][1] == xo \
        or array[0][2] == xo and array[1][2] == xo and array[2][2] == xo \
        or array[0][0] == xo and array[0][1] == xo and array[0][2] == xo \
        or array[1][0] == xo and array[1][1] == xo and array[1][2] == xo \
        or array[2][0] == xo and array[2][1] == xo and array[2][2] == xo \
        or array[0][0] == xo and array[1][1] == xo and array[2][2] == xo \
        or array[0][2] == xo and array[1][1] == xo and array[2][0] == xo:
        return xo
    
    if count == 9:
        return 'Ничья'
    
    return False