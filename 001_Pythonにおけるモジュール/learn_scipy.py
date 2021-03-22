"""
2021/02/11
@Yuya Shimizu

Scipyについての簡単なまとめ
"""
#微分方程式を解くためのodeintをインポート
from scipy.integrate import odeint

import numpy as np
from matplotlib import pyplot as plt


"""dy = -1/5 y + 1/5 u
    この微分方程式の数値積分を実行する
    いま，入力を次のようにする
    u = 0 (t<10) or u = 1 (t>=10)
"""

#微分方程式の定義
def system(y, t):
    if t < 10.0:
        u = 0.0
    else:
        u = 1.0

    dydt = (-y + u)/5.0

    return dydt


#初期値と時間を設定して，微分方程式を解く
y0 = 0.5
t = np.arange(0, 40, 0.04)
y = odeint(system, y0, t)


#グラフを描画
fig, ax = plt.subplots()

ax.plot(t, y, label = 'y')
ax.plot(t, 1 * (t>=10), linestyle = '--', color = 'k', label = 'u')
ax.set_title('Differential equation: dydt = (-y + u)/5.0')
ax.set_xlabel('t')
ax.set_ylabel('y, u')
ax.legend(loc = 'best')
ax.grid(linestyle = ':')

fig.show()

fig.savefig('scipy_微分方程式.jpg')
