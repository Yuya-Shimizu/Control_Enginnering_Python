"""
2021/02/14
@Yuya Shimizu

伝達関数モデル（アーム）
"""
from control import tf


def arm_tf(J, mu, M, g, l):
    ##伝達関数を作成
    Np = [0, 1]       #分子の多項式係数（0*s + 1）
    Dp = [J, mu, M*g*l]    #分母の多項式係数（M*s^2 + μ*s + M*g*l）

    P = tf(Np, Dp)

    return P

if __name__ == '__main__':
    J    =   1       #慣性モーメント
    mu =   1       #粘性係数
    M   =   1       #質量
    g    =   9.8    #重力加速度
    l     =   1      #回転軸から重心までの距離
    P = arm_tf(J, mu, M, g, l)

    print(f"伝達関数モデル（アーム）\n{P}\n慣性モーメント: {J}\n粘性係数: {mu}\n質量: {M}\n重力加速度: {g}\n回転軸から重心までの距離: {l}")
