"""
2021/03/05
@Yuya Shimizu

零点と振る舞い
"""

from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
from for_plot import *    #自分で定義した関数をインポート
#定義した関数について (https://qiita.com/Yuya-Shimizu/items/f811317d733ee3f45623)


##零点による振る舞いの変化
zeta = 0.3          #減衰係数
omega_n = 5      #固有角振動数
K = 1                 #ゲイン

Np = [[0, K*omega_n**2],        #P1 : 零点なし 
          [3, K*omega_n**2],        #P2 : 安定零点
          [-3, K*omega_n**2]]        #P3 :  不安定零点
    
#図示の準備
fig, ax = plt.subplots()
LS = linestyle_generator()  #線種を与える関数(自作のfor_plotライブラリより)

for i in range(len(Np)):
    P = tf(Np[i], [1, 2*zeta*omega_n, omega_n**2])
    y, t = step(P, np.arange(0, 5, 0.01))   #ステップ応答（0~5秒で，0.01刻み）
    ax.plot(t, y, ls=next(LS), label=f"$P_{i+1}$")

plot_set(ax, 't', 'y', 'best')
plt.title(f"$\zeta$={zeta}, $\omega_n$={omega_n}, K={K}")
plt.show()
