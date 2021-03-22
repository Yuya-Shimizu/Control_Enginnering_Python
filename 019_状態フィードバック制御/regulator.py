"""
2021/03/21
@Yuya Shimizu

状態フィードバック制御（最適レギュレータ）
"""
import numpy as np
import matplotlib.pyplot as plt
from control import ss
from control.matlab import lqr, initial, care
from for_plot import plot_set

##状態空間モデル
A = [[ 0, 1],
        [-4, 5]]
B = [[0],
        [1]]
C = [[ 1, 0],
        [ 0, 1]]
D = [[0],
        [0]]

P = ss(A, B, C, D)

##最適レギュレータ
Q = [[100, 0],
        [   0, 1]]
R = 1

F, X, E = lqr(P.A, P.B, Q, R)  #F: フィードバックゲイン  X: リカッチ方程式の解  E: 閉ループ系の極
F = -F  #関数の仕様で符号が反転するため修正（lqrではu=-Fxに対するFが得られる．）

print('---フィードバックゲイン---')
print(F)
print(-(1/R)*P.B.T*X)
print('---閉ループ極---')
print(E)
print(np.linalg.eigvals(P.A+P.B*F))
"""
#care関数を使っても同様のことができる
X, E, F = care(P.A, P.B, Q, R)  #lqrとは戻り値の順が違う
F = -F
print('---フィードバックゲイン---')
print(F)
print('---閉ループ極---')
print(E)
"""

##状態フィードバック制御
Acl = P.A + P.B*F   #入力をFとする
Pfb = ss(Acl, P.B, P.C, P.D)    #状態フィードバック制御

Td = np.arange(0, 5, 0.01)  #シミュレーション時間
x0 = [-0.3, 0.4]    #初期状態
x, t = initial(Pfb, Td, x0)

#描画
fig, ax = plt.subplots()
ax.plot(t, x[:, 0], label = '$x_1$')
ax.plot(t, x[:, 1], ls = '-.', label = '$x_2$')
ax.set_title('response of state - regulator')
plot_set(ax, 't', 'x', 'best')
plt.show()
