"""
2021/04/11
@Yuya Shimizu

ボード線図
"""
import matplotlib.pyplot as plt
import numpy as np
from control import tf, c2d
from control.matlab import bode
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
fig, ax = plt.subplots(2, 1)

#連続時間システム
gain, phase, w = bode(P, np.logspace(-2, 2), Plot = False)
ax[0].semilogx(w, 20*np.log10(gain), ls = '-.', label = 'continuous')
ax[1].semilogx(w, phase*180/np.pi, ls = '-.', label = 'continuous')

#離散時間システム（0次ホールドによる離散化）
gain, phase, w = bode(Pd1, np.logspace(-2, 2), Plot = False)
ax[0].semilogx(w, 20*np.log10(gain), ls = '-.', label = 'zoh')
ax[1].semilogx(w, phase*180/np.pi, ls = '-.', label = 'zoh')

#離散時間システム（双一次変換による離散化）
gain, phase, w = bode(Pd2, np.logspace(-2, 2), Plot = False)
ax[0].semilogx(w, 20*np.log10(gain), ls = '-.', label = 'tustin')
ax[1].semilogx(w, phase*180/np.pi, ls = '-.', label = 'tustin')

#周波数がw=pi/tsのところに線を引く
ax[0].axvline(np.pi/ts, lw = 0.5, c = 'k')
ax[1].axvline(np.pi/ts, lw = 0.5, c = 'k')
ax[1].legend()

ax[0].set_ylabel('Gain [dB]')
ax[1].set_ylabel('Phase [deg]')
ax[1].set_xlabel('$\omega$ [rad/s]')
fig.tight_layout()
plt.show()
