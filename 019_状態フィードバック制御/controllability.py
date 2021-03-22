"""
2021/03/21
@Yuya Shimizu

可制御性
"""
import numpy as np
from control import ss
from control.matlab import ctrb

def controllability(A, B, C, D):
    #状態空間モデル（Matlab表記でも記述可能）
    P = ss(A, B, C, D)

    #可制御性check
    Uc = ctrb(P.A, P.B)                     #可制御性行列
    n = len(Uc)
    det = np.linalg.det(Uc)                #行列式
    rank = np.linalg.matrix_rank(Uc)  #ランク
    print(f"Uc = \n{Uc}")
    print(f"n = {n}")
    print(f"det(Uc) = {det}")
    print(f"rank(Uc) = {rank}")

    if n == rank:
        print('可制御である')
        return True
    else:
        print('可制御でない')
        return False


if __name__ == '__main__':
    A = '0 1; -4 5'
    B = '0; 1'
    C = '1 0'
    D = '0'

    controllability(A, B, C, D)
