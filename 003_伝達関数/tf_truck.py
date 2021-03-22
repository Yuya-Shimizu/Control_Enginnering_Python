"""
2021/02/14
@Yuya Shimizu

伝達関数モデル（台車）
"""
from control import tf


def truck_tf(M, mu):
    ##伝達関数を作成
    Np = [0, 1]       #分子の多項式係数（0*s + 1）
    Dp = [M, mu]    #分母の多項式係数（M*s + μ）

    P = tf(Np, Dp)

    return P

if __name__ == '__main__':
    M   =    1       #質量 
    mu =    1       #粘性係数
    P = truck_tf(M, mu)

    print(f"伝達関数モデル（台車）\n{P}\n質量: {M}\n粘性係数: {mu}")
