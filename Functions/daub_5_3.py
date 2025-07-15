# version 1.0 by romangorbunov91
# 15-Jul-2025

import numpy as np
def daub_5_3(N):
    if ((N > 1)&((N % 2) == 0)):
       
        alpha = [-1/8, 1/4, 3/4, 1/4, -1/8]
        beta = [-1/2, 1, -1/2]
        
        N_alpha = len(alpha)
        N_beta = len(beta)
        
        V = np.zeros((N//2, (N + (N_alpha-2))))
        W = np.zeros((N//2, (N + (N_beta-2 ))))
        
        for idx in range(N//2):
            V[idx,(2*idx):(2*idx+N_alpha)] = alpha
            W[idx,(2*idx):(2*idx+N_beta )] = beta
        
        # Even symmetry.
        V[:,3] += V[:,1]
        V[:,4] += V[:,0]
        V[:,-3] += V[:,-1]
        
        W[:,-3] += W[:,-1]
    else:
        print('USER ERROR: Length (N) is incorrect!!!')
    return V[:,2:-1], W[:,0:-1]