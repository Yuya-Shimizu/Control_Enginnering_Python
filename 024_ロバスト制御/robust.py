"""
2021/04/10
@Yuya Shimizu

ロバスト制御器の設計
"""
import numpy as np
import matplotlib.pyplot as plt
from control import bode, tf, mixsyn, ss2tf
from control.matlab import logspace, feedback, step
from tf_arm import arm_tf
from for_plot import plot_set

###垂直アームのノミナルモデル
g    = 9.81               #重力加速度 [m/s^2]
l     = 0.2                 #アームの長さ[m]
M   = 0.5                 #アームの質量[kg]
mu = 1.5e-2            #粘性摩擦係数[kg*m^2/s]
J    = 1.0e-2            #慣性モーメント[kg*m^2]

Pn = arm_tf(J, mu, M, g, l)

###重み関数の定義
WS = tf([0, 1], [1, 1, 0.25])   #感度関数に対する重み関数
WU = tf(1, 1)
WT = tf([10, 0], [1, 150])   #相補感度関数に対する重み関数


###混合感度問題
K, _, gamma = mixsyn(Pn, w1 = WS, w2 = WU, w3 = WT) #混合感度問題を解く
print('K=', ss2tf(K))
print('gamma=', gamma[0])

fig, ax = plt.subplots(1, 2)
###感度関数
Ssys = feedback(1, Pn*K)
gain, _, w = bode(Ssys, logspace(-3, 3), Plot = False)
ax[0].semilogx(w, 20*np.log10(gain), lw=2, label='$S$')
gain, _, w = bode(1/WS, logspace(-3, 3), Plot = False)
ax[0].semilogx(w, 20*np.log10(gain), ls='-.', label='$1/W_S$')

###相補感度関数
Tsys = feedback(Pn*K, 1)
gain, _, w = bode(Tsys, logspace(-3, 3), Plot = False)
ax[1].semilogx(w, 20*np.log10(gain), lw=2, label='$T$')
gain, _, w = bode(1/WT, logspace(-3, 3), Plot = False)
ax[1].semilogx(w, 20*np.log10(gain), ls='--', label='$1/W_T$')

for i in range(2):
    ax[i].set_ylim(-40, 40)
    ax[i].legend()
    ax[i].grid(which="both", ls=':')
    ax[i].set_ylabel('Gain [dB]')
    ax[i].set_xlabel('$\omega$ [rad/s]')

fig.tight_layout()
fig.suptitle("robust controller")
plt.show()

###設計した制御器の性能確認
fig, ax = plt.subplots()
ref = 30      #目標値30
#不確かさ
delta = np.arange(-1, 1, 0.1)
WT = tf([10, 0], [1, 150])

#不確かさを有するモデルに対する性能
for i in range(len(delta)):
    #不確かさをもつ制御対象
    P = (1 + WT*delta[i])*Pn
    Gyr = feedback(P*K, 1)
    y, t = step(Gyr, np.arange(0, 5, 0.01))
    ax.plot(t, y*ref, color='k', lw=0.3)

#ノミナルモデル（不確かさなし）に対する性能
Gyr = feedback(Pn*K, 1)
y, t = step(Gyr, np.arange(0, 5, 0.01))
ax.plot(t, y*ref, color='r', lw=2, label="nominal model")
ax.legend()
plot_set(ax, 't', 'y')

ax.set_title("robust controller test in model")
plt.show()
