"""
2021/04/07
@Yuya Shimizu

オブザーバによる状態推定
"""
import numpy as np
import matplotlib.pyplot as plt
from control import ss, acker
from control.matlab import initial, lsim
from for_plot import plot_set

#係数行列
A = '0 1; -4 5'
B = '0; 1'
C = '1 0'
D = '0'

#状態空間モデル
P = ss(A, B, C, D)

#オブザーバ極
observer_poles = [-15+5j, -15-5j]

#オブザーバゲインの設計（状態フィードバックの双対）
L = -acker(P.A.T, P.C.T, observer_poles).T

#描画に向けて
fig, ax = plt.subplots(1, 2)
Td = np.arange(0, 3, 0.01)   #シミュレーション時間
X0 = [-1, 0.5]                      #初期状態

#制御対象Pを安定化する状態フィードバックゲインの設計
regulator_poles = [-5+5j, -5-5j]
F = -acker(P.A, P.B, regulator_poles)

#真の状態の振る舞い
Gsf = ss(P.A + P.B*F, P.B, np.eye(2), [[0], [0]])
x, t = initial(Gsf, Td, X0)     #初期条件応答
ax[0].plot(t, x[:, 0], ls='-.', label='${x}_1$')
ax[1].plot(t, x[:, 1], ls='-.', label='${x}_2$')

#オブザーバで推定した状態の振る舞い
#入力　u = Fx
u = [ [F[0, 0]*x[i, 0] + F[0, 1]*x[i, 1]] for i in range(len(x)) ]
#出力　y = Cx
y = x[:, 0]
#オブザーバによる状態推定
Obs = ss(P.A + L*P.C, np.c_[P.B, -L], np.eye(2), [[0, 0], [0, 0]] )
xhat, t, x0 = lsim(Obs, np.c_[u, y], Td, [0, 0])
ax[0].plot(t, xhat[:, 0], label='$\hat{x}_1$')
ax[1].plot(t, xhat[:, 1], label='$\hat{x}_2$')

for i in [0, 1]:
    plot_set(ax[i], 't', ' ', 'best')

ax[0].set_ylabel('$x_1, \hat{x}_1$')
ax[1].set_ylabel('$x_2, \hat{x}_2$')

fig.tight_layout()
fig.suptitle(f"estimation with observer; Obs_Pole={observer_poles}")

plt.show()
