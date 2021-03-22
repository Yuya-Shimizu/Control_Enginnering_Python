"""
2021/03/21
@Yuya Shimizu

可観測性
"""
import numpy as np
from control import ss
from control.matlab import obsv

def observability(A, B, C, D):
    #状態空間モデル（Matlab表記でも記述可能）
    P = ss(A, B, C, D)

    #可制御性check
    Uo = obsv(P.A, P.C)                     #可観測性行列
    n = len(Uo)
    det = np.linalg.det(Uo)                #行列式
    rank = np.linalg.matrix_rank(Uo)  #ランク
    print(f"Uo = \n{Uo}")
    print(f"n = {n}")
    print(f"det(Uo) = {det}")
    print(f"rank(Uo) = {rank}")

    if n == rank:
        print('可観測である')
        return True
    else:
        print('可観測でない')
        return False


if __name__ == '__main__':
    A = '0 1; -4 5'
    B = '0; 1'
    C = '1 0'
    D = '0'

    observability(A, B, C, D)
