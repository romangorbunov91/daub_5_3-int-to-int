# Функция преобразования индексов по правилу "even symmetry".
def indx_even(k, N):
    reminder = abs(k) % (2*(N-1))
    if reminder <= (N-1):
        # rise
        return reminder
    else:
        # fall
        return 2*(N-1) - reminder

# Функция вычисления коэффициентов флуктуации.
def d_func(k, f, N, int_flag):
    if int_flag:
        return f[indx_even(2*k+1,N)] - (f[indx_even(2*k,N)] + f[indx_even(2*k+2,N)])//2
    else:
        return f[indx_even(2*k+1,N)] - (f[indx_even(2*k,N)] + f[indx_even(2*k+2,N)])/2