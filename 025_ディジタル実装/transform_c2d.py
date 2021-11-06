"""
2021/04/11
@Yuya Shimizu

連続時間システムから離散時間システムへの変換
"""
import matplotlib.pyplot as plt
import numpy as np
from control import tf, c2d
from control.matlab import step
from for_plot import plot_set

P = tf([0, 1], [0.5, 1])
print(P)

###数式

ts = 0.2    #サンプリング時間

# 0次ホールドによる離散化
Pd1 = c2d(P, ts, method='zoh')
print('離散時間システム（zoh）', Pd1)
# 双一次変換による離散化
Pd2 = c2d(P, ts, method='tustin')
print('離散時間システム（tustin）', Pd2)


###図示
fig, ax = plt.subplots(1, 2, figsize = (6, 2.6))

#連続時間システム
Tc = np.arange(0, 3, 0.01)
y, t = step(P, Tc)
ax[0].plot(t, y, ls = '-.')
ax[1].plot(t, y, ls = '-.')

#離散時間システム（0次ホールドによる離散化）
T = np.arange(0, 3, ts)
y, t = step(Pd1, T)
ax[0].plot(t, y, ls = ' ', marker = 'o', label = 'zoh')

#離散時間システム（双一次変換による離散化）
y, t = step(Pd2, T)
ax[1].plot(t, y, ls = ' ', marker = 'o', label = 'tustin')

title = ['0th hold', 'Tustin']
for i in range(2):
    ax[i].set_xlabel('t')
    ax[i].set_ylabel('y')
    ax[i].set_title(title[i])
    ax[i].legend()
fig.tight_layout()
plt.show()
