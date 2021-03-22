"""
2021/03/04
@Yuya Shimizu

入出力安定（BIBO安定）
"""
from control import tf, pole

##伝達関数の作成
#1次遅れ系
P1 = tf([0, 1], [1, 1])     #1/(s+1)
P2 = tf([0, 1], [-1, 1])     #1/(-s+1)

#2次遅れ系
P3 = tf([0, 1], [1, 0.05, 1])     #1/(s^2+0.05s+1)
P4 = tf([0, 1], [1, -0.05, 1])     #1/(s^2-0.05s+1)


##極の計算
#1次遅れ系
pole1 = pole(P1)
pole2 = pole(P2)

#2次遅れ系
pole3 = pole(P3)
pole4 = pole(P4)

print(f"<極によるBIBO安定判定>\n-----1次遅れ系-----\n(例1){P1}\n極:s={pole1[0]}\t\t⇒\tBIBO安定である")
print(f"\n(例2){P2}\n極:s={pole2[0]}\t\t⇒\tBIBO安定でない")
print(f"\n-----2次遅れ系-----\n(例3){P3}\n極:s={pole3}\t\t⇒\tBIBO安定である")
print(f"\n(例4){P4}\n極:s={pole4}\t\t⇒\tBIBO安定でない")

##別記法
"""
#極が分母多項式の根ということより，次のようにして記述することもできる

from control import tfdata
import numpy as np

#分子多項式と分母多項式に分ける．
Dp = []
P = [P1, P2, P3, P4]
for p in P:
    [[N]], [[D]] = tfdata(p)
    Dp.append(D)

Pole = []
for dp in Dp:
    root = np.roots(dp)
    Pole.append(root)

for i in range(len(Pole)):
    print(f"\n(例{i+1}){P[i]}\n極:s={Pole[i]}\n")
"""
