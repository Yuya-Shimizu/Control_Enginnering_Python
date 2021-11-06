"""
2021/04/10
@Yuya Shimizu

乗法的不確かさを有する制御対象
"""
import numpy as np
import matplotlib.pyplot as plt
from control import bode, tf
from control.matlab import logspace
from tf_arm import arm_tf
from for_plot import bodeplot_set

###垂直アームのノミナルモデル
g    = 9.81               #重力加速度 [m/s^2]
l     = 0.2                 #アームの長さ[m]
M   = 0.5                 #アームの質量[kg]
mu = 1.5e-2            #粘性摩擦係数[kg*m^2/s]
J    = 1.0e-2            #慣性モーメント[kg*m^2]

Pn = arm_tf(J, mu, M, g, l)


###不確かさ
delta = np.arange(-1, 1, 0.1)
WT = tf([10, 0], [1, 150])

fig, ax = plt.subplots(1, 2)

for i in range(len(delta)):
    #不確かさをもつ制御対象
    P = (1 + WT*delta[i])*Pn
    gain, _, w = bode(P, logspace(-3, 3), Plot = False)
    ax[0].semilogx(w, 20*np.log10(gain), color='k', lw=0.3)

    #乗法的不確かさ
    DT = (P - Pn)/Pn
    gain, _, w = bode(DT, logspace(-3, 3), Plot = False)
    ax[1].semilogx(w, 20*np.log10(gain), color='k', lw=0.3)

gain, _, w = bode(Pn, logspace(-3, 3), Plot = False)
ax[0].semilogx(w, 20*np.log10(gain), color='k', lw=2)
gain, _, w = bode(WT, logspace(-3, 3), Plot = False)
ax[1].semilogx(w, 20*np.log10(gain), color='k', lw=2)

bodeplot_set(ax)
ax[0].set_xlabel('$\omega$ [rad/s]')
ax[0].set_ylabel('Gain of $P$ [dB]')
ax[1].set_xlabel('$\omega$ [rad/s]')
ax[1].set_ylabel('Gain of $\Delta W_T/P$ [dB]')

fig.suptitle("Gain of control target with Certainty")
plt.show()
