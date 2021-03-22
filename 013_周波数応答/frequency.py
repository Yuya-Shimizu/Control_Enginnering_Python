"""
2021/03/07
@Yuya Shimizu

正弦波を入力したときの応答を調べる
"""
from control import tf
from control.matlab import lsim
import matplotlib.pyplot as plt 
import numpy as np
from for_plot import plot_set       #自分で定義した関数をインポート
#定義した関数について (https://qiita.com/Yuya-Shimizu/items/f811317d733ee3f45623)

fig, ax = plt.subplots(2, 2)

#2次遅れ系
zeta = 0.7
omega_n = 5
K = 1
P = tf([0, K*omega_n**2], [1, 2*zeta*omega_n, omega_n**2])

freq = [2, 5, 10, 20]   #周波数を4つ用意
Td = np.arange(0, 5, 0.01)  #シミュレーション時間

for i in range(2):
    for j in range(2):
        u = np.sin(freq[i+j+i*1]*Td)    #正弦波入力
        y, t, x0 = lsim(P, u, Td, 0)    #シミュレーション

        #描画
        ax[i, j].plot(t, u, ls='--', label='u')
        ax[i, j].plot(t, y, label='y')
        ax[i, j].set_title(f"freqency {freq[i+j+i*1]} [Hz]")
        plot_set(ax[i, j], 't', 'u, y')

ax[0, 0].legend()   #1つ目の図だけ凡例表示

plt.show()
