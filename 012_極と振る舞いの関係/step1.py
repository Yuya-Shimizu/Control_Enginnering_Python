"""
2021/03/05
@Yuya Shimizu

極と振る舞い（1次遅れ系）
"""

from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
from for_plot import *    #自分で定義した関数をインポート
#定義した関数について (https://qiita.com/Yuya-Shimizu/items/f811317d733ee3f45623)


##1次遅れ系のステップ応答

K = 1   #ゲインの設定
T = (1, 0.2, -0.2, -1)  #時定数の設定

y=[]
t=[]

for i in range(len(T)):
    P = tf([0, K], [T[i], 1])  #1次遅れ系
    yy, tt = step(P, np.arange(0, 5, 0.01))   #ステップ応答（0~5秒で，0.01刻み）
    y.append(yy)
    t.append(tt)

for i in range(len(T)):
    fig, ax = plt.subplots()
    ax.plot(t[i], y[i])
    plot_set(ax, 't', 'y') #グリッドやラベルを与える関数(自作のfor_plotライブラリより)
    plt.title(f"T={T[i]}, K={K}")
    plt.show()

#1つの図にまとめる
fig, ax = plt.subplots()
LS = linestyle_generator()  #線種を与える関数(自作のfor_plotライブラリより)
for i in range(len(T)):
    ax.plot(t[i], y[i], ls=next(LS), label=f"T={T[i]}")
plot_set(ax, 't', 'y', 'best')
ax.set_ylim(-1.2, 1.2)
plt.title(f"T={T}, K={K}")
plt.show()

