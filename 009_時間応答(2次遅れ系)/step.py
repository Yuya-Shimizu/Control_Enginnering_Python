"""
2021/02/27
@Yuya Shimizu

時間応答（2次遅れ系）
"""

from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
from for_plot import *    #自分で定義した関数をインポート
#定義した関数について (https://qiita.com/Yuya-Shimizu/items/f811317d733ee3f45623)


##2次遅れ系のステップ応答

zeta, omega_n, K = 0.4, 5, 1   #減衰係数と固有角振動数とゲインの設定
P = tf([0, K*omega_n**2], [1, 2*zeta*omega_n, omega_n**2])  #2次遅れ系
y, t = step(P, np.arange(0, 5, 0.01))   #ステップ応答（0~5秒で，0.01刻み）

fig1, ax1 = plt.subplots()
ax1.plot(t, y)
plot_set(ax1, 't', 'y') #グリッドやラベルを与える関数(自作のfor_plotライブラリより)
plt.title(f"$\zeta$={zeta}, $\omega_n$={omega_n}, K={K}")
plt.show()


##2次遅れ系のステップ応答（減衰係数zetaを変化させる）
zeta = (-0.1, 0, 0.3, 0.7, 1)   #5種類の減衰係数を用意
omega_n = 5
K = 1

#図示の準備
fig2, ax2 = plt.subplots()
LS = linestyle_generator()  #線種を与える関数(自作のfor_plotライブラリより)

for i in range(len(zeta)):
    P = tf([0, K*omega_n**2], [1, 2*zeta[i]*omega_n, omega_n**2])  #2次遅れ系
    y, t = step(P, np.arange(0, 3, 0.01))   #ステップ応答（0~3秒で，0.01刻み）
    ax2.plot(t, y, ls=next(LS), label=f"$\zeta$={zeta[i]}")

plot_set(ax2, 't', 'y', 'best')
plt.title(f"$\zeta$={zeta}, $\omega_n$={omega_n}, K={K}")
plt.show()


##2次遅れ系のステップ応答（固有角振動数omega_nを変化させる）
zeta = 0.7
omega_n = (1, 5, 10)   #3種類の固有角振動数を用意
K = 1

#図示の準備
fig3, ax3 = plt.subplots()
LS = linestyle_generator()  #線種を与える関数(自作のfor_plotライブラリより)

for i in range(len(omega_n)):
    P = tf([0, K*omega_n[i]**2], [1, 2*zeta*omega_n[i], omega_n[i]**2])  #2次遅れ系
    y, t = step(P, np.arange(0, 5, 0.01))   #ステップ応答（0~5秒で，0.01刻み）
    ax3.plot(t, y, ls=next(LS), label=f"$\omega_n$={omega_n[i]}")

plot_set(ax3, 't', 'y', 'best')
plt.title(f"$\zeta$={zeta}, $\omega_n$={omega_n}, K={K}")
plt.show()


##2次遅れ系のステップ応答（ゲインKを変化させる）
zeta = 0.7
omega_n = 5
K = (1, 2, 3)   #3種類のゲインを用意

#図示の準備
fig3, ax3 = plt.subplots()
LS = linestyle_generator()  #線種を与える関数(自作のfor_plotライブラリより)

for i in range(len(K)):
    P = tf([0, K[i]*omega_n**2], [1, 2*zeta*omega_n, omega_n**2])  #2次遅れ系
    y, t = step(P, np.arange(0, 5, 0.01))   #ステップ応答（0~5秒で，0.01刻み）
    ax3.plot(t, y, ls=next(LS), label=f"K={K[i]}")

plot_set(ax3, 't', 'y', 'best')
plt.title(f"$\zeta$={zeta}, $\omega_n$={omega_n}, K={K}")
plt.show()

