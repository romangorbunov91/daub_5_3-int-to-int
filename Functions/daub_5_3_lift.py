from Functions.user_functions import indx_even, d_func
# version 1.0 by romangorbunov91
# 08-Jul-2025

def daub_5_3_lift(f, int_flag):
    N = len(f)
    d = [0] * (N//2)
    a = [0] * (N//2)
    
    for k in range(N//2):
        d[k] = d_func(k, f, N, int_flag)
        if int_flag:
            a[k] = f[indx_even(2*k,N)] + (d_func(k-1, f, N, int_flag) + d[k]) //4
        else:
            a[k] = f[indx_even(2*k,N)] + (d_func(k-1, f, N, int_flag) + d[k]) /4
    return a+d