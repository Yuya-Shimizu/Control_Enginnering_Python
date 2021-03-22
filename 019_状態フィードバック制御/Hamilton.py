"""
2021/03/21
@Yuya Shimizu

状態フィードバック制御（ハミルトン行列の固有値を求める）
"""
import numpy as np
import matplotlib.pyplot as plt
from control import ss
from control.matlab import acker, initial, care
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

##ハミルトン行列
Q = [[100, 0],
        [   0, 1]]
R = 1

H1 = np.c_[P.A, -P.B*(1/R)*P.B.T]   #配列の連結np.c_はnp.hstackと同じ
H2 = np.c_[Q, P.A.T]
H = np.r_[H1, -H2]                          #配列の連結np.c_はnp.vstackと同じ
eigH = np.linalg.eigvals(H)
print(eigH)

print('---ハミルトン行列の安定固有値---')
eigH_stable = [i for i in eigH if i < 0]    #実部が負の固有値を抽出
print(eigH_stable)

F = -acker(P.A, P.B, eigH_stable)  #関数の仕様で符号が反転するため修正（lqrではu=-Fxに対するFが得られる．）

print('---フィードバックゲイン---')
print(F)

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
ax.set_title('response of state - pole placement method by Hamilton')
plot_set(ax, 't', 'x', 'best')
plt.show()
