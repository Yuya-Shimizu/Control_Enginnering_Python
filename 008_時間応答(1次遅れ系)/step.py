"""
2021/02/26
@Yuya Shimizu

時間応答（1次遅れ系）
"""

from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
from for_plot import *    #自分で定義した関数をインポート
#定義した関数について (https://qiita.com/Yuya-Shimizu/items/f811317d733ee3f45623)


##1次遅れ系のステップ応答

T, K = 0.5, 1   #時定数とゲインの設定
P = tf([0, K], [T, 1])  #1次遅れ系
y, t = step(P, np.arange(0, 5, 0.01))   #ステップ応答（0~5秒で，0.01刻み）

fig1, ax1 = plt.subplots()
ax1.plot(t, y)
plot_set(ax1, 't', 'y') #グリッドやラベルを与える関数(自作のfor_plotライブラリより)
plt.title(f"T={T}, K={K}")
plt.show()


##1次遅れ系のステップ応答（時定数Tを変化させる）
K = 1
T = (1, 0.5, 0.1)   #3種類の時定数を用意

#図示の準備
fig2, ax2 = plt.subplots()
LS = linestyle_generator()  #線種を与える関数(自作のfor_plotライブラリより)

for i in range(len(T)):
    P = tf([0, K], [T[i], 1])  #1次遅れ系
    y, t = step(P, np.arange(0, 5, 0.01))   #ステップ応答（0~5秒で，0.01刻み）
    ax2.plot(t, y, ls=next(LS), label=f"T={T[i]}")

plot_set(ax2, 't', 'y', 'best')
plt.title(f"T={T}, K={K}")
plt.show()


##1次遅れ系のステップ応答（ゲインKを変化させる）
T = 0.5
K = (1, 2, 3)   #3種類のゲインを用意

#図示の準備
fig3, ax3 = plt.subplots()
LS = linestyle_generator()  #線種を与える関数(自作のfor_plotライブラリより)

for i in range(len(K)):
    P = tf([0, K[i]], [T, 1])  #1次遅れ系
    y, t = step(P, np.arange(0, 5, 0.01))   #ステップ応答（0~5秒で，0.01刻み）
    ax3.plot(t, y, ls=next(LS), label=f"K={K[i]}")

plot_set(ax3, 't', 'y', 'best')
plt.title(f"T={T}, K={K}")
plt.show()


