"""
2021/03/24
@Yuya Shimizu

安定なナイキスト線図と不安定なナイキスト線図
"""

import matplotlib.pyplot as plt
from control import tf, nyquist
from control.matlab import logspace
from for_plot import plot_set

P = tf([0, 1], [1, 1, 1.5, 1])
P2 = tf([0, 1], [1, 2, 2, 1])

##ナイキスト線図
fig, ax = plt.subplots(1, 2)

#閉ループ系が不安定になる場合
P = tf([0, 1], [1, 1, 1.5, 1])
x, y, _ = nyquist(P, logspace(-3, 5, 1000), Plot=False)
ax[0].plot(x, y, color='k')
ax[0].plot(x, -y, ls='--', color='k')
ax[0].scatter(-1, 0, color='r')
ax[0].set_title('unstable')
plot_set(ax[0], 'Re', 'Im')

#閉ループ系が不安定になる場合
P = tf([0, 1], [1, 2, 2, 1])
x, y, _ = nyquist(P, logspace(-3, 5, 1000), Plot=False)
ax[1].plot(x, y, color='k')
ax[1].plot(x, -y, ls='--', color='k')
ax[1].scatter(-1, 0, color='r')
ax[1].set_title('stable')
plot_set(ax[1], 'Re', 'Im')

fig.suptitle('Nyquist', size=15)
plt.show()
