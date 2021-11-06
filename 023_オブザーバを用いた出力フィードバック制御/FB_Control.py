"""
2021/04/08
@Yuya Shimizu

出力フィードバック制御器の設計
"""
import numpy as np
import matplotlib.pyplot as plt
from control import ss, acker, feedback, tf
from control.matlab import initial, lsim
from for_plot import plot_set

#係数行列
A = '0 1; -4 5'
B = '0; 1'
C = '1 0'
D = '0'

#状態空間モデル
P = ss(A, B, C, D)

#状態フィードバックゲインの設計
regulator_poles = [-5+5j, -5-5j]
F = -acker(P.A, P.B, regulator_poles)

#オブザーバゲインの設計
observer_poles = [-15+5j, -15-5j]
L = -acker(P.A.T, P.C.T, observer_poles).T

#出力フィードバック（オブザーバ+状態フィードバック）
K = ss(P.A+P.B*F+L*P.C, -L, F, 0)

#出力フィードバック系
Gfb = feedback(P, K, sign=1)

fig, ax = plt.subplots()
Td = np.arange(0, 3, 0.01)

#出力フィードバック制御なし
y, t = initial(P, Td, [-1, 0.5])
ax.plot(t, y, ls = '-.', label = 'w/o controller')
#出力フィードバック制御あり
y, t = initial(Gfb, Td, [-1, 0.5, 0, 0])
ax.plot(t, y, label = 'w/ controller')

plot_set(ax, 't', 'y', 'best')

ax.set_title(f"Feesback with observer; Obs_Pole={observer_poles}")

plt.show()
