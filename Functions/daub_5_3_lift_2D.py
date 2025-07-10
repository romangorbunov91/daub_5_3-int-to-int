import numpy as np
from Functions.daub_5_3_lift import daub_5_3_lift
# version 0.1 by romangorbunov91
# 10-Jul-2025

# Преобразование выполняется в следующей последовательности:
# 1. Преобразование строк.
# 2. Изменение порядка строк (bottom-up).
# 3. Преобразование столбцов.
# 4. Изменение порядка строк (bottom-up).

def daub_5_3_lift_2D(f, int_flag):
    Nrow, Ncol = np.shape(f)
    
    # 1. Преобразование строк.
    coeff_row = np.zeros_like(f)
    for idx in range(Nrow):
        coeff_row[idx,:] = daub_5_3_lift(f[idx,:], int_flag)
    
    # 2. Изменение порядка строк (bottom-up).
    coeff_row = np.flipud(coeff_row)
    print(coeff_row)
    
    # 3. Преобразование столбцов.
    # Предварительно - преобразуем столбцы в строки.
    coeff = np.zeros_like(f).T
    for idx in range(Ncol):
        coeff[idx,:] = np.array(daub_5_3_lift(coeff_row[:,idx].reshape(1,-1)[0], int_flag))
    
    # 4. Изменение порядка строк (bottom-up).
    # Предварительно - обратное преобразуем строки в столбцы.
    return np.flipud(coeff.T)