"""
2021/03/05
@Yuya Shimizu

極と振る舞い（2次遅れ系）
"""

from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
from for_plot import *    #自分で定義した関数をインポート
#定義した関数について (https://qiita.com/Yuya-Shimizu/items/f811317d733ee3f45623)

##2次遅れ系のステップ応答（固有角振動数omega_nを変化させる）
zeta = 0.8
omega_n = (-1, -0.5, 0, 0.5, 1)   #3種類の固有角振動数を用意
K = 1

y=[]
t=[]

for i in range(len(omega_n)):
    P = tf([0, K*omega_n[i]**2], [1, 2*zeta*omega_n[i], omega_n[i]**2])  #2次遅れ系
    yy, tt = step(P, np.arange(0, 5, 0.01))   #ステップ応答（0~5秒で，0.01刻み）
    y.append(yy)
    t.append(tt)

#図示
for i in range(len(omega_n)):
    fig, ax = plt.subplots()
    ax.plot(t[i], y[i])
    plot_set(ax, 't', 'y') #グリッドやラベルを与える関数(自作のfor_plotライブラリより)
    plt.title(f"$\zeta$={zeta}, $\omega_n$={omega_n[i]}, K={K}")
    plt.show()

#図示の準備
fig, ax = plt.subplots()
LS = linestyle_generator()  #線種を与える関数(自作のfor_plotライブラリより)

for i in range(len(omega_n)):
    ax.plot(t[i], y[i], ls=next(LS), label=f"$\omega_n$={omega_n[i]}")

plot_set(ax, 't', 'y', 'best')
ax.set_ylim(0, 1.2)
plt.title(f"$\zeta$={zeta}, $\omega_n$={omega_n}, K={K}")
plt.show()

##2次遅れ系のステップ応答（減衰係数zetaを変化させる）
zeta = (0, 0.2, 0.8)   #5種類の減衰係数を用意
omega_n = 5
K = 1

y=[]
t=[]

for i in range(len(zeta)):
    P = tf([0, K*omega_n**2], [1, 2*zeta[i]*omega_n, omega_n**2])  #2次遅れ系
    yy, tt = step(P, np.arange(0, 5, 0.01))   #ステップ応答（0~5秒で，0.01刻み）
    y.append(yy)
    t.append(tt)

#図示
for i in range(len(zeta)):
    fig, ax = plt.subplots()
    ax.plot(t[i], y[i])
    plot_set(ax, 't', 'y') #グリッドやラベルを与える関数(自作のfor_plotライブラリより)
    plt.title(f"$\zeta$={zeta[i]}, $\omega_n$={omega_n}, K={K}")
    plt.show()
    
#図示の準備
fig, ax = plt.subplots()
LS = linestyle_generator()  #線種を与える関数(自作のfor_plotライブラリより)

for i in range(len(zeta)):
    ax.plot(t[i], y[i], ls=next(LS), label=f"$\zeta$={zeta[i]}")

plot_set(ax, 't', 'y', 'best')
plt.title(f"$\zeta$={zeta}, $\omega_n$={omega_n}, K={K}")
plt.show()
