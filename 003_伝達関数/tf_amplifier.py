"""
2021/02/14
@Yuya Shimizu

伝達関数モデル（増幅回路）
"""
from control import tf


def amplifier_tf(R1, R2):
    ##伝達関数を作成
    Np = [0, -R2]       #分子の多項式係数（0*s - R2）
    Dp = [R1*R2, R1]    #分母の多項式係数（R1*R2*s + R1）

    P = tf(Np, Dp)

    return P

if __name__ == '__main__':
    R1 =  1   #抵抗器1
    R2 =  1   #抵抗器2
    
    P = amplifier_tf(R1, R2)

    print(f"伝達関数モデル（アーム）\n{P}\n抵抗器1: {R1}\n抵抗器2: {R2}")
