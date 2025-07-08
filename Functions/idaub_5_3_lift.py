from Functions.user_functions import indx_even, d_func
# version x.x by romangorbunov91
# 08-Jul-2025

def idaub_5_3_lift(coeff, int_flag):
    N = len(coeff)
    f = [0] * N
    
    a = coeff[:(N//2)]
    d = coeff[(N//2):]
    
    # Odd values.
    if int_flag:
        for k in range(N//2):
            f[2*k] = a[k] - (d_func(k-1, f, N, int_flag=False) + d[k]) //4
    else:
        for k in range(N//2):
            f[2*k] = a[k] - (d_func(k-1, f, N, int_flag=False) + d[k]) /4    
    
    # Even values.
    if int_flag:
        for k in range(N//2):
            f[2*k+1] = d[k] + (f[2*k] + f[indx_even(2*k+2,N)]) //2
    else:
        for k in range(N//2):
            f[2*k+1] = d[k] + (f[2*k] + f[indx_even(2*k+2,N)]) /2

    return f