"""
2021/03/24
@Yuya Shimizu

正弦波を入力としたときの出力の振幅変化
"""

import numpy as np
import matplotlib.pyplot as plt
from control import tf, margin
from control.matlab import lsim
from for_plot import plot_set

P = tf([0, 1], [1, 1, 1.5, 1])
P2 = tf([0, 1], [1, 2, 2, 1])


#位相が180deg遅れる周波数(w_pc)を取得
_, _, wpc, _ = margin(P)
_, _, wpc2, _ = margin(P)

t = np.arange(0, 30, 0.01)  #シミュレーション時間
u = np.sin(wpc * t)
u2 = np.sin(wpc2 * t)
y = 0 * u
y2 = 0 * u2

#描画
fig, ax = plt.subplots(2, 2)
fig2, ax2 = plt.subplots(2, 2)
for i in range(2):
    for j in range(2):
        #出力をネガティブフィードバックして次の時刻の入力を生成
        u = np.sin(wpc*t) - y
        y, t, x0 = lsim(P, u, t, 0)

        u2 = np.sin(wpc2*t) - y2
        y2, _, _ = lsim(P2, u2, t, 0)

        ax[i, j].plot(t, u, ls='--', label = 'u')
        ax[i, j].plot(t, y, label = 'y')
        plot_set(ax[i, j], 't', 'u, y')

        ax2[i, j].plot(t, u2, ls='--', label = 'u')
        ax2[i, j].plot(t, y2, label = 'y')
        plot_set(ax2[i, j], 't', 'u, y')
        
fig.tight_layout()
fig.suptitle("unstable; input < output", size = 15)
fig2.tight_layout()
fig2.suptitle("stable; input > output", size = 15)

plt.show()
