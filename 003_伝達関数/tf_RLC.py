"""
2021/02/14
@Yuya Shimizu

伝達関数モデル（RLC回路）
"""
from control import tf


def RLC_tf(R, L, C):
    ##伝達関数を作成
    Np = [0, 1]       #分子の多項式係数（0*s + 1）
    Dp = [L*C, R*C, 1]    #分母の多項式係数（L*C*s^2 + R*C*s + 1）

    P = tf(Np, Dp)

    return P

if __name__ == '__main__':
    R =  1   #抵抗器
    L =  1   #コイル
    C =  1   #コンデンサ
    
    P = RLC_tf(R, L, C)

    print(f"伝達関数モデル（アーム）\n{P}\n抵抗器: {R}\nコイル: {L}\nコンデンサ: {C}")
